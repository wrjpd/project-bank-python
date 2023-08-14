from models.cliente import Cliente


class Conta:
    codigo: int = 1001  # Id da conta

    def __init__(self, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self) -> float:
        return self.__saldo + self.__limite

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo = self.__saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print("Depósito efetuado com sucesso")
        else:
            print("Erro ao efetuar o depósito. Tente novamente")

    def sacar(self, valor: float) -> None:
        if valor > 0 and self.__saldo >= valor:
            self.__saldo = self.__saldo - valor
            self.saldo_total = self._calcula_saldo_total
            print("Saque efetuado com sucesso")
        else:
            print("Saque não realizado. Tente novamente")

    def transferir(self, destino: object, valor: float) -> None:
        if valor > 0 and self.saldo >= valor:
            self.__saldo = self.__saldo - valor
            self.saldo_total = self._calcula_saldo_total
            destino.saldo = destino.saldo + valor
            destino.saldo_total = destino._calcula_saldo_total

            print('Transferência realizada com sucesso.')
        else:
            print('Transferência não realizada. Tente novamente')

    def __str__(self) -> str:
        return f"Número da conta: {self.__numero} \nCliente: {self.cliente.nome} \nSaldo Total: {self.__saldo_total} \nSaldo: {self.__saldo} \nLimite: {self.__limite}"
