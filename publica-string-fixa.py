# Ensures paho is in PYTHONPATH
# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish

# Publica
publish.single("pi/dados", "Olá Mundo!", hostname="broker.emqx.io")
