import sys

from Models.computador import Computadores
from ServerCliente.host import *

class UI:
    @staticmethod
    def main() -> None:
        LigarServidor.ligar()

        while servidor_aberto:
            comando = UI.menu()
            UI.comandos(comando)
    
    @staticmethod
    def menu() -> str:
        print("\t------- LISTA DE COMANDOS ------- \n")
        print("\033[1m\033[32m/maquina\033[0m - Ver Informações das Máquinas que Foram Conectadas")
        print("\033[1m\033[32m/remover\033[0m - Remover Informações das Máquinas que Foram Conectadas")
        print("\033[1m\033[32m/sair\033[0m - Fecha o Servidor")
        return input("\n\033[32mInforme o comando:\033[0m ")
    
    def comandos(comandos: str) -> None:
        match comandos:
            case "/maquina":
                maquinas = View.Listar()
                if maquinas:
                    for maquina in maquinas:
                        print(f"\n[{maquina.id}] - {maquina.nome} \n")

                    id = input("\nInforme o N° da máquina que deseja verificar os dados: ")
                    maquina = View.Listar_Id(id)

                    if not maquina:
                        print("\n\033[31mNúmero da Máquina Incorreto!\033[0m \n")
                    else:
                        print(maquina)

                else:
                    print("\n\033[31mNão há informações de Máquinas! Nenhuma Máquina foi Conectada!\033[0m \n")

            case "/remover":
                maquinas = View.Listar()
                if maquinas:
                    for maquina in maquinas:
                        print(f"[{maquina.id}] - {maquina.nome} \n")

                    id = input("\nInforme o N° da máquina que deseja remover os dados do Database: ")
                    maquina = View.Listar_Id(id)

                    if not maquina:
                        print("\n\033[31mNúmero da Máquina Incorreto!\033[0m \n")
                    else:
                        View.Remover(id)

                else:
                    print("\n\033[31mNão há informações de Máquinas! Nenhuma Máquina foi Conectada!\033[0m \n")

            case "/sair":
                global servidor_aberto
                servidor_aberto = False
                print("\n\033[1m\033[32mServidor Fechado!\033[0m \n")
                sys.exit()
            
            case _:
                print("\033[31mComando Informado Inválido!\033[0m \n")

UI.main()
