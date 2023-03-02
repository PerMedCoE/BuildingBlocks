FROM ubuntu:22.04

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        "r-base=4.1.2*" \
        "default-jre=2:1.11*" \
        "default-jdk=2:1.11*" \
        "perl=5.34.0*" \
        "python3=3.10.6*" \
        "python3-pip=22.0.2*" \
        "wget=1.21.2*" \
        "unzip=6.0*" && \
    rm -rf /var/lib/apt/lists/* && \
    ln -sf /usr/bin/python3 /usr/bin/python

# ASL 2.0 license
# https://b2drop.bsc.es/index.php/s/SRWPNAkKL73oaRw/download
COPY ./jar/BiNoM.jar /usr/local/jar/BiNoM.jar

# LGPL-3.0 license (is compatibility an issue?)
# https://github.com/auranic/VDAOEngine/raw/master/jar/VDAOEngine.jar
COPY ./jar/VDAOEngine.jar /usr/local/jar/VDAOEngine.jar

ARG MABOSS_VERSION=2.5.2
RUN wget --no-hsts --quiet "https://github.com/sysbio-curie/MaBoSS-env-2.0/releases/download/v${MABOSS_VERSION}/MaBoSS-linux64.zip" && \
    unzip -o MaBoSS-linux64.zip -d /usr/local/bin/ && \
    rm MaBoSS-linux64.zip

COPY ./requirements-freeze.txt /opt/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt
