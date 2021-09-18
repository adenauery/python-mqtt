import paho.mqtt.client as mqtt
import json
import socket
import time
import psycopg2
from datetime import datetime, timezone
import datetime

# Retorno quando um cliente recebe um  CONNACK do Broker, confirmando a subscricao
def on_connect(client, userdata, flags, rc):
    print("Conectado, com o seguinte retorno do Broker: "+str(rc))

# O subscribe fica no on_connect pois, caso perca a conexão ele a renova
# Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("pi/dados")

# Callback responsavel por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
      print(msg.topic+" "+str(msg.payload))

      dados_python = json.loads(msg.payload)
      metrica = dados_python['id']
      sensor = dados_python['valor']
      data_e_hora_atuais = datetime.datetime.now()
      data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
      print (data_e_hora_em_texto)

      con = psycopg2.connect(host='localhost', database='postgres', user='projeto', password='!int7@')
      cur = con.cursor()
      dt = datetime.datetime.now(timezone.utc)
      insertline = """INSERT INTO adenauer (sensor_id,  sensor_value, pub_date, pub_time) VALUES (%s, %s, %s, %s);"""

      w_sensor_id = metrica
      w_sensor_value = sensor
      w_pub_date = data_e_hora_em_texto
      w_pub_time = datetime.datetime.now().timestamp()

      values = (w_sensor_id, w_sensor_value, w_pub_date, w_pub_time)

      cur.execute(insertline, values)

      con.commit()
      con.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Define um usuário e senha para o Broker, se não tem, não use esta linha
#client.username_pw_set("Xxxxx", password="ZZZZzzz")

# Conecta no MQTT Broker
client.connect("broker.emqx.io", 1883)

# Inicia o loop
client.loop_forever()
