import os

import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
from datetime import timezone


# Retorno quando um cliente recebe um  CONNACK do Broker, confirmando a subscricao
def on_connect(client, userdata, flags, rc):
    print("Conectado, com o seguinte retorno do Broker: "+str(rc))

# O subscribe fica no on_connect pois, caso perca a conexao ele a renova
# Lembrando que quando usado o #, voce estah falando que tudo que chegar apos a barra do topico, sera recebido
    client.subscribe("pi/dados")

# Callback responsavel por receber uma mensagem publicada no topico acima
def on_message(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))

   try:
      dados_python = json.loads(msg.payload)
      metrica = dados_python['id']
      sensor = float(dados_python['valor'])
      if metrica == "cpu1":
         if sensor >= 40.1:
            comando = "mosquitto_pub -h broker.emqx.io -t pi/alertas  -m 'ocupacao CPU Servidor elevada'" 
            os.system(comando)

   except Exception:
      print("Erro na leitura do JSON via Broker MQTT")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Define um usuario e senha para o Broker, se nao tem, nao use esta linha
#client.username_pw_set("Xxxxxxx", password="ZZZZZ")

# Conecta no MQTT Broker
client.connect("broker.emqx.io", 1883)

# Inicia o loop
client.loop_forever()
