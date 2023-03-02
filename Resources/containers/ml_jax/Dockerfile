FROM localhost/mambaforge:latest

ARG CONDA_ENV=ml_jax
ENV PATH="/opt/conda/envs/$CONDA_ENV/bin:$PATH"

COPY ./env.lock /opt/env.yml
# TODO: nomkl?
RUN mamba env create --quiet --name "$CONDA_ENV" --file /opt/env.yml && \
    mamba clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete

COPY ./scripts/ml.py /opt/ml.py
RUN chmod +x /opt/ml.py && \
    ln -sf /opt/ml.py /usr/local/bin/ml
