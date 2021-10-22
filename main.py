from graph import Graph, Node

def read_file(filename):
    with open(filename, "r") as arquivo:
        dados = arquivo.readlines()
        for i in range(len(dados)):
            dados[i] = dados[i].strip("\n")
        estados = dados[0].split(" ")[1:]
        alfabeto = list(dados[1][3:])
        estadoI = dados[2].split(" ")[1:]
        estadosF = dados[3].split(" ")[1:]

        regras = []
        casosTeste = []
        for arr in dados[4:dados.index('---')]:
            arr = arr.replace('->', '')
            states = arr[:arr.index('|')-1].split(" ")
            simb: str
            for simb in arr[arr.index('|')+2::2]:
                if simb == '\\' and simb in alfabeto:
                    raise Exception
                
                if not simb in alfabeto and simb != '\\':
                    raise Exception

                regras.append(tuple([states[0], states[2], simb]))

        for arr in dados[dados.index('---') + 1:]:
            casosTeste.append(arr)

    return estados, alfabeto, estadoI, estadosF, regras, casosTeste

if __name__ == "__main__":
    estados, alfabeto, estadoI, estadosF, regras, casosTeste = read_file("./text/test2.txt")

    g = Graph()
    for e in estados:
        initial = False
        final = False
        if e in estadoI:
            initial = True
        
        if e in estadosF:
            final = True

        g.add_nodes(Node(e, initial=initial, final=final))

    for r in regras:
        g.add_neighbors(r[0], r[1], r[2])
    
    for tcase in casosTeste:
        if g.is_valid(tcase):
            print('OK')
        else:
            print('X')