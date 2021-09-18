import os
sensor_cpu = 98.77
comando = "mosquitto_pub -h broker.emqx.io -t pi/dados  -m " + "'" + '{"id":  "cpu1", "origem":  "adenauer", "descricao":  "ocupacao cpu", "Valor": ' + '"' + str(sensor_cpu)
comando2 = comando + '"}' + "'"
print(comando2)
os.system(comando2)
