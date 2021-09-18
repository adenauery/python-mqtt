import os
import psutil

sensor_cpu = psutil.cpu_percent(interval=1)

comando = "mosquitto_pub -h broker.emqx.io -t pi/dados  -m " + "'" + '{"id":  "cpu1", "origem":  "adenauer", "descricao":  "ocupacao cpu", "Valor": ' + '"' + str(sensor_cpu)
comando2 = comando + '"}' + "'"
#print(comando2)
os.system(comando2)
