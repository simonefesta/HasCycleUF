from abc import ABC, abstractmethod
import random
from dictionary.trees.treeArrayList import TALNode as TreeNode
from dictionary.trees.treeArrayList import TreeArrayList as Tree
from datastruct.Queue import CodaArrayList_deque as Queue
from datastruct.Stack import PilaArrayList as Stack
from unionfind.quickFind import *
from unionfind.quickUnion import *
from time import time


class Node:
    """
    The graph basic element: node.
    """

    def __init__(self, id, value):
        """
        Constructor.
        :param id: node ID (integer).
        :param value: node value.
        """
        self.id = id
        self.value = value

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other node.
        :return: True if ids are equal; False, otherwise.
        """
        return self.id == other.id

    def __str__(self):
        """
        Returns the string representation of the node.
        :return: the string representation of the node.
        """
        return "[{}:{}]".format(self.id, self.value)

#
class Edge: # classe contente gli archi.
    """
    The graph basic element: (weighted) edge.
    """

    def __init__(self, tail, head, weight=None):
        """
        Constructor.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        """
        self.head = head
        self.tail = tail
        self.weight = weight

    def __cmp__(self, other):
        """
        Compare two edges with respect to their weight.
        :param other: the other edge to compare.
        :return: 1 if the weight is greater than the other;
        -1 if the weight is less than the other; 0, otherwise.
        """
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0

    def __lt__(self, other):
        """
        Less than operator.
        :param other: the other edge.
        :return: True, if the weight is less than the others; False, otherwise.
        """
        return self.weight < other.weight

    def __gt__(self, other):
        """
        Greater than operator.
        :param other: the other edge.
        :return: True, if the weight is greater than the others; False, otherwise.
        """
        return self.weight > other.weight

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other edge.
        :return: True if weights are equal; False, otherwise.
        """
        return self.weight == other.weight

    def __str__(self):
        """
        Returns the string representation of the edge.
        :return: the string representation of the edge.
        """
        return "({},{},{})".format(self.tail, self.head, self.weight)


class GraphBase(ABC): #Classe del Grafo
    """
    The basic graph data structure (abstract class).
    """

    def __init__(self):
        """
        Constructor.
        """
        self.nodes = {}  # dictionary {nodeId: node}
        self.nextId = 0  # the next node ID to be assigned

    def isEmpty(self):
        """
        Check if the graph is empty.
        :return: True, if the graph is empty; False, otherwise.
        """
        return not any(self.nodes)

    def numNodes(self):
        """
        Return the number of nodes.
        :return: the number of nodes.
        """
        return len(self.nodes)

    @abstractmethod
    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        ...

    @abstractmethod
    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        newNode = Node(self.nextId, elem)
        self.nextId += 1
        return newNode

    @abstractmethod
    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        ...

    @abstractmethod
    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        ...

    @abstractmethod
    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        ...

    @abstractmethod
    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        ...

    @abstractmethod
    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        ...

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        ...

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        ...

    @abstractmethod
    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # Note: this method only checks if tail and head exist
        ...


    @abstractmethod
    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        :rtype: list
        """
        ...

    @abstractmethod
    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        ...

    def genericSearch(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        tree = Tree(treeNode)
        vertexSet = {treeNode}  # nodes to explore
        markedNodes = {rootId}  # nodes already explored

        while len(vertexSet) > 0:  # while there are nodes to explore ...
            treeNode = vertexSet.pop()  # get an unexplored node
            adjacentNodes = self.getAdj(treeNode.info)
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # if not explored ...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # mark as explored
        return tree

    def bfs(self, rootId):
        """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # BFS nodes initialization
        bfs_nodes = []

        # queue initialization
        q = Queue()
        q.enqueue(rootId)

        explored = {rootId}  # nodes already explored

        while not q.isEmpty():  # while there are nodes to explore ...
            node = q.dequeue()  # get the node from the queue
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    q.enqueue(adj_node)
            bfs_nodes.append(node)

        return bfs_nodes

    def dfs(self, rootId):
        """
        Execute a Depth-First Search (DFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the DFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # DFS nodes initialization
        dfs_nodes = []

        # queue initialization
        s = Stack()
        s.push(rootId)

        explored = {rootId}  # nodes already explored

        while not s.isEmpty():  # while there are nodes to explore ...
            node = s.pop()  # get the node from the stack
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the stack
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    s.push(adj_node)

            print(dfs_nodes)
            dfs_nodes.append(node)

        return dfs_nodes

    @abstractmethod
    def print(self):
        """
        Print the graph.
        :return: void.
        """
        ...




#Di seguito sono implementate le richieste del progetto 2.




    def createGraph(self,nNode,cycle = False):
        """
        Crea un grafo, collegando gli archi, e creando un ciclo se necessario.
        :param nNode: il numero di nodi.
        :param cycle: True se vogliamo un ciclo, False altrimenti.
        """

        index = []
        for i in range(nNode):
            self.addNode(i)
            index.append(i)

        random.shuffle(index)

        for i in range (0, nNode - 1):
            self.insertEdge(index[i],index[i+1],1)
            self.insertEdge(index[i+1],index[i],1)
        if not cycle or nNode <=2:
            return
        else :
            self.insertEdge(index[0],index[nNode-1],1)
            self.insertEdge(index[nNode - 1],index[0],1)


    def decoratoreStampa (func):
        """
        Decorator: calcola il tempo di esecuzione e lo scrive su un file.
        :param func: algoritmo hasCyleUF & hasCycleDFS

        """
        def wrapper (self):
            start = time ()
            value = func (self)
            elapsed = elapsed = time() - start

            out_file = open("test.txt", "a")
            out_file.write("Numero archi : "+str(self.numEdges())+" tempo di esecuzione : "+str(elapsed)+"\n\n")
            out_file.close()
            print("ha impiegato :",elapsed, " s.")
            print("")



        return wrapper


    def controllo(self):
        """
        Dato un arco, esso viene aggiunto nella lista di archi orientati se esso non è già
        presente e se non è presente il suo arco complementare.
        Il flag c verifica tali condizioni. Se l'arco non è già presente, allora lo aggiunge.

        """

        edges = self.getEdges()
        edgesOriented = []
        for i in edges:
            c = False
            for k in edgesOriented :
                if (i.head == k.head) and (i.tail == k.tail):
                    c = True
                    break
                if ((i.head == k.tail) and (k.head == i.tail)):
                    c = True
                    break
            if (c == False):
                edgesOriented.append(i)

       # print("Edges:", [str(i) for i in edgesOriented ], "di dimensione :", len(edgesOriented ))
        return edgesOriented


    class EdgeIter():
        """
        Iterator degli archi.
        """

        def __init__(self, lista):
            self.lista = lista
            self.id = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.id == len(self.lista):
                raise StopIteration     # ferma l'iterazione
            value = self.lista[self.id]
            self.id +=1

            return value



    @decoratoreStampa
    def hasCycleUF(self):

        """
        Verifica la presenza di un ciclo prelevando gli archi ed eseguendo
        operazioni di find ed union. Se la find restituisce lo stesso risultato
        per i nodi formanti l'arco, allora è presente un ciclo, altrimenti viene
        eseguita una operazione di union.

        """
        print("hasCycleUF")
        uf = QuickFind()
        edgesOriented = self.controllo()
        for i in self.nodes:
           uf.makeSet(i)
        iterat = self.EdgeIter(edgesOriented)
        #iterat = iter(edgesOriented)
        for i in iterat :
            if uf.findRoot(uf.nodes[i.tail]).elem == uf.findRoot(uf.nodes[i.head]).elem :
                print("ha rilevato un ciclo.")
                return True
            else:

                uf.union(uf.findRoot(uf.nodes[i.tail]),uf.findRoot(uf.nodes[i.head]))
        print("NON ha rilevato un ciclo.")
        return False




    @decoratoreStampa
    def hasCycleDFS(self):

        """
        Verifica la presenza di un ciclo eseguendo una visita in profondità.
        Se è presente un ciclo, un elemento verrà aggiunto due volte nella Stack,
        e verrà aggiunto due volte alla lista dfs_nodes.
        Basta verificare la presenza di un nodo già presente per trovare un ciclo.

         """
        print("hasCycleDFS")
        rootId = (self.getNode(0).id)       #inizio dal nodo 0
        if rootId not in self.nodes:
            return None
        dfs_nodes = []
        s = Stack()
        s.push(rootId)

        explored = {rootId}

        while not s.isEmpty():
            node = s.pop()
            explored.add(node)
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    s.push(adj_node)

            if node in dfs_nodes:   #Se la visita DFS presenta un ciclo, il nodo che lo crea viene aggiunto due volte in dfs_nodes.
                print("ha rilevato un ciclo.")
                return True

            dfs_nodes.append(node)
        print("NON ha rilevato un ciclo.")
        return False


