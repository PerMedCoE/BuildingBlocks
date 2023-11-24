# Directory for installing packages
libpath <- .libPaths()[1]

# Install devtools and load it
install.packages("devtools", dependencies = TRUE, lib = libpath)
library("devtools")

# Install Bioconductor
BiocManager::install(lib = libpath, ask = FALSE)

# Install required packages using install_version from devtools
install_version("remotes", dependencies = TRUE, lib = libpath)
install_version("igraph", dependencies = TRUE, lib = libpath)
install_version("stringi", dependencies = TRUE, lib = libpath)
#BiocManager::install("tidyverse", lib = libpath, update = FALSE)
BiocManager::install("OmnipathR", lib = libpath, update = FALSE)
BiocManager::install("progeny", lib = libpath, update = FALSE)
BiocManager::install("dorothea", lib = libpath, update = FALSE)
BiocManager::install("decoupleR", lib = libpath, update = FALSE)
BiocManager::install("cosmosR", lib = libpath, update = FALSE)
BiocManager::install("optparse", lib = libpath, update = FALSE)
BiocManager::install("CellNOptR", lib = libpath, update = FALSE)
BiocManager::install("rhdf5", lib = libpath, update = FALSE)
remotes::install_github("saezlab/CARNIVAL", ref="963fbc1db2d038bfeab76abe792416908327c176")
