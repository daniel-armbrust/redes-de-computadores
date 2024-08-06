#
# Exemplo de um Servidor TCP no qual pode receber dados
# pela rede.
#

import socket

# Valores que devem ser alterados de acordo com o 
# contexto de execução.
endereco_ip_servidor = '127.0.0.1'
porta_servidor = 8085

# Cria um objeto SOCKET que utliza o protocolo TCP.
servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# "Escuta" por conexões no Endereço IP e Porta especifidados.
servidor_tcp.bind((endereco_ip_servidor, porta_servidor))

# Habilita o Servidor TCP a aceitar no máximo uma (1) conexão. 
servidor_tcp.listen(1)

print(f'Iniciado o Servidor TCP no IP "{endereco_ip_servidor}" e PORTA "{porta_servidor}".')

# Aguarda uma conexão remota (cliente remoto).
conexao_remota, endereco_ip_remoto = servidor_tcp.accept()

print(f'O Endereço IP "{endereco_ip_remoto}" se conectou ao Servidor.')
print('Aguardando o recebimento dos dados...')

while True:
    dados_recebidos = conexao_remota.recv(1024)

    if not dados_recebidos:
        break

    print(f'Dados Recebidos >>>', dados_recebidos.decode())

    conexao_remota.sendall(dados_recebidos)


# Fecha a conexão remota e encerra o Servidor TCP.
conexao_remota.close()
servidor_tcp.close()
