import os
import time
import Cardapios.Vegano as Vegano

def inicio():
    print("Seja Bem Vindo a Cesar Bistro")
def AcessarMenu():
    inicio()
      
    print('Cardápios Disponíveis')
    print('''
    1-Vegano
    2-Sem Glúten
    3-Diabéticos
    4-Geral
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

    elif acesso == 2:
        print('Escolheu o cardápio Sem Glúten.')
     
    elif acesso == 3:
        print('Escolheu o cardápio Diabéticos.')

    elif acesso == 4:
        print('Escolheu o cardápio Geral.')

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
