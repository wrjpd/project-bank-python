from datetime import date
from utils.helper import date_para_str, str_para_date


class Cliente:
    contador: int = 101  # Id do cliente

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self) -> str:
        return f"Código: {self.__codigo} \nNome: {self.__nome} \nData de Nascimento: {self.__data_nascimento} \nCadastro: {self.__data_cadastro}"
