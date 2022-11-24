import json
import time

import pandas as pd
import requests

URL = "http://localhost:8080/lead"

contacts = pd.read_csv("contacts.csv", index_col=False)
result = []
result.append(['phone','note'])
phones = (contacts['phone'].to_numpy()).tolist()
for i in phones:

    body = {
        "phone":"57{}".format(i),
        "message":"""
Hola👋

Somos TECLOGI CARGO:

Necesitamos:
Patinetas de Buenaventura a Bogotá
Flete: 3.400.000.
Anticipo 70%
Saldo se paga de contado

Si estás en Cali o Medellín te pagamos 500.000 adicional para que te desplaces a cargar en Buenaventura.

Contáctanos y asegura tu cupo en esta operación de temporada:

📞 3175136128

📞 3160242164

📞 3212573885

📞 3212884773

Te esperamos.
        """,
    }
    payload = json.dumps(body)

    headers = {
        "Content-Type":"application/json"
    }

    r = requests.post(url=URL, headers=headers, data=payload)

    response = None

    try:
        response = 'id'+ ' :: '+ r.json()['responseExSave']['id']
    except:
        response = 'error'+ ' :: '+ r.json()['responseExSave']['error']
    
    result.append([i,response])
    print(response)
    time.sleep(1)

dfResult = pd.DataFrame(result)
dfResult.reset_index(drop=True)
dfResult.to_csv('result.csv', index=False)