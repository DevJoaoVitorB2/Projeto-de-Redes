import socket
import json

from ServerCliente.view import View

class Cliente:
    def __init__(self, porta=5000):
        self.porta = porta
        # Criando um Socket Cliente/UDP
        self.socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_udp.bind(('', self.porta))
    
    def procurar_servidor(self):
        while True:
            print("Aguardando Informações do Servidor...")
            dados, endereco = self.socket_udp.recvfrom(1024) # Receber os dados Broadcast

            # Decodificação dos Dados
            servidor_info = json.loads(dados)
            ip = servidor_info['ip']
            porta = servidor_info['porta']

            # Encontrou o Servidor!
            self.socket_udp.close()
            print(f"Conexão com o Servidor Efetuada: \n\t{ip} - {porta}")
            break
        self.conectar(ip, porta)

    def conectar(self, ip, porta):
        # Criar um Socket Cliente/TCP
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_tcp.connect((ip, porta)) # Conectar ao Servidor TCP/IP

        # Enviar os dados da maquina do Cliente e finalizar conexão
        socket_tcp.send(View.ExtrairDados().encode())  
        socket_tcp.close()
