import os
import time


def inicio():
    print("Seja Bem Vindo a Cesar Bistro")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def AcessarMenu():
    limpar_tela()
    inicio()

    print('Cardápios Disponíveis')
    print('''
    1 Portugues
    2 Ingles
  
    ''')
    try:
        acesso = int(input('Digite Qual Cardápio Deseja Acessar: '))
       
    except ValueError:
        print('Por favor, digite um número válido.')
        time.sleep(2)
        limpar_tela()
        AcessarMenu()


AcessarMenu()