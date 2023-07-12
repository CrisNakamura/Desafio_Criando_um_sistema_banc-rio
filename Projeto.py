import textwrap

def menu():
    menu = '''
============= MENU =============
Digite a operação desejada:
[1] Depósito
[2] Saque
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo usuário
[0] Sair
================================
-> '''
    return input(textwrap.dedent(menu))
    
def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
        print(f'Valor depositado: R$ {valor:.2f}\tSaldo atual: R$ {saldo:.2f}')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Não foi possível realizar o saque! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Não foi possível realizar o saque! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Não foi possível realizar o saque! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")
        print(f'Valor sacado: R$ {valor:.2f}\tSaldo atual: R$ {saldo:.2f}')


    else:
        print("Não foi possível realizar o saque! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("Usuário existente!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade - UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não localizado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular da conta:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        op = menu()

        if op == '1':
            valor = float(input('Digite o valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif op == '2':
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif op == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif op == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif op == '5':
            listar_contas(contas)
        
        elif op == '6':
            criar_usuario(usuarios)
                
        elif op == '0':
            print('Obrigado por utilizar nosso sistema! Volte sempre!')
            break
        
        else:
            print('Operação inválida! Selecione novamente a operação desejada!')

main()