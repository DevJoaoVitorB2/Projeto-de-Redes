import os
import json
from typing import List, Optional

class Computador:
    def __init__(self, id: int, nome: str, ramTotal: float, ramLivre: float, qtdProcessadores: int, armazTotal: float, armazLivre: float) -> None:
        self.id = id
        self.nome = nome
        self.ramTotal = ramTotal
        self.ramLivre = ramLivre
        self.qtdProcessadores = qtdProcessadores
        self.armazTotal = armazTotal
        self.armazLivre = armazLivre

class Computadores:
    objetos = []

    @classmethod
    def inserir(cls, obj: Computador) -> None:
        cls.abrir()

        id = 0
        for computador in cls.objetos:
            if computador.id > id:
                id = computador.id
        obj.id = id + 1

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> List[Computador]:
        cls.abrir()

        lista_computadores = cls.objetos

        if len(lista_computadores) == 0:
            return []
        else:
            return lista_computadores

    @classmethod
    def listar_id(cls, id: int) -> Optional[Computador]:
        cls.abrir()

        for computador in cls.objetos:
            if computador.id == id:
                return computador

        return None

    @classmethod
    def excluir(cls, id: int) -> None:
        cls.abrir()
        cls.objetos = [computador for computador in cls.objetos if computador.id != id]
        cls.salvar()

    ############ Outros métodos ############################
    @classmethod
    def abrir(cls) -> None:
        if not os.path.exists("Database/DadosCliente.json"):  # Usar um arquivo JSON
            with open("Database/DadosCliente.json", mode="w") as arquivo:
                json.dump([], arquivo)

        with open("Database/DadosCliente.json", mode="r") as arquivo:  # Lendo o arquivo JSON
            cls.objetos = [Computador(**obj) for obj in json.load(arquivo)]

    @classmethod
    def salvar(cls) -> None:
        with open("Database/DadosCliente.json", mode="w") as arquivo:  # Salvando como JSON
            json.dump([vars(computador) for computador in cls.objetos], arquivo)
