#!/usr/bin/env Rscript --vanilla
install.packages(c("devtools","BiocManager","remotes","igraph","stringi"), repos='http://cran.us.r-project.org')
BiocManager::install(c("tidyverse","OmnipathR","progeny","dorothea","decoupleR","cosmosR","optparse","CellNOptR","rhdf5"))
remotes::install_github("saezlab/CARNIVAL", ref="963fbc1db2d038bfeab76abe792416908327c176")
