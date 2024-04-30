
def adicionar_cliente():
    
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu CPF apenas numeros: "))
    with open('clientes.txt', 'a') as arquivo:
        arquivo.write(f"Nome: {nome}\n CPF: {cpf}\n")
    print("Cliente adicionado com sucesso!")

def mostrar_clientes():
    try:
        with open('clientes.txt', 'r') as arquivo:
            print("Clientes cadastrados:")
            for linha in arquivo:
                nome, cpf = linha.strip().split(',')
                print(f"Nome: {nome}, CPF: {cpf}")
    except FileNotFoundError:
        print("Nenhum cliente cadastrado.")


""""
TESTEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""