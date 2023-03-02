FROM localhost/r-base_mambaforge:latest

ARG CONDA_ENV=carnivalpy
ENV PATH=/opt/conda/envs/${CONDA_ENV}/bin:${PATH}
ENV LD_LIBRARY_PATH=/opt/env/:${LD_LIBRARY_PATH}

COPY ./env.lock /opt/env.yml
RUN mamba env create --quiet --name "$CONDA_ENV" --file /opt/env.yml && \
    mamba clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete

COPY ./scripts/carnivalpy.sh /opt/carnivalpy.sh
COPY ./scripts/export.R /opt/export.R
COPY ./scripts/feature_merge.py /usr/local/bin/feature_merger
RUN chmod +x /usr/local/bin/feature_merger
