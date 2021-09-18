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
#   print(msg.topic+" "+str(msg.payload))

   try:
      dados_python = json.loads(msg.payload)
      metrica = dados_python['id']
      fonte = dados_python['origem']
      caracterizacao = dados_python['descricao']
      sensor = dados_python['valor']
      data_e_hora_atuais = datetime.now()
      data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
      print (data_e_hora_em_texto)
#      message = metrica + " " + sensor + " " + str(int(time.time())) + "\n"
      message = "id: " + metrica
      print (message)
      message = "origem: " + fonte
      print (message)
      message = "descricao: " + caracterizacao
      print (message)
      message = "valor: " + sensor + "\n"
      print (message)

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
