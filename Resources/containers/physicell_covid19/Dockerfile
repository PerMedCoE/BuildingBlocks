FROM ubuntu:22.04

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        build-essential \
        flex \
        bison \
        git \
        gcc \
        g++ \
        make \
        wget \
        unzip \
        r-base \
        r-base-dev \
        libxml2-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        python3 \
        python3-dev && \
    rm -rf /var/lib/apt/lists/* && \
    ln -sf /usr/bin/python3 /usr/bin/python

ARG MABOSS_VERSION=4.2.2
RUN wget --no-hsts --quiet "https://github.com/sysbio-curie/MaBoSS-env-2.0/releases/download/v${MABOSS_VERSION}/MaBoSS-linux64.zip" && \
    unzip -o MaBoSS-linux64.zip -d /usr/local/bin/ && \
    rm MaBoSS-linux64.zip

# TODO: Vincent will lock this version when he has updated the code
RUN git clone https://github.com/vincent-noel/COVID19.git \
        /usr/local/src/covid19 && \
    rm -rf /usr/local/src/covid19/.git && \
    (cd /usr/local/src/covid19/PhysiCell && sed -i 's/COVID19/myproj/g' Makefile && make ;) && \
    ln -sf /usr/local/src/covid19/PhysiCell/myproj /usr/local/bin/myproj

COPY ./install.R /opt/install.R
RUN Rscript --vanilla /opt/install.R
