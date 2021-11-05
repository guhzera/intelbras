import iperf3

server = iperf3.Server()
print("Configurando parâmetros do servidor")
server.bind_address = str(input("IP da placa de rede: "))
server.port = int(input("Porta: "))
server.verbose = False

print("IP: ",server.bind_address," PORTA: ",server.port)
print("Servidor Iniciado!")
while True:
	server.run()
	print("Conexao recebida!")