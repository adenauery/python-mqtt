## Projeto-Integrador-IV-A

### Segundo Encontro - 18/09/2021

#### URL Base MQTT e dados para teste
* mosquitto_sub -h broker.emqx.io -t pi/dados
  * Broker MQTT utilizado: broker.emqx.io
  * Tópico empregado: pi/dados
  * Dados postados por origem: adenauer 24 h x 7:
    * Temp1: sensor exposto a radiação solar a cada 10 minutos
    * Temp2: sensor na sombra a cada 10 minutos
    * cpu1: ocupação da CPU do servidor a cada 10 minutos
    * dolar: cotação do dolar a cada hora cheia (vide o programa **publica-moedas-mqtt.py**)

#### Instalando o Postgresql & PHPpgadmin
* [TechExpert](https://techexpert.tips/pt-br/postgresql-pt-br/instalar-phppgadmin-no-ubuntu-linux/)
* [Bóson](http://www.bosontreinamentos.com.br/postgresql-banco-dados/instalacao-do-postgresql-e-do-phppgadmin-no-linux/)

#### Python & Postgres
  * [Python & PostGres](https://www.devmedia.com.br/como-criar-uma-conexao-em-postgresql-com-python/34079)
  * [Manipulando dados em PostgreSQL com Python](https://dadosaocubo.com/manipulando-dados-em-postgresql-com-python/)

#### Python & MQTT
  * https://gercil.me/blog/usando-o-pahomqtt-para-python

#### Tutorial sobre o GitHub
  * [Material sobre GitHub da FullCycle](https://fullcycle.com.br/git-e-github/) - [site da FullCycle](https://fullcycle.com.br/)

### Primeiro Encontro - 07/08/2021

### Projeto Final

* [Visão Geral do Projeto Final](https://docs.google.com/presentation/d/1WLr_SozYkB1iTrH71zghpa4Tljgqp3P9QaTv15OrLP4/)


#### Sockets TCP & UDP
[Introdução ao Conceito de Sockets](http://olaria.ucpel.edu.br/materiais/lib/exe/fetch.php?media=introducao-sockets.pdf)

#### Conceitos Relacionados à IoT:
* [Slides](http://olaria.ucpel.edu.br/materiais/lib/exe/fetch.php?media=internet_das_coisas.pdf)
* [IoT Comic Book](https://iotcomicbook.org/)
* [Fog & Cloud](http://olaria.ucpel.edu.br/materiais/lib/exe/fetch.php?media=apresentacao-pi-iv.pdf)

#### Plataformas de Nuvem para IoT
* [Relação de Serviços](http://olaria.ucpel.edu.br/materiais/doku.php?id=plataformas_nuvem_iot)

#### Embarcados para IoT
* [System on a Chip ESP32S](http://olaria.ucpel.edu.br/micropython/doku.php?id=esp32) -- [Ofertas Mercado Livre](https://eletronicos.mercadolivre.com.br/componentes/esp32)
* [Sensor de Temperatura DS18b20](https://www.maximintegrated.com/en/products/sensors/DS18B20.html) -- [Ofertas Mercado Livre](https://lista.mercadolivre.com.br/ds18b20#D[A:ds18b20])

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

#### Virtualizando
* [Virtual Box](https://www.virtualbox.org/)
* [Linux Mint](https://linuxmint.com/)

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


#### Instalando os Clientes da Plataforma Mosquitto

* Linux:
  * sudo apt install mosquitto-clients
* MS-Windows:
  * https://www.curtocircuito.com.br/blog/Categoria%20IoT/seguranca-no-mqtt

* Testes feitos com o Broker: broker.emqx.io

* mosquitto_sub -h broker.emqx.io -t pi4

* mosquitto_pub -h broker.emqx.io -t pi4 -m "Primeira Conexao"
* Envio da data:
  * mosquitto_pub -h broker.emqx.io -t pi4 -m "\`(date)\`"


#### Publicando com Script Bash em Broker MQTT
~~~
#!/bin/bash
contador=1
while [ $contador -le 10 ]
do
        mosquitto_pub -h broker.emqx.io -t pi4 -m $contador
        sleep 3
        let contador=contador+1
done
~~~

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

