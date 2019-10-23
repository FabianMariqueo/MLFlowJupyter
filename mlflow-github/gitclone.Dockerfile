FROM python

ARG GIT_TOKEN
ARG URL_GIT

USER root

RUN mkdir /build_scripts
WORKDIR /build_scripts
COPY install_miniconda.sh /build_scripts
RUN ./install_miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"
RUN conda install -c anaconda scikit-learn
RUN conda install -c conda-forge mlflow
RUN conda install -c anaconda psycopg2
RUN conda install -c anaconda flask
RUN conda install -c anaconda flask-cors

RUN mkdir /mlflow/

COPY app/ /mlflow/app/
WORKDIR /mlflow/app

RUN git clone $URL_GIT repositorio