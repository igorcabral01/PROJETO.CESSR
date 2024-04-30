def Listarpratos(Diabeticos):
    with open(Diabeticos, 'r') as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(dado.strip())
