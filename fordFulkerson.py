import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example3()

    # Le poids des arcs de ce graphe correspondent au flow
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

def example2():

    g = graph.Graph(np.array(["s", "1", "2", "3", "4", "t"]))

    g.addArc("s", "1", 16)
    g.addArc("s", "2", 13)
    g.addArc("1", "2", 10)
    g.addArc("2", "1", 4)
    g.addArc("1", "3", 12)
    g.addArc("2", "4", 14)
    g.addArc("3", "2", 9)
    g.addArc("4", "3", 7)
    g.addArc("3", "t", 20)
    g.addArc("4", "t", 4)

    return g

def example3():

    g = graph.Graph(np.array(["s", "A", "B", "C", "D", "E", "F", "t"]))

    g.addArc("s", "A", 10)
    g.addArc("s", "C", 12)
    g.addArc("s", "E", 15)
    g.addArc("A", "B", 9)
    g.addArc("A", "C", 4)
    g.addArc("A", "D", 15)
    g.addArc("B", "D", 15)
    g.addArc("B", "t", 10)
    g.addArc("C", "D", 8)
    g.addArc("C", "E", 4)
    g.addArc("D", "F", 15)
    g.addArc("D", "t", 10)
    g.addArc("E", "F", 16)
    g.addArc("F", "C", 6)
    g.addArc("F", "t", 10)

    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à  -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    # initialiser le flow comme zero
    for i in arcs:
        flow.addArcByIndex(i.id1, i.id2, 0.0)
    
    while True:
        # initialiser a chaque iteration chaque noeud comme non marque
        mark = [sys.float_info.max] * g.n
        # marquer s comme +
        mark[s] = 0
        while True:
            new_node_marked = False
            for i in arcs:
                # marquer un noeud comme positif (sens direct)
                if(mark[i.id1] != sys.float_info.max and mark[i.id2] == sys.float_info.max and i.weight > flow.adjacency[i.id1][i.id2]):
                    mark[i.id2] = i.id1
                    new_node_marked = True
                # marquer un noeud comme negatif (sens inverse)
                elif(mark[i.id1] == sys.float_info.max and mark[i.id2] != sys.float_info.max and flow.adjacency[i.id1][i.id2] > 0.0):
                    mark[i.id1] = -1 * i.id2
                    new_node_marked = True
            # conditions d'arret du boucle interieur
            if(new_node_marked == False):
                break
            elif(mark[t] != sys.float_info.max):
                break
        if mark[t] != sys.float_info.max:
            # chaine ameliorante
            result = 0
            # on va parcourir le chemin de t a s, stocke dans le vecteur mark
            current = t
            # stocker les valeurs qui seront ensuitecomparees 
            positive = []
            negative = []
            while True:
                if(mark[current] < 0):
                    # flow inverse : stocker le flow actuel
                    negative.append(flow.adjacency[current][abs(mark[current])])
                else:
                    # flow direct : stocker capacite - flow actuel
                    positive.append(g.adjacency[mark[current]][current] - flow.adjacency[mark[current]][current])
                current = abs(mark[current])
                # condition d'arret : arriver a s
                if current == s:
                    # cas ou la chaine ameliorante n'est composee que par des chemins directes
                    if(negative == []):
                        negative.append(sys.float_info.max)
                    result = min(min(positive), min(negative))
                    break
            current = t
            # modifier le flow pour appliquer la chaine ameliorante
            while True:
                if(mark[current] < 0):
                    flow.adjacency[current][abs(mark[current])] -= result
                else:
                    flow.adjacency[mark[current]][current] += result
                current = abs(mark[current])
                if current == s:
                    break
        # condition d'arret du boucle exterieur 
        else:
            break
    return flow
   
if __name__ == '__main__':
    main()