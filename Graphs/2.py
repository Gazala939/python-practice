class graph():
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = { }
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgesname = []
        for i in self.gdict:
            for j in self.gdict[i]:
                if(j,i) not in edgesname:
                    edgesname.append((i,j))
        return edgesname

graph_structure = {
    'a':["b","c"],
    'b':["a","c"],
    'c':["b","a"],
    'd':["a","e"]
}
g = graph(graph_structure)
print("The graph edges:",g.edges())
