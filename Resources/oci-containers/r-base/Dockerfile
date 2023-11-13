FROM ubuntu:22.04

ENV LC_ALL=C
ENV R_LIBS="/usr/local/lib/R/site-library:/usr/lib/R/site-library:/usr/lib/R/library"

ARG R_BASE_VERSION=4.1.2
RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        "r-base=${R_BASE_VERSION}*" \
        "r-base-dev=${R_BASE_VERSION}*" \
        "r-base-core=${R_BASE_VERSION}*" \
        "r-recommended=${R_BASE_VERSION}*" \
        "libhdf5-dev=1.10.*" \
        "libxml2-dev=2.9.*" \
        "libgit2-dev=1.1.*" \
        "libssl-dev=3.0.*" \
        "libcurl4-openssl-dev=7.81.*" \
        "libpng-dev=1.6.*" && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/downloaded_packages/ /tmp/*.rds

