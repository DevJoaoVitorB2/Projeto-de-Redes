import socket
import json
import time
import threading 

from ServerCliente.view import View

class ServidorUDP:
    @staticmethod
    def enviar_conexao(host='0.0.0.0', udp=5000, tcp=7000):
        # Criando o Socket Servidor/UDP
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Ativar envio de Pacotes de Broadcast
        socket_udp.bind((host, udp))

        while True:
            dados = {'ip':host, 'porta':tcp}
            mensagem = json.dumps(dados).encode('utf-8')
            socket_udp.sendto(mensagem, ('<broadcast>', udp)) # Enviar para todos os dispositivos da rede
            time.sleep(30) # Enviar a cada 30 segundos as informações

class ServidorTCP:
    @staticmethod
    def conexoes(host='0.0.0.0', porta=7000):
        # Criando o Socket Servidor/TCP
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_tcp.bind((host, porta)) # Escutar as informações dos Clientes conectados na Porta 7000
        socket_tcp.listen(5) # Permitir no máximo 5 conexões pendentes no servidor

        while True:
            cliente, endereco = socket_tcp.accept() # Aceitar conexão de um cliente no servidor
            dados = json.loads(cliente.recv(1024).decode()) # Tratar os dados a serem guardados
            View.Inserir(dados) # Guardar os dados
            cliente.close() # Fechar conexão

class LigarServidor:
    @staticmethod
    def ligar():
        threading.Thread(target=ServidorUDP.enviar_conexao, daemon=True).start() # Fazer uma threading para o Sevidor UDP e TCP funcionar simultaneamente
        ServidorTCP.conexoes()