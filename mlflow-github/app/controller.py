from services.Meteored_service import MeteoredService
from conf.Configuration_manager import Configuration_manager
import pickle
import json

conf = Configuration_manager.load_config()
meteoredService = MeteoredService()
meteored_data = meteoredService.get_data()

path_model = conf["ruta_modelo_pkl"] + "/model.pkl"
loaded_model = pickle.load(open(path_model, 'rb'))

prediccion = loaded_model.predict(meteored_data['data'])

json_prediccion = []

if len(prediccion) == len(meteored_data["horas"]):
    print("No problem!!")
    for i in range(len(prediccion)):
        json_prediccion.append({
            "fecha": meteored_data["horas"][i],
            "valor":prediccion[i]
        })
    
    with open('prediccion.json', 'w') as outfile:
        json.dump(json_prediccion, outfile)

#print(meteored_data)
#print(conf["ruta_modelo_pkl"])