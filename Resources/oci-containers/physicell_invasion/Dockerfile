FROM ubuntu:22.04

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends \
        ca-certificates \
        build-essential \
        flex \
        bison \
        git \
        gcc \
        g++ \
        make \
        wget \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements-freeze.txt /opt/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/requirements.txt

RUN git clone https://github.com/sysbio-curie/Invasion_model_PhysiBoSS.git /usr/local/src/Invasion_model_PhysiBoSS && \
    rm -rf /usr/local/src/Invasion_model_PhysiBoSS/.git && \
    (cd /usr/local/src/Invasion_model_PhysiBoSS/src && make ;) && \
    cp /usr/local/src/Invasion_model_PhysiBoSS/src/myproj /usr/local/src/Invasion_model_PhysiBoSS/bin/myproj && \
    ln -sf /usr/local/src/Invasion_model_PhysiBoSS/bin/myproj /usr/local/bin/myproj && \
    sed -i "s/<folder>./<folder>output/g" /usr/local/src/Invasion_model_PhysiBoSS/data/PhysiCell_settings_2D.xml
