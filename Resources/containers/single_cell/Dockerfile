FROM ubuntu:22.04

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        r-base \
        r-base-dev \
        libhdf5-dev \
        libxml2-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        libfontconfig1-dev \
        libgit2-dev \
        libzmq3-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev && \
    rm -rf /var/lib/apt/lists/*

COPY ./install.R /opt/install.R
RUN Rscript --vanilla /opt/install.R
