def entrada():
    print("Olá querido credor(a).")
    print("Seja bem-vindo ao Banco Pyton.")
    print("Vamos iniciar.")
    possui_cadastro = input("Você já possui um cadastro conosco? (responda com sim ou não) ").lower()

    if possui_cadastro == "sim":
        login()
    elif possui_cadastro == "não":
        cadastro()
    else:
        print("Opção inválida. Por favor, responda com sim ou não.")
        entrada()

def login():
    nome_usuario = input("Ficamos felizes que tenha um cadastro conosco. Por gentileza, insira o seu nome registrado: ")
    senha = input("Digite a sua senha, por favor: ")
    
    autenticado, identificador, nome_cliente, saldo = verificar_credenciais(nome_usuario, senha)
    
    if autenticado:
        print("Login bem-sucedido!")
        menu(identificador, nome_cliente, saldo)
    else:
        print("Credenciais inválidas.")
        opcao = input("Deseja fazer um cadastro conosco (1) ou voltar ao menu de entrada (2)? ")
        if opcao == "1":
            cadastro()
        elif opcao == "2":
            entrada()
        else:
            print("Opção inválida.")
            entrada()

def verificar_credenciais(nome_usuario, senha):
    with open("cadastros.txt", "r") as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) == 4:  # Verifica se a linha possui os 4 valores esperados
                identificador, usuario, senha_armazenada, saldo = valores
                if usuario == nome_usuario and senha_armazenada == senha:
                    saldo = float(saldo.replace('$', '').replace(',', ''))  # Remover símbolo de dólar e vírgulas
                    return True, identificador, usuario, saldo
        return False, None, None, None  # Retorna False se as credenciais não forem encontradas

def verificar_credenciais_por_id(identificador):
    with open("cadastros.txt", "r") as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) == 4 and valores[0] == identificador:  # Verifica se a linha possui os 4 valores esperados e se o identificador corresponde
                saldo = float(valores[3].replace('$', '').replace(',', ''))  # Remover símbolo de dólar e vírgulas
                return True, valores[1], valores[2], saldo  # Retorna as credenciais se encontradas
    return False, None, None, None  # Retorna False se o identificador não for encontrado

def menu(identificador, nome_cliente, saldo):
    while True:
        print(f"Seja bem-vindo, cliente {nome_cliente}! Seu Saldo atual é de R${saldo:.2f}.")
        print("1. Consultar saldo")
        print("2. Realizar saque")
        print("3. Realizar depósito")
        print("4. Realizar Transferência de dinheiro")
        print("5. Sair")

        escolha = input("Digite a opção que deseja realizar: ")
        if escolha == "1":
            print(f"Seu saldo atual é R${saldo:.2f}.")
        elif escolha == "2":
            valor_saque = float(input("Digite o valor do saque: "))
            saldo = realizar_saque(saldo, valor_saque, identificador)
            print(f"Saque de R${valor_saque:.2f} realizado. Novo saldo: R${saldo:.2f}.")
        elif escolha == "3":
            valor_deposito = float(input("Digite o valor do depósito: "))
            saldo += valor_deposito
            atualizar_saldo_arquivo(identificador, saldo)
            print(f"Depósito de R${valor_deposito:.2f} realizado. Novo saldo: R${saldo:.2f}.")
        elif escolha == "4":
            realizar_transferencia(identificador)        
        elif escolha == "5":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida.")

def realizar_transferencia(id_remetente):
    id_destinatario = input("Digite o ID do destinatário: ")
    valor_transferencia = float(input("Digite o valor da transferência: "))

    # Verificar se o destinatário existe
    autenticado_destinatario, _, _, _ = verificar_credenciais_por_id(id_destinatario)
    if not autenticado_destinatario:
        print("Destinatário não encontrado.")
        return

    # Verificar saldo do remetente
    _, _, _, saldo_remetente = verificar_credenciais_por_id(id_remetente)
    if saldo_remetente is None or saldo_remetente < valor_transferencia:
        print("Senhor, no momento você não possui esse valor. Por favor, faça uma transferência correspondente ao seu saldo.")
        return

    # Realizar a transferência
    _, _, _, saldo_destinatario = verificar_credenciais_por_id(id_destinatario)
    novo_saldo_remetente = saldo_remetente - valor_transferencia
    novo_saldo_destinatario = saldo_destinatario + valor_transferencia

    atualizar_saldo_arquivo_por_id(id_remetente, novo_saldo_remetente)
    atualizar_saldo_arquivo_por_id(id_destinatario, novo_saldo_destinatario)

    print(f"Transferência de R${valor_transferencia:.2f} para o ID {id_destinatario} realizada com sucesso.")

def realizar_saque(saldo, valor_saque, identificador):
    if valor_saque > saldo:
        print("Saldo insuficiente.")
        return saldo

    novo_saldo = saldo - valor_saque
    atualizar_saldo_arquivo(identificador, novo_saldo)
    return novo_saldo

def atualizar_saldo_arquivo(identificador, novo_saldo):
    with open("cadastros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        identificador_arquivo, usuario, senha_armazenada, saldo = linha.strip().split(',')
        if identificador_arquivo == identificador:
            linhas[i] = f"{identificador},{usuario},{senha_armazenada},{novo_saldo:.2f}\n"
            break

    with open("cadastros.txt", "w") as arquivo:
        arquivo.writelines(linhas)

def atualizar_saldo_arquivo_por_id(identificador, novo_saldo):
    with open("cadastros.txt", "r") as arquivo:
        linhas = arquivo
def atualizar_saldo_arquivo_por_id(identificador, novo_saldo):
    with open("cadastros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        valores = linha.strip().split(',')
        if valores[0] == identificador:
            valores[3] = f"{novo_saldo:.2f}"
            linhas[i] = ','.join(valores) + '\n'
            break

    with open("cadastros.txt", "w") as arquivo:
        arquivo.writelines(linhas)

def cadastro():
    nome_usuario = input("Por favor, insira seu nome: ")
    senha = input("Insira sua senha: ")
    saldo_inicial = float(input("Insira o saldo inicial: "))

    with open("cadastros.txt", "a") as arquivo:
        if not arquivo.tell():
            identificador = 1
        else:
            arquivo.seek(0)
            identificador = max(int(linha.split(',')[0]) for linha in arquivo) + 1
        arquivo.write(f"{identificador},{nome_usuario},{senha},${saldo_inicial:.2f}\n")
    
    print("Cadastro realizado com sucesso!")
    print("Seja bem vindo ao Banco Pyton o banco que não te aperta")
    print("Mas te envenena aos poucos!")

entrada()
