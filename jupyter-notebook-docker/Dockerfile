FROM jupyter/scipy-notebook

USER root
RUN mkdir /mlflow/

USER jovyan
RUN conda install --quiet --yes \
    'mlflow' \
    'psycopg2'
