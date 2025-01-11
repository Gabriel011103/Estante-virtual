#Estante virtual

estante = {}

while True:
    print ("\n----- menu -----")
    print ("1. Abastecimento livro")
    print ("2. Venda livro")
    print ("3. Remover livro")
    print ("4. Listar Livros")
    print ("5. sair")
    print ("\n-----------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do livro: ")
        quantidade = int(input("Digite a quantidade que você deseja adicionar: "))
        if nome in estante:
            estante[nome] += quantidade
        else:
            estante[nome] = quantidade

    elif opcao == "2":
        nome = input("Digite o nome do livro que você vendeu: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        if nome in estante:
            if estante[nome] >= quantidade:
                estante[nome] -= quantidade
                if estante[nome] == 0:
                    del estante[nome]
                print(f"{quantidade} unidade(s) de {nome} vendida(s).")
            else:
                print("não existe livros suficientes para serem vendidos.")
        else:
            print("O livro não está na estante.")

    elif opcao == "3":
        nome = input("Digite o nome do titulo que deseja remover da sua estante: ")
        if nome in estante:
            del estante[nome]
            print(f"{nome} removido.")
    elif opcao == "4":
        if not estante:
            print("A estante se encontra vazia.")
        else:
            print("Livros na estante: ")
            for livro, quantidade in estante.items():
                print (f"{livro}: {quantidade} unidades")
                
    elif opcao == "5":
        print ("Tchau, caso deseje voltar é só reiniciar o programa !!")
        break

    else:
        print("Opção invalida. Tente novamente")