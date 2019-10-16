FROM python

USER root

RUN mkdir /build_scripts
WORKDIR /build_scripts
COPY install_miniconda.sh /build_scripts
RUN ./install_miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"
RUN conda install -c anaconda scikit-learn
RUN conda install -c conda-forge mlflow
RUN conda install -c anaconda psycopg2

RUN mkdir /mlflow/
WORKDIR /mlflow
    
#CMD mlflow run https://github.com/FabianMariqueo/wine-quality-mlflow.git
#CMD mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=0.5

#RUN eval $( cat /mlflow/mlflow_run.txt)
#CMD mlflow models serve -m $MLFLOW_ARTIFACT_PATH/model -h 0.0.0.0 -p 1234
#CMD mlflow models serve -m /mlflow/$PROJECT_ID/$MODEL_ID/artifacts/model -h 0.0.0.0 -p 1234

