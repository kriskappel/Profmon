import socket

HOST = '192.168.0.10'   # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está

# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

#-------------- Iniciando a conexão com o servidor -------------
mensagem_inicio_conexao = 'Mensagem recebida'
tcp.send(mensagem_inicio_conexao.encode())

tcp.close()