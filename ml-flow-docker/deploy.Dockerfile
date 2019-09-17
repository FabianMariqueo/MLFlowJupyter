FROM python

USER root

RUN mkdir /build_scripts
WORKDIR /build_scripts
COPY install_miniconda.sh /build_scripts
RUN ./install_miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"
RUN conda install -c conda-forge scikit-learn=0.21.3 -y
RUN conda install -c conda-forge mlflow -y
RUN conda install -c conda-forge psycopg2 -y

RUN mkdir /mlflow/
WORKDIR /mlflow

COPY deploy.sh /mlflow

CMD mlflow models serve -m /mlflow/$PROJECT_ID/$MODEL_ID/artifacts/model -h 0.0.0.0 -p 1234