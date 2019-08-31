FROM python

USER root
#RUN pip install mlflow

#RUN apt install libpq-dev python3-dev

#RUN pip install psycopg2

RUN mkdir /build_scripts
WORKDIR /build_scripts
COPY install_miniconda.sh /build_scripts
RUN ./install_miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"
RUN conda install -c conda-forge scikit-learn -y
RUN conda install -c conda-forge mlflow -y
RUN conda install -c conda-forge psycopg2 -y

RUN mkdir /mlflow/
WORKDIR /mlflow

CMD mlflow server \
    --backend-store-uri postgresql://admin:secret@postgres:5432/mlflow \
    --default-artifact-root file:/mlflow \
    --host 0.0.0.0


