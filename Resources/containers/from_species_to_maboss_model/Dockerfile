FROM localhost/mambaforge:latest

ARG CONDA_ENV=pypath
ENV PATH=/opt/conda/envs/$CONDA_ENV/bin:$PATH

COPY ./env.yml /opt/env.yml
COPY ./scripts/download_database.py /opt/download_database.py

# TODO: Vincent will find working versions for the Python dependencies
# TODO: pin pypath-omnipath version
RUN mamba env create --quiet --name "$CONDA_ENV" --file /opt/env.yml && \
    mamba clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete && \
    mkdir -p /opt/FromSpeciesToMaBoSSModel && \
    /opt/conda/envs/"$CONDA_ENV"/bin/python /opt/download_database.py \
       /opt/FromSpeciesToMaBoSSModel/cache /opt/FromSpeciesToMaBoSSModel/network.pickle

