import os
import time
import Cardapios.Vegano as Vegano
import Cardapios.Diabeticos as Diabetico
import Pagamento.Pagamento as pagamento
import Clientes.Clientes as Cliente


def inicio():
    print("Seja Bem Vindo a Cesar Bistro")
def AcessarMenu():
    limpar_tela()
    inicio()

    print('Cardápios Disponíveis')
    print('''
    1-Vegano
    2-Sem Glúten
    3-Diabéticos
    4-Geral
    5-Pagamento
    6-Adicionar Cliente
    ''')
    try:
        acesso = int(input('Digite Qual Cardápio Deseja Acessar: '))
        escolhacard(acesso)
    except ValueError:
        print('Por favor, digite um número válido.')
        time.sleep(2)
        limpar_tela()
        AcessarMenu()


def escolhacard(acesso):
    
    if acesso == 1:
        limpar_tela()
        print('CARDAPIO VEGANO')
        Vegano.Listarpratos('Vegano.txt')
        time.sleep(10)
        AcessarMenu()

    elif acesso == 2:
        print('Escolheu o cardápio Sem Glúten.')
     
    elif acesso == 3:
        limpar_tela()
        print('CARDAPIO DE DIABETICOS')
        Diabetico.Listarpratos('Diabeticos.txt')
        time.sleep(10)
        AcessarMenu()

    elif acesso == 4:
        print('Escolheu o cardápio Geral.')

    elif acesso == 5:
        limpar_tela()
        pagamento.Pagamento()
        pagamento.SelecaoPag()
    elif acesso == 6:
        Cliente.adicionar_cliente()
        Cliente.mostrar_clientes()
        
    else:
        print('Digite um Numero Válido')
        time.sleep(2)
        limpar_tela()
        AcessarMenu()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Main():
    AcessarMenu()

if __name__ == "__main__":
    Main()
