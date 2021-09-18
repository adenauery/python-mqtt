import psutil

ocupacao = psutil.cpu_percent(interval=1)

print (ocupacao)
