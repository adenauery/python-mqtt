## Python & MQTT

#### URL Base MQTT e dados para teste
* mosquitto_sub -h broker.emqx.io -t pi/dados
  * Broker MQTT utilizado: broker.emqx.io
  * Tópico empregado: pi/dados
  * Dados postados por origem: adenauer 24 h x 7:
    * dolar: cotação do dolar a cada hora cheia (vide o programa **publica-moedas-mqtt.py**)

#### Python & MQTT
  * https://gercil.me/blog/usando-o-pahomqtt-para-python


#### Monitorando Informações do Equipamento
[Integrando Bash com Python](http://olaria.ucpel.edu.br/materiais/doku.php?id=integrando-bash-python)
[Exemplo em Bash](http://olaria.ucpel.edu.br/materiais/doku.php?id=script-filtro-informacoes)

#### Conhecendo o Bash de Sistemas Operacionais Posix
* [Sistemas Posix](https://pt.wikipedia.org/wiki/POSIX)
* [Foca Linux](http://www.guiafoca.org/)
* [Ebooks sobre Sistemas Operacionais Posix](https://drive.google.com/drive/folders/0B2INSZz1E5TlVWdkVFM0OUxKXzA)

* Uso do Cron: 
  * [Como utilizar o Cron no agendamento de tarefas](https://www.infowester.com/linuxcron.php)
  * 0-59/2 * * * * date >> exemplo-pi-iv.txt 
  * A cada 2 minutos o comando é executado

#### Transmitindo Informações Sensoriadas do Meio para um Servidor
  * Conceitos
    * [Protocolo MQTT - Material IBM](https://www.ibm.com/developerworks/br/library/iot-mqtt-why-good-for-iot/index.html)
    * [Protocolo MQTT - Material Curto Circuito](https://www.curtocircuito.com.br/blog/introducao-ao-mqtt/)
    * [Slides sobre MQTT - Material UFC](https://pt.slideshare.net/MaurcioMoreiraNeto/protocolo-mqtt-redes-de-computadores)
    * [Comparação MQTT & Outros Protocolos](https://medium.com/internet-das-coisas/iot-05-dando-uma-breve-an%C3%A1lise-no-protocolo-mqtt-e404e977fbb6)
  * Plataformas de Software
    * [Mosquitto da Eclipse Foundation](https://mosquitto.org)
    * [Brokers MQTT gratuitos e pagos para utilizar em projetos da IoT](https://diyprojects.io/8-online-mqtt-brokers-iot-connected-objects-cloud/#.XzfHmEl7nUI)
    * [Explorando o uso de MQTT em Programas Python](https://fazbe.github.io/Usando-o-paho-mqtt-para-Python/)

#### Linguagem Python
* [Aprenda Programar - PythonBrasil](https://wiki.python.org.br/AprendaProgramar)
* [Receitas para manipular arquivos de texto em Python](http://devfuria.com.br/python/receitas-para-manipular-arquivos-de-texto/)

#### Comunicando com um Broker MQTT utilizando Python

##### Instalação do paho-mqtt
  * https://www.eclipse.org/paho/index.php?page=clients/python/index.php

##### Procedimento de Subscrição
~~~
# Cliente Python para subscrever em um Broker MQTT
#
# Para instalar o paho-mqtt use o comando pip install paho-mqtt ou
# apt get install paho-mqtt
# Faca as instalacoes como root
#
import paho.mqtt.client as mqtt

# Retorno quando um cliente recebe um  CONNACK do Broker, confirmando a subscricao
def on_connect(client, userdata, flags, rc):
    print("Conectado, com o seguinte retorno do Broker: "+str(rc))

    # O subscribe fica no on_connect pois, caso perca a conexao ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, sera recebido
    client.subscribe("pi4/#")

# Callback responsavel por receber uma mensagem publicada no topico acima
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
# adicionar comandos para gravar no banco de dados  <<-=-=-=<<

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Define um usuário e senha para o Broker, se não tem, não use esta linha
# client.username_pw_set("USUARIO", password="SENHA")

# Conecta no MQTT Broker
client.connect("broker.emqx.io", 1883, 60)

# Inicia o loop
client.loop_forever()

~~~


##### Procedimento de Publicação
~~~
# Ensures paho is in PYTHONPATH
# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish

# Publica
publish.single("pi4", "Olá Mundo!", hostname="broker.emqx.io")
~~~
###### Publicação com Laço de Repetição
~~~
import paho.mqtt.publish as publish
import time

# Publica

contador = 0
while (contador < 5):
        publish.single("pi4", contador, hostname="broker.emqx.io")
        contador = contador + 1
        time.sleep(2)
~~~

###### Instalação do psutil

  * https://pypi.org/project/psutil/

###### Script em Bash para gerar ocupação de CPU
~~~
while true; do

a=7.15/6.74

done

~~~

