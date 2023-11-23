# ubuntu:22.04
FROM rocker/r-ver:4.3.2

COPY ./install.sh /opt/install.sh
RUN /opt/install.sh

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
        python3 \
        python3-dev \
        python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    ln -sf /usr/bin/python3 /usr/bin/python

ARG MABOSS_VERSION=2.5.2
RUN wget --no-hsts --quiet "https://github.com/sysbio-curie/MaBoSS-env-2.0/releases/download/v${MABOSS_VERSION}/MaBoSS-linux64.zip" && \
    unzip -o MaBoSS-linux64.zip -d /usr/local/bin/ && \
    rm MaBoSS-linux64.zip

RUN git clone --branch v6 --single-branch https://github.com/vincent-noel/COVID19.git /usr/local/src/covid19 && \
    rm -rf /usr/local/src/covid19/.git && \
    (cd /usr/local/src/covid19/PhysiCell && make ;) && \
    ln -sf /usr/local/src/covid19/PhysiCell/COVID19 /usr/local/bin/COVID19
    
RUN pip install pandas numpy scipy matplotlib seaborn
