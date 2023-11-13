FROM ubuntu:22.04

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        #"r-base=4.1.2*" \
        #"default-jre=2:1.11*" \
        "python3=3.10.6*" \
        "python3-pip=22.0.2*" && \
    rm -rf /var/lib/apt/lists/* && \
    ln -sf /usr/bin/python3 /usr/bin/python

COPY ./requirements-freeze.txt /opt/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt
