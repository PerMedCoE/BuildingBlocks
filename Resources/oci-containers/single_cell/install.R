# Directory for installing packages
libpath <- .libPaths()[1]

# Install devtools and load it
install.packages("devtools", dependencies = TRUE, lib = libpath)
library("devtools")

# Install Bioconductor
BiocManager::install(lib = libpath, ask = FALSE)

# Install other packages
install.packages("pacman", dependencies = TRUE, lib = libpath)
install.packages("usethis", dependencies = TRUE, lib = libpath)
install_version("RcppAnnoy", version = "0.0.16", dependencies = TRUE, lib = libpath)
BiocManager::install("BiocNeighbors", lib = libpath, update = FALSE)
install_version("RcppAnnoy", version = "0.0.18", dependencies = TRUE, lib = libpath)
BiocManager::install("SingleR", lib = libpath, update = FALSE)
BiocManager::install("limma", lib = libpath, update = FALSE)
BiocManager::install("SingleCellExperiment", lib = libpath, update = FALSE)

install_version(package = "rsvd", version = package_version("1.0.2"), dependencies = TRUE, lib = libpath)
install_version(package = "Seurat", version = package_version("3.2.3"), dependencies = TRUE, lib = libpath)
install.packages("https://cran.r-project.org/src/contrib/Archive/spatstat/spatstat_1.64-1.tar.gz",
                 repos=NULL, type="source", INSTALL_opts = "--no-lock", dependencies = TRUE, lib = libpath)

install.packages("dplyr", dependencies = TRUE, lib = libpath)
install.packages("Matrix", dependencies = TRUE, lib = libpath)
install.packages("future", dependencies = TRUE, lib = libpath)
install.packages("pheatmap", dependencies = TRUE, lib = libpath)
install.packages("ggplot2", dependencies = TRUE, lib = libpath)
install.packages("optparse", dependencies = TRUE, lib = libpath)
install.packages("hdf5r", dependencies = TRUE, lib = libpath)
