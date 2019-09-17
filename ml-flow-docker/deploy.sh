model_id="09ee19989e5d4867a5d319d6f8b88c77"
project_id="1"
mlflow models serve -m /mlflow/data/$project_id/$model_id/artifacts/model -h 0.0.0.0 -p 1234