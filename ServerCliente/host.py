import socket
import json
import time
import threading

from ServerCliente.view import View
from Models.computador import Computadores

porta_udp = 5000 # Porta do Servidor UDP
porta_tcp = 7000 # Porta do Servidor TCP

servidor_aberto = True # Definir que o Servidor está Aberto

class ServidorUDP:
    @staticmethod
    def enviar_conexao(host='0.0.0.0', udp=porta_udp, tcp=porta_tcp):
        # Socket Servidor UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_udp:
            socket_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Ativar envio de Pacotes de Broadcast

            while servidor_aberto:
                dados = {'ip':host, 'porta':tcp}
                mensagem = json.dumps(dados).encode('utf-8')
                socket_udp.sendto(mensagem, ('<broadcast>', udp)) # Enviar para todos os dispositivos da rede
                time.sleep(15) # Enviar a cada 15 segundos as informações

class ServidorTCP:
    @staticmethod
    def conexoes(host='0.0.0.0', porta=porta_tcp):
        # Socket Servidor TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
            socket_tcp.bind((host, porta)) # Escutar as informações dos Clientes conectados na Porta 7000
            socket_tcp.listen(5) # Permitir no máximo 5 conexões pendentes no servidor

            while servidor_aberto:
                cliente, endereco = socket_tcp.accept() # Aceitar conexão de um cliente no servidor
                dados = json.loads(cliente.recv(1024).decode()) # Tratar os dados a serem guardados

                # Adicionar ao Database os dados da máquina do Cliente
                maquina_nome = dados['nome'] # Pegar o nome da máquina do Cliente
                maquina_existente = View.Listar_Nome(maquina_nome) # Verificar a existência dela no Database

                if maquina_existente:
                    View.Atualizar(maquina_nome, dados) # Atualizar se já existir a máquina no Database
                else:
                    View.Inserir(dados) # Inserir se não existir a máquina no Database
                cliente.close() # Fechar conexão com o Cliente

class LigarServidor:
    @staticmethod
    def ligar():
        threading.Thread(target=ServidorUDP.enviar_conexao, daemon=True).start() # Fazer uma threading para o Sevidor UDP e TCP funcionar simultaneamente
        threading.Thread(target=ServidorTCP.conexoes, daemon=True).start() # Fazer uma threading para o Sevidor UDP e TCP funcionar simultaneamente
