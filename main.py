def read_file():
    with open("test1.txt", "r") as arquivo:
        dados = arquivo.readlines()
        for i in range(len(dados)):
            dados[i] = dados[i].strip("\n")
        estados = dados[0].split(" ")[1:]
        estadoI = dados[1].split(" ")[1:]
        estadosF = dados[2].split(" ")[1:]
        regras = []
        casosTeste = []
        for arr in dados[3:dados.index('---')]:
            arr = arr.split(" ")
            arr.remove('->')
            arr.remove('|')
            simb: str
            for simb in arr[2:]:
                regras.append(tuple([arr[0], arr[1], simb]))

        for arr in dados[dados.index('---') + 1:]:
            casosTeste.append(arr)

    return estados, estadoI, estadosF, regras, casosTeste

