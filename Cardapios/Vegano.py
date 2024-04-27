def Listarpratos(Vegano):
    with open(Vegano, 'r') as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(dado.strip())


