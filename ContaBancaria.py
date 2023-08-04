menu = "\nDigite a operação que deseja realizar\n [1] Depósito\n [2] Saque\n [3] Extrato\n [4] Sair"
saldo = 0
limite_saque = 500
quantidade_saque = 3
extrato = ""

while True:
    print(menu)
    opcao = int(input("Opção: "))
                
    if opcao == 1:
        valor = float(input("\nValor que deseja depositar: "))
        saldo += valor
        extrato += f"\nDepósito: {valor:.2f}"

    elif opcao == 2:
        valor = float(input("\nValor que deseja sacar: "))

        excedeu_limite_saque = valor > limite_saque
        excedeu_quantidade_saque = quantidade_saque <= 0
        excedeu_saldo = valor > saldo
        
        if excedeu_quantidade_saque:
            print("Falha na operação! Quantidades de saques excedidos!")

        elif excedeu_limite_saque:
            print("Falha na operação! Valor do saque excedido!")

        elif excedeu_saldo:
            print("Falha na operação! O saldo não é suficiente!")

        else:
            saldo -= valor
            extrato += f"\nSaque: {valor:.2f}"
            quantidade_saque -= 1

    elif opcao == 3:
        print(f"\n{extrato}")
        print("-"*20)
        print(f"Saldo: {saldo}")

    elif opcao == 4:
        break

    else:
        print("Comando inválido!")
