#Sistema Cadastro/Buscar de Cliente :
# comentário
dados = {}

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ").capitalize()
    endereco = input("Digite seu endereço: ")
    cpf = input("Digite o CPF do cliente: ")
    email=input("Digite seu E-mail: ")
    senha=input("Digite sua senha: ")

    cliente = {
        'nome': nome,
        'endereço': endereco,
        'cpf': cpf,
        'email': email,
        'senha': senha
        
    }

    dados.append(cliente)
    print("Cliente cadastrado com sucesso!\n")


def buscar_cliente_por_email():
    email_busca = input("Digite o E-mail do cliente para busca: ")

    encontrado = False
    for cliente in dados:
        if cliente['email'] == email_busca:
            print("\n===Cliente encontrado===")
            print(f"Nome: {cliente['nome']}")
            print(f"Endereço: {cliente['endereço']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"E-mail: {cliente['email']}")
            encontrado = True
            break

    if not encontrado:
        print("cliente não encontrado.\n")

def menu():
    while True:
        print("=== Sistema de Cadastro ===")
        print("1. Cadastrar novo cliente")
        print("2. Buscar paciente por email")
        print("3. Sair")
        opcao = input("Escolha uma opção (1-3): ")

        if opcao == '1':
            cadastrar_cliente()   
        elif opcao == '2':
            buscar_cliente_por_email()
        elif opcao == '3':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
menu()



#def listar_clientes():
# if not dados:
#         print("⚠️ Nenhum cliente cadastrado.\n")
#         return
#     for cpf, dadoss in dados.items():
#         print(f"CPF: {cpf}")
#         print(f"  Nome: {dadoss['nome']}")
#         print(f"  Email: {dadoss['email']}")
#         print(f"  Endereço: {dadoss['endereço']}\n")