import psutil
import paho.mqtt.publish as publish

sensor_cpu = psutil.cpu_percent(interval=1)

comando = '{"id":  "cpu1", "origem":  "adenauer", "descricao":  "ocupacao cpu", "valor": ' + '"' + str(sensor_cpu)
comando2 = comando + '"}' + "'"
print(comando2)

publish.single("pi/dados", comando2, hostname="broker.emqx.io")
