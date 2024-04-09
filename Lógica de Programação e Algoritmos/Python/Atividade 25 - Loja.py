"""""
letra = 's'
while letra == 's':

    produtos = []

    produto = input('Digite o produto que você deseja registrar: ')
    produtos.append(produto)

    valores = []

    valor = float(input('Digite o valor deste produto: '))
    valores.append(valor)

    quantidades = []

    quantidade = int(input('Digite a quantidade: '))
    quantidades.append(quantidade)

    descrições = []

    descrição = input('Digite a descrição do seu produto: ')
    descrições.append(descrição)

    letra = input('Deseja continuar? [s/n]')

    clear()
    opcao = input('Deseja exibir os produtos [sim/nao]')
    if opcao == 'sim':
        print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ')
        for i in range(0, len(nome_produto)):
            print(
                f'{nome_produto[i]} \t\t {valor_produto[i]} \t\t\t {quantidade_produto[i]} \t\t {descricao_produto[i]}')
"""

from click import clear

opcao = 0
nome_produto = []
valor_produto = []
descricao_produto = []
quantidade_produto = []

def adicionar():
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome_produto.append(nome)
    valor_produto.append(valor)
    descricao_produto.append(descricao)
    quantidade_produto.append(quantidade)

    with open('produtos.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{valor}, {descricao}, {quantidade}\n')



def mostrar():
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ')
    for i in range(0, len(nome_produto)):
        print(f'{nome_produto[i]} \t\t\t\t\t {valor_produto[i]} \t\t\t\t {quantidade_produto[i]} \t\t\t\t {descricao_produto[i]}')
    input("pressione ENTER para continuar...")

def excluir():
    opcao = int(input('Qual registro deseja deletar?'))
    nome_produto.pop(opcao)
    valor_produto.pop(opcao)
    descricao_produto.pop(opcao)
    quantidade_produto.pop(opcao)


while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar um produto")
    print("2 - Para mostrar produtos")
    print("3 - Para excluir um produto")
    print("4 - Para sair")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        mostrar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        break

