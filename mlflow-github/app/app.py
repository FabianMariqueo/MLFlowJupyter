import mlflow
import importlib
from conf.Configuration_manager import Configuration_manager

## Archivo de configuración donde se guarda el modelo y la ruta del archivo pkl del modelo
config = Configuration_manager.load_config()

## Modelo cargado desde un archivo de configuración
modelo = importlib.import_module("repositorio." + config['modelo'])
mlflow_api = importlib.import_module(config['mlflow_api'])

with mlflow.start_run():
    
    conda = config['conda_env']

    ## Guardar el modelo pkl
    mlflow_api.log_model(modelo.get_model(), 'model', conda_env = conda)

    ## Obtener la ruta del pkl donde quedo guardado
    artifact_path = mlflow.get_artifact_uri()
    artifact_path = artifact_path.replace("file://", "")
    print(artifact_path)

    ## Guardar la ruta del modelo pkl en el archivo de configuracion
    config['ruta_modelo_pkl'] = artifact_path + "/model"
    Configuration_manager.save_values(config)

    #f = open("/mlflow/model_path.txt", "w")
    #f.write(artifact_path+"/model")
    #f.write("mlflow models serve -m "+artifact_path+"/model -h 0.0.0.0 -p 1234 -w 1")
    #f.close()
    #os.environ["MLFLOW_ARTIFACT_PATH"] = artifact_path
