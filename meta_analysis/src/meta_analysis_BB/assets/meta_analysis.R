
# rm(list=ls())

suppressPackageStartupMessages({
  # library(SingleR)
  # library(dplyr)
  # library(Matrix)
  # library(Seurat)
  # library(future)
  library(pheatmap)
  # library(ggplot2)
  library(optparse)
  library(rmatio)
  library(RColorBrewer)
  source("physi_eval_utils.R")
})

###################### INPUT

option_list = list(
  make_option(c("-m", "--meta_file"), type="character", default=NULL, help="Metadata file", metavar="character"),
  make_option(c("-o", "--outdir"), type="character", default=NULL, help="Output folder", metavar="character"),
  # make_option(c("-s", "--serialize"), type="logical", default=F, help="Save Seurat object", metavar="T|F"),
  make_option(c("-p", "--model_prefix"), type="character", default=NULL, help="Model prefix", metavar="character"),
  # make_option(c("-t", "--cell_type"), type="character", default=NULL, help="Selected cell type", metavar="character"),
  make_option(c("-k", "--ko_file"), type="character", default=NULL, help="KO genes file", metavar="character"),
  make_option(c("-r", "--reps"), type="integer", default=NULL, help="Number of used simulation replicates", metavar="integer"),
  make_option(c("-v", "--verbose"), type="logical", default=T, help="Verbose", metavar="T|F"),
  make_option(c("-z", "--results_dir"), type="character", default=NULL, help="Output folder", metavar="character")
)
opt_parser <- OptionParser(option_list=option_list, add_help_option = T)
opt <- parse_args(opt_parser)

# EVALUATE CLI
if (is.null(opt$meta_file)){
  print_help(opt_parser)
  stop("No metadata file provided", call.=FALSE)
}
if (is.null(opt$out)){
  print_help(opt_parser)
  stop("No output folder provided", call.=FALSE)
}
if(is.null(opt$model_prefix)){
  print_help(opt_parser)
  stop("No model prefix provided", call.=FALSE)
}
# if(is.null(opt$cell_type)){
#   print_help(opt_parser)
#   stop("No cell type selected provided", call.=FALSE)
# }
if(is.null(opt$results_dir)){
  print_help(opt_parser)
  stop("No results directory provided", call.=FALSE)
}


# Hardcoded for testing purposes
#opt$verbose <- F
#opt$meta_file <- "data/metadata.tsv"
#opt$outdir <- "results_all"
#opt$model_prefix <- "data/epithelial_cell_2"
#opt$ko_file <- "data/ko_file.txt"
#opt$reps <- 2

cat("\n\n")
cat("***********************************\n")
cat("***        META-ANALYSIS        ***\n")
cat("***********************************\n\n")
cat("metadata file: ", opt$meta_file, "\n")
cat("outdir: ", opt$outdir, "\n")
cat("model prefix: ", opt$model_prefix, "\n")
# cat("cell type: ", opt$cell_type, "\n")
cat("ko file: ", opt$ko_file, "\n")
cat("replicates: ", opt$rep, "\n")
cat("verbose: ", opt$verbose, "\n")
cat("results_dir: ", opt$results_dir, "\n\n")


# set results directory
outdir <- opt$results_dir
dir.create(outdir)

###################### LOAD DATA

# read metadata
meta <- read.table(opt$meta_file, header=T, sep="\t", stringsAsFactors = F)
rownames(meta) <- meta$id

ugroups <- unique(meta$group)
group_colors <- brewer.pal(length(ugroups), "Set1")
names(group_colors) <- ugroups

# KOs
kos <- read.table(opt$ko_file, stringsAsFactors = F)$V1


# GET SIMULATIONS
sample_folders <- paste0(opt$outdir, "/", meta$id)
names(sample_folders) <- meta$id

model_name <- basename(opt$model_prefix)

meta_sim <- lapply(meta$id, function(id) {
  sims_prefix <- paste0(sample_folders[id],"/physiboss_results/", model_name, "_personalized", c("",paste0("__", kos,"_ko")), "_physiboss_run_")
  sims_folder <- paste0(rep(sims_prefix, each=opt$reps), rep(1:opt$reps, length(sims_prefix)))
  sample_meta_sim <- data.frame(
    id=id,
    ko=rep(c("WT",kos), each=opt$reps),
    rep=rep(1:opt$reps, length(sims_prefix)),
    sim_folder=sims_folder,
    stringsAsFactors = F
  )
})
meta_sim <- do.call("rbind", meta_sim)
rownames(meta_sim) <- paste0(meta_sim$id, "_", meta_sim$ko, "_rep", meta_sim$rep)


ukos <- unique(meta_sim$ko)
ko_colors <- brewer.pal(length(ukos), "Set2")
names(ko_colors) <- ukos

#
# sim <- meta_sim$sim_folder[1]
# xml <- paste0(sim,"/final.xml")
# mat_file <- paste0(sim,"/final_cells_physicell.mat")

# GET FINAL CELL'S MATRICES
fc_mats <- lapply(meta_sim$sim_folder, function(sim){

  xml <- paste0(sim,"/final.xml")
  mat_file <- paste0(sim,"/final_cells_physicell.mat")

  labels <- get_col_labels(xml)
  mat <- get_cell_matrix(mat_file, labels)
  # categorical <- c("cell_type", "cycle_model", "current_phase")
  # summaries <- summarize_mat(mat, exclude="ID", categorical=categorical)

  return(mat)
})

# variable params
var_params <- names(which(apply(fc_mats[[1]], 2, function(x) any(x!=x[1]))))
var_params_clean <- setdiff(var_params, c("ID", "position_1", "position_2", "position_3", "cell_type"))

# available cell types
all_cell_types <- as.character(unique(unlist(lapply(fc_mats, function(x) unique(x[,"cell_type"])))))


get_cell_type_proportion <- function(mats){
  do.call("rbind", lapply(mats, function(x) table(as.character(x[,"cell_type"]))[all_cell_types]))
}

###################### WT DESCRIPTIVE

trans <- function(x) log(x+.0000001)
plot_param <- function(msim, values, param, colors){
  boxplot(lapply(values,trans), col=colors, names=rownames(msim), las=2, main=param)
  return(NULL)
}

wt_indexes <- which(meta_sim$ko=="WT")
meta_sim_wt <- meta_sim[wt_indexes,]
wt_mats <- fc_mats[wt_indexes]

np <- length(var_params_clean)+1
nc <- floor(sqrt(np))
nr <- ceiling(np/nc)

png(paste0(outdir,"/wt_params.png"), width=100+400*nc, height=100+300*nr, pointsize = 20)
par(mfrow=c(nr,nc), mar=c(10,3,3,3), oma=c(3,3,7,3))
groups <- meta[meta_sim_wt$id, "group"]
lapply(var_params_clean, function(param) {
  values <- lapply(wt_mats, function(x) x[,param])
  invisible(plot_param(meta_sim_wt, values, param, colors=group_colors[groups]))
})
mtext("All variable params (WT)", outer=T, cex=1.5, padj=-2, col="#5555aa")
plot.new()
legend("center", legend = names(group_colors), col=group_colors, pch=15, bty="n", cex=1.4)
dev.off()


###################### BY PATIENT


for(i in 1:nrow(meta)){

  p_indexes <- which(meta_sim$id==meta_sim$id[i])
  meta_sim_p <- meta_sim[p_indexes,]
  p_mats <- fc_mats[p_indexes]

  png(paste0(outdir,"/", meta$id[i],"_params.png"), width=100+400*nc, height=100+300*nr, pointsize = 20)
  par(mfrow=c(nr,nc), mar=c(10,3,3,3), oma=c(3,3,7,3))
  groups <- meta[meta_sim_wt$id, "group"]
  lapply(var_params_clean, function(param) {
    values <- lapply(p_mats, function(x) x[,param])
    invisible(plot_param(meta_sim_p, values, param, colors=ko_colors[meta_sim_p$ko]))
  })
  mtext(paste0("All variable params (", meta$id[i],")"), outer=T, cex=1.5, padj=-2, col="#5555aa")
  plot.new()
  legend("center", legend = names(ko_colors), col=ko_colors, pch=15, bty="n", cex=1.4)
  dev.off()

}





