def menu():
    print("""\nDigite a operação que deseja realizar\n
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Cadastrar usuário
    [5] Cadastrar conta
    [6] Listar contas
    [7] Sair""")
    opcao = int(input("\nOpção: "))

    return opcao

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: {valor:.2f}"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nValor informado é inválido!")

    return saldo, extrato

def sacar(*,valor, saldo, extrato, quantidade_saques, limite_saque, numero_saques):
    excedeu_limite_saque = valor > limite_saque
    excedeu_quantidade_saque = numero_saques >= quantidade_saques
    excedeu_saldo = valor > saldo
        
    if excedeu_quantidade_saque:
        print("Falha na operação! Quantidades de saques excedidos!")

    elif excedeu_limite_saque:
        print("Falha na operação! Valor do saque excedido!")

    elif excedeu_saldo:
        print("Falha na operação! O saldo não é suficiente!")

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque: {valor:.2f}"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nValor informado é inválido!")

    return saldo, extrato

def extrato(saldo, extrato):
    print(f"\n{extrato}")
    print("-"*20)
    print(f"Saldo: {saldo}")

    return 0

def cadastrar_usuario(usuarios):
    cpf = input("CPF do usuário: ")
    existe_usuario = filtrar_usuario(cpf, usuarios)

    if existe_usuario:
        print("\nUsuário já existente!")
        return
    
    nome = input("Nome do usuário: ")
    email = input("E-mail do usuário: ")
    data_nascimento = input("Data de nascimento do usuário(dd/mm/aaaa): ")
    cep = input("CEP do usuário: ")
    
    usuarios.append({"cpf": cpf, "nome": nome, "email": email, "data_nascimento": data_nascimento, "cep": cep})

    print("\nUsuário cadastrado com sucesso!")

def cadastrar_conta(agencia, id_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "id_conta": id_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}, \nID Conta: {conta['id_conta']}, \nUsuário: {conta['usuario']['nome']}")
        print(contas)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = []

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)

    if usuarios_filtrados:
        return usuarios_filtrados[0]
    else:
        return None
    
saldo = 0
limite_saque = 500
QUATIDADE_SAQUES = 3
numero_saques = 0
extrato = ""
usuarios = []
contas = []
AGENCIA = "0001"

while True:

    opcao = menu()
                
    if opcao == 1:
        valor = float(input("\nValor que deseja' depositar: "))

        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == 2:
        valor = float(input("\nValor que deseja sacar: "))

        saldo, extrato = sacar(valor=valor, saldo=saldo, extrato=extrato, quantidade_saques=QUATIDADE_SAQUES, 
                               limite_saque=limite_saque, numero_saques=numero_saques)

    elif opcao == 3:
        extrato(saldo, extrato)

    elif opcao == 4:
        cadastrar_usuario(usuarios)
    
    elif opcao == 5:
        id_conta = len(contas) + 1
        conta = cadastrar_conta(AGENCIA, id_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 7:
        break

    else:
        print("Comando inválido!")
