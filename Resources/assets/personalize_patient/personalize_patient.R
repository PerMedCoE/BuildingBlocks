
rm(list=ls())

suppressPackageStartupMessages({
  # if (!require("pacman")) install.packages("pacman")
  # list.of.packages <- c("dplyr","tidyverse","diptest","mclust","moments","pheatmap","optparse")
  # pacman::p_load(list.of.packages, character.only = TRUE)
  library(dplyr)
  library(tidyverse)
  library(diptest)
  library(mclust)
  library(moments)
  library(pheatmap)
  library(optparse)
  source("profile.R")
})


###################### INPUT

option_list = list(
  # make_option(c("-i", "--id"), type="character", default=NULL, help="Sample id", metavar="character"),
  make_option(c("-e", "--exp_file"), type="character", default=NULL, help="Normalized expression file", metavar="character"),
  make_option(c("-c", "--cells_meta_file"), type="character", default=NULL, help="Cells metadata file", metavar="character"),
  make_option(c("-m", "--model_prefix"), type="character", default=NULL, help="Model prefix", metavar="character"),
  make_option(c("-t", "--cell_type"), type="character", default=NULL, help="Selected cell type", metavar="character"),
  make_option(c("-o", "--model_outdir"), type="character", default=NULL, help="Model output folder", metavar="character"),
  make_option(c("-p", "--personalized_result"), type="character", default=NULL, help="Personalization result tsv", metavar="character"),
  make_option(c("-k", "--ko_file"), type="character", default=NULL, help="KO genes file", metavar="character"),
  make_option(c("-r", "--rates_factor"), type="numeric", default=100, help="KO genes file", metavar="numeric"),
  make_option(c("-v", "--verbose"), type="logical", default=T, help="Verbose", metavar="T/F")
)
opt_parser <- OptionParser(option_list=option_list);
opt <- parse_args(opt_parser);


# EVALUATE CLI
if(is.null(opt$exp_file)){
  print_help(opt_parser)
  stop("No expression file provided", call.=FALSE)
}
if(is.null(opt$cells_meta_file)){
  print_help(opt_parser)
  stop("No cells metadata file provided", call.=FALSE)
}
if(is.null(opt$model_prefix)){
  print_help(opt_parser)
  stop("No model prefix provided", call.=FALSE)
}
if(is.null(opt$cell_type)){
  print_help(opt_parser)
  stop("No cell type selected provided", call.=FALSE)
}

if(is.null(opt$model_outdir)) opt$model_outdir <- dirname(opt$exp_file)

cat("\n\n")
cat("***********************************\n")
cat("******* PERSONALIZE MODEL *********\n")
cat("***********************************\n\n")
# cat("sample id: ", sample_id, "\n")
cat("expression file: ", opt$exp_file, "\n")
cat("cells metadata file: ", opt$cells_meta_file, "\n")
cat("model prefix: ", opt$model_prefix, "\n")
cat("cell type: ", opt$cell_type, "\n")
cat("ko file: ", opt$ko_file, "\n")
cat("model outdir: ", opt$model_outdir, "\n")
cat("personalization result: ", opt$personalized_result, "\n")
cat("verbose: ", opt$verbose, "\n\n")


###################### LOAD DATA

dat <- data.matrix(read.table(opt$exp_file, header=T, row.names = 1, sep="\t", check.names = F))

cmeta <- read.table(opt$cells_meta_file, sep="\t", header=T, stringsAsFactors = F)

model <- load_model(paste0(opt$model_prefix,".bnd"))
cfg <- load_config(paste0(opt$model_prefix,".cfg"))

kos <- NULL
if(!is.null(opt$ko_file)){
  kos <- read.table(opt$ko_file, stringsAsFactors = F)$V1
}

###################### BINARIZE/NORMALIZE

all_nodes <- names(model)

# TO-FIX 
# Target nodes in complexes that are not represented individually in the model
# complexes <- all_nodes[grep("complex",all_nodes)]
# complex_units <- unlist(strsplit(gsub("_complex", "", complexes),"_"))
# all_nodes <- unique(c(all_nodes, complex_units))

subset <- data.matrix(dat[rownames(dat) %in% all_nodes,])

criteria <- compute_criteria(t(data.matrix(subset)))
table(criteria$Category)

# DEBUG
# bimodals <- criteria$Gene[criteria$Category=="Bimodal"]
# dual_plot(dat[sample(bimodals,1),])
# zeroinf <- criteria$Gene[criteria$Category=="ZeroInf"]
# dual_plot(dat[sample(zeroinf,1),])
# discarded <- criteria$Gene[criteria$Category=="Discarded"]
# dual_plot(dat[sample(discarded,1),])


subset_bin <- t(binarize_exp(t(subset), t(subset), criteria, show.plot = T))
subset_bin[is.na(subset_bin)] <- 0

summarize_cells <- function(x, fun=mean) apply(x,2,fun)
# XXX
# subset_bin_cell_type_mean <- do.call("cbind", by(t(subset_bin), cmeta$cell_type, summarize_cells))
subset_bin_cell_type_mean <- do.call("cbind", by(t(subset_bin), cmeta$seurat_clusters, summarize_cells))
pheatmap(subset_bin_cell_type_mean)

# XXX
# subset_bin_cell_type_sd <- do.call("cbind", by(t(subset_bin), cmeta$cell_type, summarize_cells, fun=sd))
subset_bin_cell_type_sd <- do.call("cbind", by(t(subset_bin), cmeta$seurat_clusters, summarize_cells, fun=sd))
subset_bin_cell_type_sd[is.na(subset_bin_cell_type_sd)] <- 0
pheatmap(subset_bin_cell_type_sd)

# DEBUG
# ### FOR maboss_specific.py
# out <- data.frame(t(subset_bin_cell_type_mean[, cell_type]))
# out <- cbind(sample_id, out)
# colnames(out) <- c("", rownames(subset_bin_cell_type_mean))
# out_file <- paste0(dirname(exp_file),"/personalized__", cell_type, ".csv")
# write.table(out, file=out_file, quote = T, sep=",", row.names = F, col.names = T)

###################### PERSONALIZE THE MODEL

get_rate <- function(value){
  round(digits = 4, opt$rates_factor^(2*value-1))
}

# XXX
# values <- subset_bin_cell_type_mean[, opt$cell_type]
values <- subset_bin_cell_type_mean[, colnames(subset_bin_cell_type_mean)==3]

cfg2 <- cfg
for(i in 1:nrow(subset_bin_cell_type_mean)){
  gene <- rownames(subset_bin_cell_type_mean)[i]
  
  if(!is.null(cfg[[paste0(gene,".istate")]])){
    # ISTATE
    cfg2[[paste0(gene,".istate")]] <- round(c(values[gene], 1-values[gene]), digits=4)
    # RATES
    # up_value = round(rates_f**(2*value-1),5)
    # down_value = round(1/up_value,5)
    cfg2[[paste0("$u_", gene)]] <- get_rate(values[gene])
    cfg2[[paste0("$d_", gene)]] <- round(1/cfg2[[paste0("$u_", gene)]], digits=4)
  } else {
    warning(paste0("Gene ", gene, " has no .istate field"))
  }
}
# cfg2 <- cfg


# ADD KOS
cfg2_kos <- list()
if(!is.null(kos)){
  for(i in 1:length(kos)){
    cfg2_kos[[i]] <- cfg2
    cfg2_kos[[i]][[paste0("$",kos[i],"_ko")]] <- 1
  }
  names(cfg2_kos) <- kos
}


###################### SAVE RESULTS

write.table(subset_bin_cell_type_mean, file=opt$personalized_result, quote=F, sep="\t", row.names=T, col.names = T)

## PERSONALIZED MODELS
model_outdirs <- opt$model_outdir
dir.create(model_outdirs)

# wt
out_model_pref <- paste0(model_outdirs, "/", basename(opt$model_prefix), "_personalized")
save_config(cfg2, filename=paste0(out_model_pref,".cfg"))
file.copy(from=paste0(opt$model_prefix, ".bnd"), to=paste0(out_model_pref,".bnd"))

# mutants
if(!is.null(kos)){
  for(i in 1:length(kos)){
    out_model_pref <- paste0(model_outdirs, "/", basename(opt$model_prefix), "_personalized__", kos[i], "_ko")
    save_config(cfg2_kos[[i]], filename=paste0(out_model_pref,".cfg"))
    file.copy(from=paste0(opt$model_prefix, ".bnd"), to=paste0(out_model_pref,".bnd"))
  }
}


cat("\n\n[finished]\n\n")




