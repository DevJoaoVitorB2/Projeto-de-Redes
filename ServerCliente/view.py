import socket
import psutil
import json

from Models.computador import Computador, Computadores

class View:
    @staticmethod
    def ExtrairDados() -> json:
        # Extrair dados da maquina do Cliente
        dados_computador = {
            "nome": socket.gethostname(),
            "ramTotal": round(psutil.virtual_memory().total / (1024 ** 3), 2),
            "ramLivre": round(psutil.virtual_memory().available / (1024 ** 3), 2),
            "qtdProcessadores": psutil.cpu_count(logical=True),
            "armazTotal": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
            "armazLivre": round(psutil.disk_usage('/').free / (1024 ** 3), 2)
        }

        dados_json = json.dumps(dados_computador)

        return dados_json

    @staticmethod
    def Inserir(dados) -> None:
        computador = Computador(
            id=0,
            nome=dados['nome'],
            ramTotal=dados['ramTotal'],
            ramLivre=dados['ramLivre'],
            qtdProcessadores=dados['qtdProcessadores'],
            armazTotal=dados['armazTotal'],
            armazLivre=dados['armazLivre']
        )

        Computadores.inserir(computador)