#!/bin/bash
# https://github.com/rocker-org/rocker-versioned2/blob/master/scripts/install_tidyverse.sh

# Install tidyverse
/rocker_scripts/install_tidyverse.sh

# Install other dependencies
install2.r --error --skipinstalled --deps TRUE \
    dplyr \
    diptest \
    mclust \
    moments \
    pheatmap \
    optparse

# Clean up
rm -rf /tmp/downloaded_packages
