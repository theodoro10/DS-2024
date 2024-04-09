from click import clear

def listar_pessoas():
    nome = input('Digite nome da pessoa: ')
    email = input('Digite e-mail da pessoa: ')

    with open('pessoa.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}\n')

    print("Pessoa cadastrada com sucesso!!!")
    for linha in arquivo:
        nome, email = linha.strip().split(',')
        print(f'Nome: {nome},E-mail: {email}\n')


#adicionar_pessoa()
#listar_pessoas()

def listar():
    with open('pessoa.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, email = linha.strip().split(',')
            print(f'Nome: {nome},E-mail: {email}')
listar()