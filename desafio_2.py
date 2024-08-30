# Lista de usuários e contas
usuarios = []
contas = []

# Função para cadastrar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return

    # Cria e adiciona o usuário à lista de usuários
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para cadastrar conta corrente
def criar_conta_corrente(cpf_usuario):
    # Verifica se o usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Erro: Usuário não encontrado.")
        return

    # Cria uma nova conta
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

# Função para realizar depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saque:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n======================== EXTRATO ========================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================================")

# Menu principal
def main():
    saldo = 0
    limite = 1800
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        menu = """
        [c] Criar Usuário
        [a] Criar Conta Corrente
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [x] Sair
        => """

        opcao = input(menu)

        if opcao == "c":
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF (somente números): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "a":
            cpf_usuario = input("Informe o CPF do usuário para criar a conta: ")
            criar_conta_corrente(cpf_usuario)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato, 
                limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "x":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
