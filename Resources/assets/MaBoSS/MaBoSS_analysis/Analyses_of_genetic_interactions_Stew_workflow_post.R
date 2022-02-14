#!/usr/bin/env Rscript
rm(list=ls(all=TRUE))
# setwd(dir = "/home/rstudio/data/scripts/run all analyses/5 Analyses of genetic interactions/")

# if (!require("pacman")) install.packages("pacman")
# list.of.packages <- c("magrittr")
# pacman::p_load(list.of.packages, character.only = TRUE)

# import data ----
a1<- read.table("./epithelial_cell_2_epistasis/epithelial_cell_2_norm.xls", header = TRUE, sep="\t", row.names = 1, stringsAsFactors=FALSE)
a2<-a1[,-c(2:5,ncol(a1))]
colnames(a2)[2]<-"HS"
colnames(a2)<-gsub(".","-", colnames(a2),fixed = T)
rownames(a2)<-sub("^_","WT",rownames(a2),perl = F)
rownames(a2)<-sub("__","-",rownames(a2),perl = F)

b1 <- read.table("./epithelial_cell_2/epithelial_cell_2_probtraj_table.csv", header = TRUE, sep="\t", stringsAsFactors=FALSE)
b1 <- b1[,-ncol(b1)]
b2 <- b1[,!grepl("Err.*",colnames(b1))]
colnames(b2) <- gsub("\\.\\.","-",gsub("\\.$","", gsub("\\.nil\\.","HS", gsub("^Prob.","", colnames(b2)))))
b3 <- as.data.frame(t(b2[,4:ncol(b2)]))
b4 <- as.data.frame(t(b3[ order(-b3[,ncol(b3)]), ]))

inputs <- scan("./inputs.txt", sep="\n", what = character() )
outputs <- scan("./outputs.txt", sep="\n", what = character() )

# Interesting phenotypes:
# outputs %>% grep("type_I$",.,perl = T) #2
# outputs %>% grep("type_II$",.,perl = T) #3

# analyse data ----
a4<-a2[,-c(1)]
WT<-a4[which(rownames(a4)=="WT"),]

ratio<-scale(as.matrix(a4), center=FALSE, scale=as.matrix(WT))
ratio<-as.data.frame(ratio[order(rownames(ratio)), ])
ratio2<-ratio[which(!rownames(ratio) %in% paste0(inputs,"_ko")),]

# filter CASP and Apoptosome nodes as they are low level:
ignorenodes<- rownames(ratio2)[c(
  grep("CASP",rownames(ratio2)),
  grep("Apoptos",rownames(ratio2)))
]

# Type I:
ratio_typeI <- ratio2[with(ratio2, order(
  ratio2[,grep(paste0(outputs[2],"$"),colnames(ratio2),perl = T)],
  ratio2[,grep(paste0(outputs[3],"$"),colnames(ratio2),perl = T)]
  )),]

ratio_typeI <- ratio_typeI[which(ratio_typeI$`Apoptosis_phenotype-Apoptosis_type_I`==0),]
ratio_typeI_best <- head(rownames(ratio_typeI)[!(rownames(ratio_typeI) %in% ignorenodes)],1)
ratio_typeI_best <- gsub("_ko","",ratio_typeI_best)

# type II:
ratio_typeII <- ratio2[with(ratio2, order(
  ratio2[,grep(paste0(outputs[3],"$"),colnames(ratio2),perl = T)],
  ratio2[,grep(paste0(outputs[2],"$"),colnames(ratio2),perl = T)]
)),]

ratio_typeII <- ratio_typeII[which(ratio_typeII$`Apoptosis_phenotype-Apoptosis_type_II`==0),]
ratio_typeII_best <- head(rownames(ratio_typeII)[!(rownames(ratio_typeII) %in% ignorenodes)],1)
ratio_typeII_best <- gsub("_ko","",ratio_typeII_best)

write(c(ratio_typeI_best,ratio_typeII_best),"ko_file.txt",sep = "\n")
