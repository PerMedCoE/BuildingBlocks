
rm(list=ls())

suppressPackageStartupMessages({
  # if (!require("pacman")) install.packages("pacman")
  # list.of.packages <- c("BiocManager","dplyr","SingleR","Matrix","Seurat","future","pheatmap","ggplot2","optparse","hdf5r")
  # BiocManager::install("SingleR")
  # BiocManager::install('limma')
  # BiocManager::install('SingleCellExperiment')
  # pacman::p_load(list.of.packages, character.only = TRUE)
  library(SingleR)
  library(dplyr)
  library(Matrix)
  library(Seurat)
  library(future)
  library(pheatmap)
  library(ggplot2)
  library(optparse)
})

###################### INPUT

option_list = list(
  make_option(c("-i", "--id"), type="character", default=NULL, help="Patient id", metavar="character"),
  make_option(c("-g", "--group"), type="character", default=NULL, help="Patient group", metavar="character"),
  make_option(c("-f", "--file"), type="character", default=NULL, help="Patient file", metavar="character"),
  make_option(c("-o", "--outdir"), type="character", default=NULL, help="Output folder", metavar="character"),
  make_option(c("-n", "--norm_data"), type="character", default=NULL, help="Output normalized data", metavar="character"),
  make_option(c("-r", "--raw_data"), type="character", default=NULL, help="Output raw data", metavar="character"),
  make_option(c("-c", "--scaled_data"), type="character", default=NULL, help="Output scaled data", metavar="character"),
  make_option(c("-m", "--cells_metadata"), type="character", default=NULL, help="Output cells metadata", metavar="character"),
  make_option(c("-v", "--verbose"), type="logical", default=T, help="Verbose", metavar="T|F"),
  make_option(c("-s", "--serialize"), type="logical", default=F, help="Save Seurat object", metavar="T|F"),
  make_option(c("-p", "--parallelize"), type="integer", default=1, help="Number of CPUs used to parallelize", metavar="integer_number")
)
opt_parser <- OptionParser(option_list=option_list, add_help_option = T)
opt <- parse_args(opt_parser)

# EVALUATE CLI
if (is.null(opt$id)){
  print_help(opt_parser)
  stop("No id provided", call.=FALSE)
}
if (is.null(opt$group)){
  print_help(opt_parser)
  stop("No group provided", call.=FALSE)
}
if (is.null(opt$file)){
  print_help(opt_parser)
  stop("No file provided", call.=FALSE)
}
if (is.null(opt$outdir)){
  print_help(opt_parser)
  stop("No output folder provided", call.=FALSE)
}
if (is.null(opt$norm_data)){
  print_help(opt_parser)
  stop("No norm data output file provided", call.=FALSE)
}
if (is.null(opt$raw_data)){
  print_help(opt_parser)
  stop("No raw data output file provided", call.=FALSE)
}
if (is.null(opt$scaled_data)){
  print_help(opt_parser)
  stop("No scaled data output file provided", call.=FALSE)
}
if (is.null(opt$cells_metadata)){
  print_help(opt_parser)
  stop("No cells metadata output file provided", call.=FALSE)
}



cat("\n\n")
cat("***********************************\n")
cat("*** SINGLE-CELL DATA PROCESSING ***\n")
cat("***********************************\n\n")
cat("id: ", opt$id, "\n")
cat("group: ", opt$group, "\n")
cat("file: ", opt$file, "\n")
cat("outdir: ", opt$outdir, "\n")
cat("verbose: ", opt$verbose, "\n")
cat("parallelize: ", opt$parallelize, "\n\n")


# Internal parallelization of Seurat using future.
# Only these functions are parallelized: NormalizeData, ScaleData, FindClusters (and JackStraw, FindMarkers, FindIntegrationAnchors)
# From https://satijalab.org/seurat/archive/v3.0/future_vignette.html
if (opt$parallelize > 1){
  plan("multicore", workers = opt$parallelize)
}

###################### LOAD DATA

# create working directory
dir.create(opt$outdir)

my_ggsave <- function(obj, filename){
  suppressMessages(ggsave(obj, filename = filename))
}

# process samples
sobjs <- list()

cat("  > Processing sample ",opt$id,")\n", sep="")

###################### INIT
cat("      - Init\n")

# init seurat object
raw_counts <- Read10X_h5(opt$file, use.names = T, unique.features = T)
sobj <- CreateSeuratObject(counts = raw_counts, min.cells = 3, min.features = 200, project = opt$id)

# create sample directory
sample_dir <- opt$outdir
dir.create(sample_dir, showWarnings = F)

sobj@misc$plots <- list()

###################### QC
cat("      - QC\n")

sobj[["percent.mt"]] <- PercentageFeatureSet(sobj, pattern = "^MT-")

sobj@misc$plots$qc_violin <- VlnPlot(sobj, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3, pt.size = .25)
my_ggsave(sobj@misc$plots$qc_violin, filename = paste0(sample_dir, "/qc_violin.png"))

plot1 <- FeatureScatter(sobj, feature1 = "nCount_RNA", feature2 = "percent.mt")
plot2 <- FeatureScatter(sobj, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
sobj@misc$plots$qc_cross <- plot1 + plot2
my_ggsave(sobj@misc$plots$qc_cross, filename = paste0(sample_dir, "/qc_cross.png"))


###################### FILTERING
cat("      - Filtering\n")

# empty droplets or double droplets ?
sobj@misc$pre_filt_dim <- dim(sobj@assays$RNA)
sobj <- subset(sobj, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 10)
sobj@misc$post_filt_dim <- dim(sobj@assays$RNA)


###################### NORMALIZATION
cat("      - Normalization\n")

sobj <- NormalizeData(object = sobj, verbose = F)


###################### VARIABLE FEATURES
cat("      - Find variable features\n")

sobj <- FindVariableFeatures(object = sobj, selection.method = "vst", nfeatures = 2000, verbose = F)
top10 <- head(VariableFeatures(sobj), 10)
plot1 <- VariableFeaturePlot(sobj)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
sobj@misc$plots$variable_features <- plot1 + plot2
# TODO: WHY FAILS (JCB)
#my_ggsave(sobj@misc$plots$variable_features, filename = paste0(sample_dir, "/variable_features.png"))


###################### SCALE DATA
cat("      - Scaling\n")

sobj <- ScaleData(object = sobj, verbose = F)


###################### DIM REDUCTION
cat("      - Dimensionality reduction\n")

## PCA
sobj <- RunPCA(object = sobj, features = VariableFeatures(object = sobj), verbose = F)
# loadings
sobj@misc$plots$pca_loadings <- VizDimLoadings(sobj, dims = 1:4, reduction = "pca")
my_ggsave(sobj@misc$plots$pca_loadings, filename = paste0(sample_dir, "/pca_loadings.png"))
# elbow
sobj@misc$plots$pca_elbow <- ElbowPlot(sobj, ndims = 40)
my_ggsave(sobj@misc$plots$pca_elbow, filename = paste0(sample_dir, "/pca_elbow.png"))
#
sobj@misc$plots$pca_main <- DimPlot(object = sobj, reduction = "pca")
my_ggsave(sobj@misc$plots$pca_main, filename = paste0(sample_dir, "/pca_main.png"))
sobj@misc$plots$pca_heatmap <- DimHeatmap(sobj, dims = 1:4, ncol=2, nfeatures = 30, cells = 1000, balanced = TRUE, fast = F)
my_ggsave(sobj@misc$plots$pca_heatmap, filename = paste0(sample_dir, "/pca_heatmap.png"))

# # number of components
# sobj <- JackStraw(sobj, num.replicate = 100, dims=20)
# sobj <- ScoreJackStraw(sobj, dims = 1:20)
# JackStrawPlot(sobj, dims = 1:20)

## T-SNE
sobj <- RunTSNE(object = sobj, dims = 1:20, verbose = F)
sobj@misc$plots$tsne_main <- DimPlot(object = sobj, reduction = "tsne")
my_ggsave(sobj@misc$plots$tsne_main, filename = paste0(sample_dir, "/tsne_main.png"))

## U-MAP
sobj <- RunUMAP(object = sobj, dims=1:20, verbose = F)
sobj@misc$plots$umap_main <- DimPlot(object = sobj, reduction = "umap")
my_ggsave(sobj@misc$plots$umap_main, filename = paste0(sample_dir, "/umap_main.png"))


###################### FIND CLUSTERS
cat("      - Find clusters\n")

sobj <- FindNeighbors(object = sobj, verbose = F)
sobj <- FindClusters(object = sobj, verbose = F)

sobj@misc$plots$pca_clusters <- DimPlot(object = sobj, reduction = "pca")
my_ggsave(sobj@misc$plots$pca_clusters, filename = paste0(sample_dir, "/pca_clusters.png"))
sobj@misc$plots$tsne_clusters <- DimPlot(object = sobj, reduction = "tsne")
my_ggsave(sobj@misc$plots$tsne_clusters, filename = paste0(sample_dir, "/tsne_clusters.png"))
sobj@misc$plots$umap_clusters <- DimPlot(object = sobj, reduction = "umap")
my_ggsave(sobj@misc$plots$umap_clusters, filename = paste0(sample_dir, "/umap_clusters.png"))


###################### GENE MARKERS
cat("      - Gene markers by cluster\n")

# find markers for every cluster compared to all remaining cells, report only the positive ones
sobj.markers <- FindAllMarkers(sobj, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25, verbose = F)
# XXX
# sobj.markers %>% group_by(cluster) %>% top_n(n = 2, wt = avg_logFC)
sobj.markers %>% group_by(cluster) %>% top_n(n = 2, wt = avg_log2FC)
sobj@misc$markers <- sobj.markers
# XXX
# top10 <- sobj.markers %>% group_by(cluster) %>% top_n(n = 10, wt = avg_logFC)
top10 <- sobj.markers %>% group_by(cluster) %>% top_n(n = 10, wt = avg_log2FC)
sobj@misc$plots$markers <- DoHeatmap(sobj, features = top10$gene) + NoLegend()
my_ggsave(sobj@misc$plots$markers, filename = paste0(sample_dir, "/markers.png"))

# XXX
###################### CELL TYPE IDENTIFICATION
# cat("      - Cell type identification\n")
#
# # Bioconductor obj
# sobj_se <- as.SingleCellExperiment(sobj)
#
# # Select reference dataset
# # ref <- SingleR::BlueprintEncodeData()
# # ref <- SingleR::DatabaseImmuneCellExpressionData()
# ref <- SingleR::HumanPrimaryCellAtlasData()
# # ref <- SingleR::MonacoImmuneData()
#
# # Prediction
# pred <- SingleR(test=sobj_se, ref=ref, labels=ref$label.main)
# sobj@misc$cell_type_ref <- ref
# sobj@misc$cell_type_pred <- pred
# sobj@misc$plots$cell_type_pred_dist <- plotScoreDistribution(pred, size = .25)
# my_ggsave(sobj@misc$plots$cell_type_pred_dist, filename = paste0(sample_dir, "/cell_type_pred_dist.png"))
# sobj@misc$plots$cell_type_pred_heatmap <- plotScoreHeatmap(pred,show.pruned = T)
# my_ggsave(sobj@misc$plots$cell_type_pred_heatmap, filename = paste0(sample_dir, "/cell_type_pred_heatmap.png"))
#
# # Cell type freqs
# png(paste0(sample_dir, "/cell_type_freqs.png"), width=800, height=700, pointsize = 20)
# par(mar=c(5,10,3,3))
# freqs <- sort(table(pred$labels), decreasing = F)
# barplot(freqs, horiz=T, las=2)
# dev.off()
#
# # Cell type to clusters
# pheatmap(log(10+table(pred$labels, sobj$seurat_clusters)), filename = paste0(sample_dir, "/cell_type_to_cluster.png"))
#
# # dim reduction plots
# sobj[["cell_type"]] <- pred$labels
# sobj@misc$plots$pca_cell_types <- DimPlot(object = sobj, reduction = "pca", group.by = "cell_type")
# my_ggsave(sobj@misc$plots$pca_cell_types, filename = paste0(sample_dir, "/pca_cell_types.png"))
# sobj@misc$plots$tsne_cell_types <- DimPlot(object = sobj, reduction = "tsne", group.by = "cell_type")
# my_ggsave(sobj@misc$plots$tsne_cell_types, filename = paste0(sample_dir, "/tsne_cell_types.png"))
# sobj@misc$plots$umap_cell_types <- DimPlot(object = sobj, reduction = "umap", group.by = "cell_type")
# my_ggsave(sobj@misc$plots$umap_cell_types, filename = paste0(sample_dir, "/umap_cell_types.png"))
#
#
# ## SUMMARIZE BY CELL TYPE
# summ_fun <- function(x) mean(x, trim=.005)
# summ_cells <- function(x, fun=summ_fun){
#   # print(dim(x))
#   apply(x,2,fun)
# }
# sobj@misc$cell_type_assay <- do.call("cbind",by(t(sobj@assays$RNA@data), pred$labels, summ_cells))


###################### FINISH
cat("      - Saving\n")

# TODO: WHY FAILS? (JCB)
#if(opt$serialize==T) save(sobj, file=paste0(sample_dir,"/seurat_object.RData"))

## TEXT FILES
# data
#write.table(sobj@assays$RNA@data, file=paste0(sample_dir, "/norm_data.tsv"), sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@data), quote=F)
write.table(sobj@assays$RNA@data, file=opt$norm_data, sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@data), quote=F)
#write.table(sobj@assays$RNA@counts, file=paste0(sample_dir, "/raw_data.tsv"), sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@counts), quote=F)
write.table(sobj@assays$RNA@counts, file=opt$raw_data, sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@counts), quote=F)
#write.table(sobj@assays$RNA@scale.data, file=paste0(sample_dir, "/scaled_data.tsv"), sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@scale.data), quote=F)
write.table(sobj@assays$RNA@scale.data, file=opt$scaled_data, sep="\t", row.names=T, col.names=colnames(sobj@assays$RNA@scale.data), quote=F)
# cell info
#write.table(sobj@meta.data, file=paste0(sample_dir, "/cells_metadata.tsv"), sep="\t", row.names=T, col.names=T, quote=F)
write.table(sobj@meta.data, file=opt$cells_metadata, sep="\t", row.names=T, col.names=T, quote=F)

cat("\n\n[finished]\n\n")
