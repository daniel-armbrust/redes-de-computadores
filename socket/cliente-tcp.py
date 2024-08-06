#
# Exemplo de um Cliente TCP no qual pode enviar dados
# pela rede.
#

import socket

# Valores que devem ser alterados de acordo com o 
# contexto de execução.
endereco_ip_servidor = '127.0.0.1'
porta_servidor = 8085

# Cria um objeto SOCKET que utliza o protocolo TCP.
cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz conexão com o Servidor TCP remoto.
cliente_tcp.connect((endereco_ip_servidor, porta_servidor))

# Armazena a entrada do usuário na variável de nome mensagem.
mensagem = input('Digite a sua mensagem >>> ')

# Envia a mensagem ao servidor usando o protocolo TCP.
cliente_tcp.sendall(mensagem.encode())

# Encerra a conexão cliente TCP.
cliente_tcp.close()