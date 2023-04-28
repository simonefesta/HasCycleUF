# HasCycleUF
Progetto 2 in itinere di "Ingegneria degli Algoritmi", a.a. 2018/2019

Dato un grafo G connesso, non orientato e non pesato, implementare due
algoritmi per determinare se G ha almeno un ciclo:

- hasCycleUF(G) che usa la struttura dati UnionFind come descritto in
Algorithm 1 e un iterator per scandire tutti gli edge del grafo

- hasCycleDFS(G) che usa l’approccio della visita in profondità (Depth-First
Search)


Dopo aver scelto l’implementazione di UnionFind (QuickFind, QuickUnion, ecc)
che minimizza il tempo di esecuzione di hasCycleUF(G), confrontare il tempo
di esecuzione dei due algoritmi al variare della dimensione del grafo di input. I
dati degli esperimenti devono essere scritti su un file da un decorator di Python
(applicato alle funzioni dei due algoritmi) con il formato n, t su ogni riga dove
n è il numero di archi del grafo e t il tempo di esecuzione dell’algoritmo. Inoltre
implementare un algoritmo che genera grafi con o senza cicli, da usare nella fase
di testing.
