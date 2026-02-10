# import json
# pedidos = [] 
# inplementar salvamento da contagem de pedidos em arquivo JSON (futuramente) 


# Sistema
# Carrinho de compra, estoque de produtos, formulário de pedidos
carrinho = {}
dados_do_pedido = {}
endereço = {}

produtos = {
    1: {"nome": "Buquê com 3 Rosas Brancas", "preco": 100.00, "Quantidade": 20},
    2: {"nome": "Buquê com 3 Rosas vermelhas", "preco": 100.0, "Quantidade": 20},
    3: {"nome": "Buquê com 3 Rosas cor de Rosa", "preco": 100.00, "Quantidade": 20},
    4: {"nome": "Buquê Mix de Flores M (colorido)", "preco": 220.00, "Quantidade": 20},
    5: {"nome": "Buquê Paris", "preco": 380.00, "Quantidade": 20}
}

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço do produto (ex: 199.90): "))
        quantidade = int(input("Quantidade em estoque: "))

        # Gerar novo ID automático baseado no maior ID atual
        novo_id = max(produtos.keys(), default=0) + 1

        produtos[novo_id] = {
            "nome": nome,
            "preco": preco,
            "Quantidade": quantidade
        }

        print(f"\nProduto '{nome}' cadastrado com sucesso com ID {novo_id}!")
    except ValueError:
        print("Erro: Entrada inválida. Tente novamente com os dados corretos.")

def editar_produto():
    listar_produtos()
    try:
        id = int(input("\nDigite o ID do produto que deseja editar: "))
        if id in produtos:
            print(f"Editando produto: {produtos[id]['nome']}")
            novo_nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
            novo_preco = input("Novo preço (deixe em branco para manter o atual): ").strip()
            nova_qtd = input("Nova quantidade (deixe em branco para manter a atual): ").strip()

            if novo_nome:
                produtos[id]['nome'] = novo_nome
            if novo_preco:
                produtos[id]['preco'] = float(novo_preco)
            if nova_qtd:
                produtos[id]['Quantidade'] = int(nova_qtd)

            print("Produto atualizado com sucesso.")
        else:
            print("Produto com esse ID não encontrado.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def excluir_produto():
    listar_produtos()
    try:
        id = int(input("\nDigite o ID do produto que deseja excluir: "))
        if id in produtos:
            confirmacao = input(f"Tem certeza que deseja excluir '{produtos[id]['nome']}'? (s/n): ")
            if confirmacao.lower() == 's':
                del produtos[id]
                print("Produto excluído com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Produto com esse ID não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def listar_produtos():
    print("\nProdutos disponíveis:")
    for id, info in produtos.items():
        print(f"{id}: {info['nome']} - R${info['preco']:.2f}")

def adicionar_ao_carrinho():
    listar_produtos()
    try:
        id = int(input("Digite o ID do produto para adicionar: "))
        if id in produtos:
            quantidade = int(input("Quantidade: "))
            if id in carrinho:
                carrinho[id]["quantidade"] += quantidade
            else:
                carrinho[id] = {
                    "nome": produtos[id]["nome"],
                    "preco": produtos[id]["preco"],
                    "quantidade": quantidade
                }
            print(f"\n{quantidade}x {produtos[id]['nome']} adicionado ao carrinho.")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")

def remover_do_carrinho():
    if not carrinho:
        print("\nCarrinho vazio.")
    else:
        ver_carrinho()
        try:
            id = int(input("Digite o ID do produto para remover: ")) 
            if id in carrinho:
                del carrinho[id]
                print("Produto removido do carrinho.")
            else:
                print("Produto não está no carrinho.")
        except ValueError:
            print("Entrada inválida.")

def ver_carrinho():
    print("\nCarrinho atual:")
    if not carrinho:
        print("Carrinho vazio.")
    else: 
        total = 0
        for id, item in carrinho.items():
            subtotal = item["preco"] * item["quantidade"]
            total += subtotal
            print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f} (ID = {id})") # imprimindo id dos produtos
        print(f"Total: R${total:.2f}")

def finalizar_compra():
    ver_carrinho()
    if carrinho:
        dados_do_pedido = formulario_compra() # função de preenchimento de formulário para finalização do pedido
        pedido_confirmado = confirmar_pedido(dados_do_pedido) # ver dados de formulário + carrinho com total
        
        if pedido_confirmado == True:
            # Salvar os dados em arquivo
            salvar_pedido_arquivo(dados_do_pedido)
            print("\n "\
            "\n >> Compra finalizada! Obrigado pela preferência. << ")
            # Zerar carrinho após salvar dados do pedido
            carrinho.clear()
        
        elif pedido_confirmado == "menu":
            menu()
        
        elif pedido_confirmado == False:
            print("PEDIDO CANCELADO!")
            sair()   
    else:
        print("Seu carrinho está vazio.")

def salvar_pedido_arquivo(dados_do_pedido):
    # numero_pedido = pedidos[-1] (implementar futuramente)
    with open("dados\pedidos.txt", 'a', encoding='utf-8') as arquivo:
        # Escrever cabeçalho
        arquivo.write("\n========== DADOS DO PEDIDO ==========\n")
        
        # Escrever dados do cliente
        arquivo.write("\n=== DADOS DO PEDIDO ===\n")
        for chave, valor in dados_do_pedido.items():
            if chave == "Endereço":
                for x, y in dados_do_pedido["Endereço"].items():
                   arquivo.write(f"{x.upper()}: {y}\n")
            else:
                arquivo.write(f"{chave.upper()}: {valor}\n")
        
        # Escrever itens do carrinho
        arquivo.write("\n=== ITENS DO PEDIDO ===\n")

        total = 0
        for chave,valor in carrinho.items():
            subtotal = (valor["quantidade"])*(valor["preco"])
            arquivo.write(f"[ID-{chave}] {valor["nome"]} - {valor["quantidade"]}x R$ {(valor["preco"]):.2f} -- R$ {subtotal:.2f}  \n")
            total += subtotal
        # Escrever total
        arquivo.write(f"\nTOTAL DO PEDIDO: R${total:.2f}\
                      \n\n{"#"*55}\n\n")
    print(f"\nPedido salvo!")        


def formulario_compra():
    print("\nPara finalizar sua compra forneça as informações a seguir: \n")
    dados_do_pedido = {"Comprador":"", "CPF":"", "E-mail":""}

    # Dados do comprador
    for campo in dados_do_pedido:
        dados_do_pedido[campo] = pedir(campo)
    

    endereco = {"CEP":"", "Logradouro":"", "Número":"", "Complemento":"", "Cidade":""}
    
    for campo in endereco:
        endereco[campo] = pedir(campo)
    print(endereco)        
    
    dados_do_pedido["Endereço"] = endereco

    # Dados da compra
    while True:
        try:
            forma_pagamento = input("Escolha uma forma de pagamento:\n 1 - Crédito\n 2 - Débito\n 3 - Pix\n ").strip()
            if forma_pagamento == "1":
                dados_do_pedido["Forma de pagamento"] = "crédito"
            elif forma_pagamento == "2":
                dados_do_pedido["Forma de pagamento"] = "débito"
            elif forma_pagamento == "3":
                dados_do_pedido["Forma de pagamento"] = "pix"
            else:
                raise ValueError("Opção inválida!")
            break

        except ValueError as e:
                print(f"Erro: {e}")
                continue           
                
    while True:
        try:
            entrega = input("Escolha uma forma de entrega:\n 1 - Retirar na loja\n 2 - Receber em casa\n ").strip()
            if entrega == "1":
                dados_do_pedido["Entrega"] = "retirar na loja"
            elif entrega == "2":
                dados_do_pedido["Entrega"] = "receber em casa" #adicionar taxa de entrega
                #calcular_entrega()
            else:
                raise ValueError("Opção inválida!")
            break

        except ValueError as e:
                print(f"Erro: {e}")
                continue
    # Fim da função
    return dados_do_pedido

def pedir(campo_pedido):
    while True:
        try:
            resposta = input(f"{campo_pedido}: ").strip()
            if input_vazio(resposta) == False:
                break 
            else:
                raise ValueError(f"Campo obrigatório não preenchido!!")
        except ValueError as e:
            print(f"Erro: {e}")
            continue
    return resposta 
                
def input_vazio(resposta):
    if resposta == "":
        return True
    else:
        return False

def confirmar_pedido(dados_do_pedido):
    print("\n Confirme as informações a seguir para finalizar seu pedido"
    "\n >> Dados do pedido <<")
    for c,v in dados_do_pedido.items():
        print(f"{c} - {v}")
    ver_carrinho()
    confirmacao = input("\nConfirmar pedido(S/N): "
    "\n sim - confirmar"
    "\n não - cancelar pedido e encerrrar programa"
    "\n voltar - voltar ao menu\n ")
    if confirmacao.lower() == "sim":
        return True
    elif confirmacao.lower() == "não" or confirmacao.lower() == "nao":
        return False
    elif confirmacao.lower() == "voltar":
        dados_do_pedido.clear()
        return "menu"
    else: #aprimorar
        print("Resposta não identificada, tente novamente!")
        confirmar_pedido()

def sair():
    print("Encerrando o sistema. Até logo!")
    exit()

def menu(): # escolher usuário antes de dar opções (comprador(opções 1, 2, 3, 4, 5, 9), funcionário (opções 1, 6, 7, 8, 9) )
    while True:
        print("\n--- Menu ---")
        print("1. Listar produtos")
        print("2. Adicionar ao carrinho")
        print("3. Remover do carrinho")
        print("4. Ver carrinho")
        print("5. Finalizar compra")
        print("6. Cadastrar novo produto (somente pessoas autorizadas)") # add ver com quantidades atualizadas em estoque
        print("7. Editar produto (somente pessoas autorizadas)")     
        print("8. Excluir produto (somente pessoas autorizadas)")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            remover_do_carrinho()
        elif opcao == "4":
            ver_carrinho()
        elif opcao == "5":
            finalizar_compra()
        elif opcao == "6":
            cadastrar_produto()
        elif opcao == "7":
            editar_produto()
        elif opcao == "8":
            excluir_produto()
        elif opcao == "9":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

def inicio():
    print("\nSeja bem-vindo à 'The Flower Spot', sua floricultura digital!")
    menu()

# Iniciar o sistema
inicio()

