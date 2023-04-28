from graph.Graph_AdjacencyList import GraphAdjacencyList
from random import randint

# NB: le varie implementazioni sono allegate nel file Graph.py , partendo da riga 344.

if __name__ == "__main__":
    graph = GraphAdjacencyList()
    randomvalue = randint(2,500)
    graph.createGraph(randomvalue,True) #False : no ciclo , True : ciclo.
    graph.print()
    graph.hasCycleUF()
    graph.hasCycleDFS()