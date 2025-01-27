estoque = []

menu = int(input("Para adicionar um novo produto ao estoque, digite 1.\n"
                 "Para excluir um produto do estoque, digite 2.\n"
                 "Para exibir a lista de produtos no estoque, digite 3.\n"
                 "Para calcular o valor total do estoque, digite 4.\n"
                 "Por favor, insira a opção desejada: "))

if menu == 1:
    estoque.append((input("Por favor, insira o nome do produto: "), float(input("Por favor, insira o preço do produto: ")), int(input("Por favor, insira a quantidade disponível do produto: "))))
    print("Produto adicionado com sucesso. O estoque atual é: ", estoque)
elif menu == 2:
    num = int(input("Por favor, insira o número do produto que deseja excluir: "))
    del estoque[num]
    print("Produto excluído com sucesso. O estoque atual é: ", estoque)
elif menu == 3:
    print("A lista atual de produtos no estoque é: ", estoque)
elif menu == 4:
    print("O valor total do estoque é: ", sum(produto[1]*produto[2] for produto in estoque))
