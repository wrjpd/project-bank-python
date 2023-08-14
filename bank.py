from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from textwrap import dedent


contas: List[Conta] = []

# Teste
# felicity: Cliente = Cliente(
#     "Felicity Jones", "felicity@gmail.com", "123.456.789.01", "02/09/1987")
# angelina: Cliente = Cliente(
#     "Angelina Jolie", "angelina@gmail.com", "234.567.891-00", "08/07/1978")

# conta: Conta = Conta(felicity)
# conta2: Conta = Conta(angelina)
# contas.extend([conta, conta2])


def main() -> None:
    menu()


def menu() -> None:
    option: int = int(input(dedent("""
                ====================================
                =============== ATM ================
                ============ Geek Bank  ============
                ====================================
                        
                Selecione uma opção abaixo:
                1 - Criar conta
                2 - Efetuar saque
                3 - Efetuar depósito
                4 - Efetuar transferência
                5 - Listar contas
                6 - Sair do sistema
                """)))

    match option:
        case 1:
            criar_conta()
        case 2:
            efetuar_saque()
        case 3:
            efetuar_deposito()
        case 4:
            efetuar_transferencia()
        case 5:
            listar_contas()
        case 6:
            print("Volte sempre!")
            exit()
        case _:
            print(dedent("""
            
            ==============
            Opção Inválida
            """))
            sleep(2)
            menu()


def criar_conta() -> None:
    print("Informe os dados do cliente: ")

    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print("==================")
    print("Contas criadas com sucesso.")
    print("Dados da conta: ")
    print("==================")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    conta = checar_conta()
    if conta:
        valor: float = float(input("Informe o valor do saque: "))
        conta.sacar(valor)
        sleep(1)
        menu()
    else:
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    conta = checar_conta()
    if conta:
        valor: float = float(input("Informe o valor do deposito: "))
        conta.depositar(valor)
        sleep(1)
        menu()
    else:
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    conta = checar_conta()
    if conta:
        numero_destino: int = int(input("Informe o número da conta destino: "))
        conta_destino: Conta = buscar_conta_por_numero(numero_destino)
        if conta_destino:
            valor: float = float(input("Informe o valor da transferencia: "))
            conta.transferir(conta_destino, valor)
            sleep(1)
            menu()
        else:
            print(
                f"A conta destino com número {numero_destino} não foi encontrada")
        sleep(2)
        menu()
    else:
        sleep(2)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de contas")

        for conta in contas:
            print(conta)
            print("===================")
            sleep(1)
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    match_conta: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                match_conta = conta
    return match_conta


def checar_conta():
    if len(contas) > 0:
        numero_conta: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero_conta)

        if conta:
            return conta
        print(f"Não foi encontrada a conta com número {numero_conta}")
        return None

    print("Ainda não existem contas cadastradas.")
    return None


if __name__ == "__main__":
    main()
