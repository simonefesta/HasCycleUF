from quickUnion import *
from quickFind import *
from time import time


def testUnionFind(n, uf):

    start = time()
    for i in range(n):                      # genero n makeset (la creazione dipende dal parametro, poichè passo quickfind, union, balanced...
        uf.makeSet(i)
    elapsed = time() - start
    print("MAKESET:", elapsed, " s")

    start = time()
    for i in range(n):                      # quanto ci metto a trovare TUTTI gli n nodi?
        uf.find(uf.nodes[i])
    elapsed = time() - start
    print("FIND:", elapsed, " s")

    start = time()                          # unisco il nodo i con i+1
    for i in range(n - 1):
        uf.union(uf.findRoot(uf.nodes[i]), uf.findRoot(uf.nodes[i + 1]))
        #uf.union(uf.findRoot(random.choice(uf.nodes)), uf.findRoot(random.choice(uf.nodes)))
    elapsed = time() - start
    print("UNION:", elapsed, " s")

    start = time()
    for i in range(n - 1):              #cerco i nodi dopo averli uniti.
        uf.find(uf.nodes[i])
        #uf.find(random.choice(uf.nodes))
    elapsed = time() - start
    print("FIND dopo la UNION:", elapsed, " s")

    print()


if __name__ == "__main__":
    n = 1000000
    qf = QuickFind()
    print("QUICKFIND\n")

    testUnionFind(n, qf)

    qfb = QuickFindBalanced()
    print("QUICKFIND BALANCED\n")

    testUnionFind(n, qfb)

    qu = QuickUnion()
    print("QUICKUNION\n")

    testUnionFind(n, qu)

    qub = QuickUnionBalanced()
    print("QUICKUNION BALANCED\n")

    testUnionFind(n, qub)

    qubpc = QuickUnionBalancedPathCompression()
    print("QUICKUNION BALANCED PATH COMPRESSION\n")

    testUnionFind(n, qubpc)

    qubps = QuickUnionBalancedPathSplitting()
    print("QUICKUNION BALANCED PATH SPLITTING\n")

    testUnionFind(n, qubps)

