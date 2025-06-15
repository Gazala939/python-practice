# Displaying ghraphs vertices

class graph():
    def __init__(self,gdict= None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())  #The keys() method retrieves only the vertex names (i.e., 'a', 'b', 'c', 'd', 'e').

graphs_structure = {
    'a':["b","c"],
    'b':["a","c"],
    'c':["b","a"],
    'd':["a","e"]
}
g = graph(graphs_structure)
print("The give vertices of the given graphs is:",g.getVertices())

#Keys ('a', 'b', 'c', 'd') → Represent vertices (nodes).
#Values (["b", "c"], etc.) → Represent edges (connections).