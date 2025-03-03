import os
import json
from typing import List

class Computador:
    def __init__(self, id: int, nome: str, ramTotal: float, ramLivre: float, qtdProcessadores: int, armazTotal: float, armazLivre: float, tempProcessador: float) -> None:
        self.id = id
        self.nome = nome
        self.ramTotal = ramTotal
        self.ramLivre = ramLivre
        self.qtdProcessadores = qtdProcessadores
        self.armazTotal = armazTotal
        self.armazLivre = armazLivre
        self.tempProcessador = tempProcessador
    
    def __str__(self):
        return f"[{self.id}]\t{self.nome} \n\tMemória RAM Total: {self.ramTotal}GB \n\tMemória RAM Livre: {self.ramLivre}GB \n\tQuantidade de Processadores: {self.qtdProcessadores} \n\tArmazenamento Total: {self.armazTotal}GB \n\tArmazenamento Livre: {self.armazLivre}GB \n\tTemperatura do Processador: {self.tempProcessador}°C \n"

class Computadores:
    objetos = []

    # Inserir a máquina no Database
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

    # Remover a máquina do Database
    @classmethod
    def remover(cls, id: int) -> None:
        cls.abrir()
        computador = next((c for c in cls.objetos if c.id == int(id)), None)
        if computador:
            cls.objetos.remove(computador)
        cls.salvar()

    # Atualizar os dados da máquina no Database
    @classmethod
    def atualizar(cls, nome: str, obj: Computador) -> None:
        cls.abrir()
        for i, maquina in enumerate(Computadores.listar()):
            if maquina.nome == nome:
                obj.id = maquina.id
                Computadores.objetos[i] = obj
        cls.salvar()

    # Lista de máquinas
    @classmethod
    def listar(cls) -> List[Computador]:
        cls.abrir()
        lista_computadores = cls.objetos
        if len(lista_computadores) == 0:
            return []
        else:
            return lista_computadores

    # Encontrar uma máquina pelo ID
    @classmethod
    def listar_id(cls, id: int) -> Computador:
        cls.abrir()
        for computador in cls.objetos:
            if computador.id == int(id):
                return computador
        return None
    
    # Encontrar uma máquina pelo Nome
    @classmethod
    def listar_nome(cls, nome: str) -> Computador:
        for maquina in cls.listar():
            if maquina.nome == nome:
                return maquina
        return None

    # Carregar os dados do Database
    @classmethod
    def abrir(cls) -> None:
        if not os.path.exists("Database/DadosCliente.json"):  # Usar um arquivo JSON
            with open("Database/DadosCliente.json", mode="w") as arquivo:
                json.dump([], arquivo)
        with open("Database/DadosCliente.json", mode="r") as arquivo:  # Lendo o arquivo JSON
            cls.objetos = [Computador(**obj) for obj in json.load(arquivo)]

    # Salvar os dados do Database
    @classmethod
    def salvar(cls) -> None:
        with open("Database/DadosCliente.json", mode="w") as arquivo:  # Salvando como JSON
            json.dump([vars(computador) for computador in cls.objetos], arquivo)
