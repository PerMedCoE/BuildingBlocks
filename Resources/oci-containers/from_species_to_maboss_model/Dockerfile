FROM localhost/mambaforge:latest

RUN apt-get --quiet update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes --no-install-recommends "gcc" "unzip" "libc-dev" && \
    rm -rf /var/lib/apt/lists/*

ARG CONDA_ENV=pypath
ENV PATH=/opt/conda/envs/$CONDA_ENV/bin:$PATH

COPY ./env.yml /opt/env.yml
COPY ./scripts/download_database.py /opt/download_database.py

RUN mamba env create --quiet --name "$CONDA_ENV" --file /opt/env.yml && \
    mamba clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete

RUN mkdir -p /opt/FromSpeciesToMaBoSSModel && \
    /opt/conda/envs/"$CONDA_ENV"/bin/python /opt/download_database.py \
       /opt/FromSpeciesToMaBoSSModel/cache /opt/FromSpeciesToMaBoSSModel/pickles
