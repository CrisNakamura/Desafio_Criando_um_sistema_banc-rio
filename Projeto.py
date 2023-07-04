saldo_inicial = 1000 # Definindo o saldo inicial.
saldo = saldo_inicial
op = -1
LIMITE_SAQUE = 3 # Definindo o limite de saque.
op_realizada = [] # Criando uma lista onde será armazenado as operações realizadas.

# Iniciando as operações.
while op != 0:
    op = int(input('''
============= MENU =============
Digite a operação desejada:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
================================
-> '''))
    
    # Operação: Depósito
    if op == 1:
        valor_deposito = float(input('Digite o valor do depósito: '))
        saldo += valor_deposito
        print(f'Saldo após efetuar depósito: R$ {saldo:.2f}')
        deposito = f'Depósito: + R$ {valor_deposito:.2f}'
        op_realizada.append(deposito)

    # Operação: Saque
    elif op == 2:
        if LIMITE_SAQUE != 0:
            valor_saque = float(input('Digite o valor do saque: '))

            if valor_saque > 500:
                print('Não foi posspivel realizar o saque! Limite máximo por saque é R$ 500,00!')

            elif saldo >= valor_saque and valor_saque <= 500:
                saldo -= valor_saque
                print(f'Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!')
                print(f'Saldo após efetuar saque: R$ {saldo:.2f}')
                saque = f'Saque: - R$ {valor_saque:.2f}'
                op_realizada.append(saque)
                LIMITE_SAQUE -= 1

            elif saldo < valor_saque:
                 print('Não foi possível realizar o saque! Saldo insuficiente!')
        
        else:
            print('O limite de saque diária foi atingida! Tente novamente amanhã!')       

    # Operação: Extrato
    elif op == 3:
        if op_realizada == []:
            print('Não foram realizadas movimentações.')

        else:
            print('EXTRATO'.center(32,'='))
            print(f'Saldo inicial: R$ {saldo_inicial:.2f}')

            for operacao in range(len(op_realizada)):
                print(op_realizada[operacao])
                
            print(f'Saldo atual: R$ {saldo:.2f}')
            print(''.center(32,'='))


    # Operação: Sair
    elif op == 0:
        print('Obrigado por utilizar nosso sistema! Volte sempre!')
        break

    # Operação inválida
    else:
        print('Operação inválida! Digite novamente!')