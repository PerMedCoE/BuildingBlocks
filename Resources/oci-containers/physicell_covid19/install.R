# Directory for installing packages
libpath <- .libPaths()[1]

# Install devtools and load it
install.packages("devtools", dependencies = TRUE, lib = libpath)
library("devtools")

# Install required packages using install_version from devtools
install_version("dplyr", dependencies = TRUE, lib = libpath)
install_version("tidyverse", dependencies = TRUE, lib = libpath)
install_version("diptest", dependencies = TRUE, lib = libpath)
install_version("mclust", dependencies = TRUE, lib = libpath)
install_version("moments", dependencies = TRUE, lib = libpath)
install_version("pheatmap", dependencies = TRUE, lib = libpath)
install_version("optparse", dependencies = TRUE, lib = libpath)
