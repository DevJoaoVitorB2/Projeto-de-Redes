import os
import json
from typing import List, Optional

class Admin:
    def __init__(self, id, usuario, senha):
        self.id = id
        self.usuario = usuario
        self.senha = senha

class Admins:
    objetos = []

    @classmethod
    def inserir(cls, obj: Admin) -> None:
        cls.abrir()

        id = 0
        for Admin in cls.objetos:
            if Admin.id > id:
                id = Admin.id
        obj.id = id + 1

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> List[Admin]:
        cls.abrir()

        lista_Admins = cls.objetos

        if len(lista_Admins) == 0:
            return []
        else:
            return lista_Admins

    @classmethod
    def listar_id(cls, id: int) -> Optional[Admin]:
        cls.abrir()

        for Admin in cls.objetos:
            if Admin.id == id:
                return Admin

        return None

    @classmethod
    def excluir(cls, id: int) -> None:
        cls.abrir()
        cls.objetos = [Admin for Admin in cls.objetos if Admin.id != id]
        cls.salvar()

    ############ Outros métodos ############################
    @classmethod
    def abrir(cls) -> None:
        if not os.path.exists("Database/Admins.json"):  # Usar um arquivo JSON
            with open("Database/Admins.json", mode="w") as arquivo:
                json.dump([], arquivo)

        with open("Database/Admins.json", mode="r") as arquivo:  # Lendo o arquivo JSON
            cls.objetos = [Admin(**obj) for obj in json.load(arquivo)]

    @classmethod
    def salvar(cls) -> None:
        with open("Database/Admins.json", mode="w") as arquivo:  # Salvando como JSON
            json.dump([vars(Admin) for Admin in cls.objetos], arquivo)
