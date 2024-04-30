import random


def Pagamento():
    print('Escolha Sua Forma De Pagamento abaixo')
    print("""
1 PIX
2 DEBITO
3 CREDITO
        """)
def SelecaoPag():
    Escolha = int(input('Selecione Sua forma de pagamento:'))
    if Escolha == 1:
        print('O pagamento Sera feito no pix?')
        Selecao = input()
        if Selecao == "sim":
            print("Aqui esta a chave PIX {123448ASD/SDAAD-FD0ASDFD*F-DASDFCS}")
        else:
            SelecaoPag()
    elif Escolha == 2:
        print('O pagamento Sera feito no Debito?')
        Selecao = "Sim"
        if Selecao == "sim":
            print("Insira o Cartao")
        else:
            SelecaoPag()
    elif Escolha == 1:
        print('O pagamento Sera feito no Credito?')
        Selecao = "Sim"
        if Selecao == "sim":
            print("Insira o Cartão")
        else:
            SelecaoPag()
    else:
        print('Forma de Pagamento Invalida')
        SelecaoPag()
    
    
    