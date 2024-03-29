import numpy as np
import graph
import sys

def main():
    
    # # Graph 1
    # # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    # g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))
    # # Ajouter les arêtes
    # g.addEdge("a", "b",  1.0)
    # g.addEdge("a", "c",  8.0)
    # g.addEdge("b", "c",  2.0)
    # g.addEdge("b", "d",  5.0)
    # g.addEdge("b", "e",  7.0)
    # g.addEdge("b", "f",  9.0)
    # g.addEdge("c", "d",  4.0)
    # g.addEdge("d", "e",  6.0)
    # g.addEdge("d", "g", 12.0)
    # g.addEdge("e", "f",  8.0)
    # g.addEdge("e", "g", 11.0)
    # g.addEdge("f", "g", 10.0)

    # # Graph 2
    # g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g", "h"]))
    # g.addEdge("a", "b", 9.0)
    # g.addEdge("b", "d", 8.0)
    # g.addEdge("a", "f", 6.0)
    # g.addEdge("b", "e", 5.0)
    # g.addEdge("c", "g", 5.0)
    # g.addEdge("d", "g", 8.0)
    # g.addEdge("d", "h", 7.0)
    # g.addEdge("g", "h", 5.0)
    # g.addEdge("e", "f", 1.0)
    # g.addEdge("b", "c", 5.0)
    # g.addEdge("c", "d", 2.0)
    # g.addEdge("a", "h", 9.0)
    # g.addEdge("e", "g", 3.0)

    # Graph 3
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f"]))
    g.addEdge("a", "b", 4.0)
    g.addEdge("a", "c", 3.0)
    g.addEdge("b", "c", 5.0)
    g.addEdge("c", "f", 5.0)
    g.addEdge("b", "f", 2.0)
    g.addEdge("c", "d", 2.0)
    g.addEdge("d", "f", 3.0)
    g.addEdge("e", "f", 3.0)
    g.addEdge("d", "e", 4.0)
    
    # Obtenir un arbre couvrant de poids minimal du graphe
    tree = kruskal(g, False)
    
    # S'il existe un tel arbre (i.e., si le graphe est connexe)
    if tree != None:
        # L'afficher
        print(tree)
    
    else:
        print("Pas d'arbre couvrant")

# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g, computeMin):
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)

    # Nombre d'arêtes dans l'arbre
    addedEdges = 0
    
    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant
    edges.sort()

    # If the flag is false, we search for the maximum tree, therefore we set the edges in decreasing order
    if not(computeMin):
        edges.reverse()

    for i in range(len(edges)):
        if(tree.createACycle(edges[i]) == False):
            # if the edge can be added, find the names of the vertices
            name_1 = ""
            name_2 = ""
            for j in range(len(tree.nodes)):
                if(tree.indexOf(tree.nodes[j]) == edges[i].id1):
                    name_1 = tree.nodes[j]
                if(tree.indexOf(tree.nodes[j]) == edges[i].id2):
                    name_2 = tree.nodes[j]
        
            # add the vertices into the tree
            tree.addEdge(name_1, name_2, edges[i].weight)
            addedEdges += 1

        # we must stop after n - 1 selections
        if(addedEdges == (len(g.nodes) - 1)):
            return tree

    if addedEdges == 0 :
        return None

if __name__ == '__main__':
    main()
