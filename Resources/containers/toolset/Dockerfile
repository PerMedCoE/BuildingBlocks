FROM localhost/r-base:latest

COPY ./install.R /opt/install.R
RUN Rscript --vanilla /opt/install.R

COPY ./scripts/tf_enrichment.R /usr/local/bin/tf_enrichment
COPY ./scripts/progeny.R /usr/local/bin/progeny
COPY ./scripts/preprocess.R /usr/local/bin/preprocess
COPY ./scripts/export.R /usr/local/bin/export
COPY ./scripts/normalize.R /usr/local/bin/normalize
COPY ./scripts/omnipath.R /usr/local/bin/omnipath
COPY ./scripts/export_carnival.R /usr/local/bin/export_carnival
COPY ./scripts/carnivalr.R /usr/local/bin/carnivalr
RUN chmod +x /usr/local/bin/*
