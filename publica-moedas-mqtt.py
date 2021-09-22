import requests
import json
import paho.mqtt.publish as publish

requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

cotacao = requisicao.json()

#print("#### Cotacao do Dolar ####")
#print ("Moeda: " + cotacao["USD"]["name"])
#print ("Data: " + cotacao["USD"]["create_date"])
#print("Valor atual: R$" + cotacao["USD"]["bid"])

comando = '{"id":  "dolar", "origem":  "adenauer", "descricao": "' 
comando2 = comando + "cotacao em: " + cotacao["USD"]["create_date"] + '", ' + '"valor": ' + '"' + cotacao["USD"]["bid"]
comando3 = comando2 + '"}'
publish.single("pi/dados", comando3, hostname="broker.emqx.io")
