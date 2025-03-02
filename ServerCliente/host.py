import socket
import json
import time
import threading
import sys

from ServerCliente.view import View
from Models.computador import Computadores

sair = False # Servidor Aberto/Fechado

class ServidorUDP:
    @staticmethod
    def enviar_conexao(host='0.0.0.0', udp=5000, tcp=7000):
        # Criando o Socket Servidor/UDP
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Ativar envio de Pacotes de Broadcast

        while True:
            global sair
            dados = {'ip':host, 'porta':tcp}
            mensagem = json.dumps(dados).encode('utf-8')
            socket_udp.sendto(mensagem, ('<broadcast>', udp)) # Enviar para todos os dispositivos da rede
            time.sleep(15) # Enviar a cada 30 segundos as informações

            if sair != False:
                socket_udp.close()

class ServidorTCP:
    @staticmethod
    def conexoes(host='0.0.0.0', porta=7000):
        # Criando o Socket Servidor/TCP
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_tcp.bind((host, porta)) # Escutar as informações dos Clientes conectados na Porta 7000
        socket_tcp.listen(5) # Permitir no máximo 5 conexões pendentes no servidor

        while True:
            global sair
            cliente, endereco = socket_tcp.accept() # Aceitar conexão de um cliente no servidor
            dados = json.loads(cliente.recv(1024).decode()) # Tratar os dados a serem guardados
            View.Inserir(dados) # Guardar os dados
            cliente.close() # Fechar conexão

            if sair != False:
                socket_tcp.close()

    def comandos():
        while True:
            global sair
            print("\t------- LISTA DE COMANDOS ------- \n")
            print("\033[1m\033[32m/maquinas\033[0m - Ver Informações das Máquinas que Forma Conectadas")
            print("\033[1m\033[32m/sair\033[0m - Fecha o Servidor")
            comandos = input("\n\033[32mInforme o comando:\033[0m ")

            if comandos == "/maquinas":
                if Computadores.listar() != []:
                    for i in Computadores.listar():
                        print(f"[{i.id}] - {i.nome} \n")

                    id = input("\nInforme o N° da máquina: ")
                    maquina = Computadores.listar_id(id)

                    if maquina == None:
                        print("\n\033[31mNúmero da Máquina Incorreto!\033[0m \n")
                    else:
                        print(maquina)
                else:
                    print("\n\033[31mNão há informações de Máquinas! Nenhuma Máquina foi Conectada!\033[0m \n")
            
            elif comandos == "/sair":
                global sair
                sair = True
                print("\n\033[1m\033[32mServidor Fechado!\033[0m \n")
                sys.exit()


class LigarServidor:
    @staticmethod
    def ligar():
        threading.Thread(target=ServidorUDP.enviar_conexao, daemon=True).start() # Fazer uma threading para o Sevidor UDP e TCP funcionar simultaneamente
        threading.Thread(target=ServidorTCP.conexoes, daemon=True).start() # Fazer uma threading para o Sevidor UDP e TCP funcionar simultaneamente
        ServidorTCP.comandos()