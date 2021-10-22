class Node:
    def __init__(self, name, initial=False, final=False) -> None:
        self.name = name
        self.initial = initial
        self.final = final

class Graph:
    def __init__(self) -> None:
        self.edges = {}
        self.nodes = {}
        self.init_states = []
        self.final_states = []
    
    def add_nodes(self, node: Node):
        self.edges[node.name] = []
        self.nodes[node.name] = node
        
        if node.initial:
            self.init_states.append(node.name)
        
        if node.final:
            self.final_states.append(node.name)
    
    def get_node(self, source_name: str) -> Node:
        if source_name in self.nodes.keys():
            return self.nodes[source_name]
        return None
    
    def add_neighbors(self, source_name: str, destination_name: str, symbol: str):
        if self.get_node(source_name) is not None:
            self.edges[source_name].append((destination_name, symbol))
        else:
            raise Exception
    
    def dfs(self, edges: list, curr_state: Node, list_symbols: str, pos: int) -> bool:
        ans = False
        
        if pos >= len(list_symbols):
            if curr_state.final:
                return True
            else:
                return False

        neighs, transitions = zip(*edges)
    
        for i in range(len(transitions)):
            if transitions[i] == list_symbols[pos] or transitions[i] == '\\':
                next_state_name = neighs[i]
                n = self.get_node(next_state_name)
                edges = self.edges[n.name]

                ans |= self.dfs(edges, n, list_symbols, pos+1)
        
        if list_symbols[pos] == '':
            ans |= self.dfs(edges, curr_state, list_symbols, pos+1)
        
        return ans

    def is_valid(self, list_symbols: str):
        if self.init_states and self.final_states: 
            for name in self.init_states:
                n = self.get_node(name)
                edges = self.edges[n.name]

                if self.dfs(edges, n, list_symbols, 0):
                    return True

            return False
        else:
            raise Exception

if __name__ == '__main__':
    a = Node('a', initial=True, final=True)
    b = Node('b')
    c = Node('c')
    d = Node('d', final=True)
    e = Node('e')

    g = Graph()
    g.add_nodes(a)
    g.add_nodes(b)
    g.add_nodes(c)
    g.add_nodes(d)
    g.add_nodes(e)

    g.add_neighbors('a', 'b', '1')
    g.add_neighbors('a', 'd', '0')
    g.add_neighbors('b', 'c', '0')
    g.add_neighbors('b', 'e', '1')
    g.add_neighbors('c', 'c', '0')
    g.add_neighbors('c', 'd', '1')
    g.add_neighbors('d', 'd', '0')
    g.add_neighbors('d', 'd', '1')
    g.add_neighbors('e', 'e', '0')
    g.add_neighbors('e', 'e', '1')

    if g.is_valid("001"):
        print("OK")
    else:
        print("X")

    if g.is_valid("1000"):
        print("OK")
    else:
        print("X")

    if g.is_valid(""):
        print("OK")
    else:
        print("X")

    if g.is_valid("10000011"):
        print("OK")
    else:
        print("X")

    if g.is_valid("111"):
        print("OK")
    else:
        print("X")

    if g.is_valid("1"):
        print("OK")
    else:
        print("X")