class graph():
    def __init__(self,gdict= None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def findedge(self):
        edge = []
        for i in self.gdict:
            for j in self.gdict[i]:
                if (j,i) not in edge:
                    edge.append((i,j))
        return edge

    def add_edge(self,node1, node2):
        if node1 not in self.gdict:
            self.gdict[node1] = []
        if node2 not in self.gdict:
            self.gdict[node2] = []

    def getVertex(self):
        return list(self.gdict.keys())

graphs_structure = {
    'a':["b","c"],
    'b':["a","c"],
    'c':["b","a"],
    'd':["a","e"]
}

g = graph(graphs_structure)
g.add_edge("a","b")
print("Vertices:",g.getVertex())
print("Edges:",g.findedge())
