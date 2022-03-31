
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

cat("\n\n")
cat("***********************************\n")
cat("******* PERSONALIZE MODEL *********\n")
cat("***********************************\n\n")

option_list = list(
  # make_option(c("-i", "--id"), type="character", default=NULL, help="Sample id", metavar="character"),
  make_option(c("-e", "--expression"), type="character", default=NULL, help="Normalized expression file", metavar="character"),
  make_option(c("-c", "--cnv"), type="character", default=NULL, help="Copy number variations file", metavar="character"),
  make_option(c("-m", "--mutations"), type="character", default=NULL, help="Mutations files", metavar="character"),
  make_option(c("-t", "--cell_line"), type="character", default=NULL, help="Selected cell line", metavar="character"),
  # make_option(c("-b", "--model_prefix"), type="character", default=NULL, help="Generic model prefix", metavar="character"),
  make_option(c("-x", "--model_bnd"), type="character", default=NULL, help="BND model", metavar="character"),
  make_option(c("-y", "--model_cfg"), type="character", default=NULL, help="CFG model", metavar="character"),
  make_option(c("-o", "--model_outdir"), type="character", default=NULL, help="Model output folder", metavar="character"),
  # make_option(c("-p", "--personalized_result"), type="character", default=NULL, help="Personalization result tsv", metavar="character"),
  # make_option(c("-k", "--ko_file"), type="character", default=NULL, help="KO genes file", metavar="character"),
  make_option(c("-r", "--rates_factor"), type="numeric", default=100, help="KO genes file", metavar="numeric"),
  make_option(c("-v", "--verbose"), type="logical", default=T, help="Verbose", metavar="T/F")
)
opt_parser <- OptionParser(option_list=option_list);
opt <- parse_args(opt_parser);


# EVALUATE CLI
if(is.null(opt$expression)){
  print_help(opt_parser)
  stop("No expression file provided", call.=FALSE)
}
if(is.null(opt$cell_line)){
  print_help(opt_parser)
  stop("No cell line file provided", call.=FALSE)
}
# if(is.null(opt$model_prefix)){
#  print_help(opt_parser)
#  stop("No model prefix provided", call.=FALSE)
#}
if(is.null(opt$model_bnd)){
  print_help(opt_parser)
  stop("No model bnd provided", call.=FALSE)
}
if(is.null(opt$model_cfg)){
  print_help(opt_parser)
  stop("No model cfg provided", call.=FALSE)
}

if(is.null(opt$model_outdir)) opt$model_outdir <- dirname(opt$exp_file)
# cat("sample id: ", sample_id, "\n")
cat("cell_line: ", opt$cell_line, "\n")
cat("expression file: ", opt$exp_file, "\n")
# cat("model prefix: ", opt$model_prefix, "\n")
cat("model bnd: ", opt$model_bnd, "\n")
cat("model cfg: ", opt$model_cfg, "\n")
cat("cell type: ", opt$cell_type, "\n")
# cat("ko file: ", opt$ko_file, "\n")
cat("model outdir: ", opt$model_outdir, "\n")
# cat("personalization result: ", opt$personalized_result, "\n")
cat("verbose: ", opt$verbose, "\n\n")


###################### LOAD DATA

dat <- read.table(opt$expression, header=T, sep=",", check.names = F, as.is=T)
opt$model_bnd
names(dat)[2] <- "symbol"
dat <- dat[-c(1,2,3),]
rownames(dat) <- dat$symbol
dat <- dat[,-c(1,2)]

norm_dat <- t(apply(data.matrix(dat), 1, function(x)(x-min(x))/(max(x)-min(x))))

# model <- load_model(paste0(opt$model_prefix,"/model.bnd"))
# cfg <- load_config(paste0(opt$model_prefix,"/model.cfg"))
model <- load_model(opt$model_bnd)
cfg <- load_config(opt$model_cfg)

###################### BINARIZE/NORMALIZE

all_nodes <- names(model)

subset <- data.matrix(norm_dat[rownames(norm_dat) %in% all_nodes,])

criteria <- compute_criteria(t(data.matrix(subset)))

get_rate <- function(value){
  round(digits = 4, opt$rates_factor^(2*value-1))
}

values <- subset[,opt$cell_line]

cfg2 <- cfg
for(i in 1:length(values)){
  gene <- names(values)[i]

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

###################### SAVE RESULTS

# write.table(values, file=opt$personalized_result, quote=F, sep="\t", row.names=T, col.names = T)


## PERSONALIZED MODELS
model_outdirs <- opt$model_outdir
dir.create(model_outdirs)

# wt
out_model_pref <- paste0(model_outdirs, "/model")
save_config(cfg2, filename=paste0(out_model_pref,".cfg"))
# file.copy(from=paste0(opt$model_prefix, "model.bnd"), to=paste0(out_model_pref,".bnd"))
file.copy(from=opt$model_bnd, to=paste0(out_model_pref,".bnd"))

cat("\n\n[finished]\n\n")
