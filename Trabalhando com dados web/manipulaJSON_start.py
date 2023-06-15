# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def ManipulaJson():
  endereco = "https://www.sciencebase.gov/catalog/item/5a01f6d0e4b0531197b72cfe?format=json"
  webURL = urllib.request.urlopen(endereco)
  if (webURL.getcode() == 200):
    dados = webURL.read()
    oJSON = json.loads(dados)
    
    contagem = oJSON["metadata"]["count"]
    print ("Contagem: " + str(contagem))
    
    for local in oJSON["features"]:
      if local["properties"]["place"] == "190km ENE of Olonkinbyen, Svalbard and Jan Mayen":
        print("****** Encontrado Registro especial ****** ")
      else:
        print(local["properties"]["place"])
      
ManipulaJson()