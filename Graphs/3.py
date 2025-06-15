class graph():
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = { }
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def addVertex(self,vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

graphs_structure = {
    'a':["b","c"],
    'b':["a","c"],
    'c':["b","a"],
    'd':["a","e"]
}
g = graph(graphs_structure)
g.addVertex('f')
print(g.getVertices())
