import iperf3
import json 
from subprocess import Popen, PIPE, STDOUT

def get_ping_time_average(host):

    ping = Popen(["ping", "-c", "5", host], stdout = PIPE,stderr = STDOUT)
    output = ping.communicate()[0].decode("utf-8").split("=")
    output = output[len(output)-1]
    output = output.split("/")
    average = output[1]
    return average
        
print("Configurando parâmetros para teste!")
client = iperf3.Client()
client.duration = int(input("Duração do teste em segundos: "))
client.server_hostname = str(input("IP do servidor: "))
client.port = int(input("Porta: "))
print("IP: ",client.server_hostname,"PORTA: ",client.port)
print("Iniciando teste de throughput!")
result = client.run()

taxa = round(result.sent_Mbps,2)
print("Througput: ", taxa,"Mbps")

print("Iniciando teste de latência!")
m_ping = get_ping_time_average("127.0.0.1")
print("Latência: ", m_ping, "ms")
dic = {}
dic["throughput"] = taxa
dic["latencia"] = m_ping

with open("resultados.json", "rb") as file:
    resultados = file.read()

resultados = json.loads(resultados)
lista = resultados["resultados"]
lista.append(dic)
resultados["resultados"] = lista

with open("resultados.json", "w") as file:
    file.write(json.dumps(resultados))