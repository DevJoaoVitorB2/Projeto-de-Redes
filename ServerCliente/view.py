import socket
import psutil
import json

from typing import List

from Models.computador import Computador, Computadores

class View:
    @staticmethod
    def ExtrairDados() -> json:
        # Extrair dados da maquina do Cliente
        dados_computador = {
            "id": 0,
            "nome": socket.gethostname(),
            "ramTotal": round(psutil.virtual_memory().total / (1024 ** 3), 2),
            "ramLivre": round(psutil.virtual_memory().available / (1024 ** 3), 2),
            "qtdProcessadores": psutil.cpu_count(logical=True),
            "armazTotal": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
            "armazLivre": round(psutil.disk_usage('/').free / (1024 ** 3), 2),
            "tempProcessador": 0
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
            armazLivre=dados['armazLivre'],
            tempProcessador=dados['tempProcessador']
        )

        Computadores.inserir(computador)
    
    def Remover(id: int) -> None:
        Computadores.remover(id)

    def Atualizar(maquina_nome: str, dados) -> None:
        computador = Computador(
            id=0,
            nome=dados['nome'],
            ramTotal=dados['ramTotal'],
            ramLivre=dados['ramLivre'],
            qtdProcessadores=dados['qtdProcessadores'],
            armazTotal=dados['armazTotal'],
            armazLivre=dados['armazLivre'],
            tempProcessador=dados['tempProcessador']
        )
        
        Computadores.atualizar(maquina_nome, computador)
    
    def Listar() -> List[Computador]:
        return Computadores.listar()
    
    def Listar_Id(id: int) -> Computador:
        return Computadores.listar_id(id)

    def Listar_Nome(maquina_nome: str) -> Computador:
        return Computadores.listar_nome(maquina_nome)