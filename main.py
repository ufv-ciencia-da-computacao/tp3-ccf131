from graph import Graph, Node

def read_file(filename):
    with open(filename, "r") as arquivo:
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

if __name__ == "__main__":
    estados, estadoI, estadosF, regras, casosTeste = read_file("./text/test1.txt")

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