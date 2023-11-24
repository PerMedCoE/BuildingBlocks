FROM rocker/r-ver:4.3.2

RUN /rocker_scripts/install_tidyverse.sh
COPY ./install.R /opt/install.R
RUN Rscript /opt/install.R && \
    rm -rf /tmp/downloaded_packages

COPY ./scripts/tf_enrichment.R /opt/tf_enrichment.R
COPY ./scripts/progeny.R /opt/progeny.R
COPY ./scripts/preprocess.R /opt/preprocess.R
COPY ./scripts/export.R /opt/export.R
COPY ./scripts/normalize.R /opt/normalize.R
COPY ./scripts/omnipath.R /opt/omnipath.R
COPY ./scripts/export_carnival.R /opt/export_carnival.R
COPY ./scripts/carnivalr.R /opt/carnivalr.R

COPY ./scripts/tf_enrichment.R /usr/local/bin/tf_enrichment
COPY ./scripts/progeny.R /usr/local/bin/progeny
COPY ./scripts/preprocess.R /usr/local/bin/preprocess
COPY ./scripts/export.R /usr/local/bin/export
COPY ./scripts/normalize.R /usr/local/bin/normalize
COPY ./scripts/omnipath.R /usr/local/bin/omnipath
COPY ./scripts/export_carnival.R /usr/local/bin/export_carnival
COPY ./scripts/carnivalr.R /usr/local/bin/carnivalr
RUN chmod +x /usr/local/bin/*
