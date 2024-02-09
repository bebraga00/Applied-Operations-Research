import graph
import sys
import numpy as np

def main():
    cities = []
    cities.append("Paris")
    cities.append("Hambourg")
    cities.append("Londres")
    cities.append("Amsterdam")
    cities.append("Edimbourg")
    cities.append("Berlin")
    cities.append("Stockholm")
    cities.append("Rana")
    cities.append("Oslo")

    g = graph.Graph(cities)
    
    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris",  "Londres", 4)
    g.addArc("Paris",  "Amsterdam", 3)
    g.addArc("Hambourg",  "Stockholm", 1)
    g.addArc("Hambourg",  "Berlin", 1)
    g.addArc("Londres",  "Edimbourg", 2)
    g.addArc("Amsterdam",  "Hambourg", 2)
    g.addArc("Amsterdam",  "Oslo", 8)
    g.addArc("Stockholm",  "Oslo", 2)
    g.addArc("Stockholm",  "Rana", 5)
    g.addArc("Berlin",  "Amsterdam", 2)
    g.addArc("Berlin",  "Stockholm", 1)
    g.addArc("Berlin",  "Oslo", 3)
    g.addArc("Edimbourg",  "Oslo", 7)
    g.addArc("Edimbourg",  "Amsterdam", 3)
    g.addArc("Edimbourg",  "Rana", 6)
    g.addArc("Oslo",  "Rana", 2)
    
    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    tree = dijkstra(g, "Paris")
    print(tree)

def dijkstra(g, origin):
   # Get the index of the origin 
   r = g.indexOf(origin)
   print(g.nodes)

   VminusR = []
   id_not_yet_pivot = []
   for i in range(len(g.nodes)):
       id_not_yet_pivot.append(g.indexOf(g.nodes[i]))
       VminusR.append(g.indexOf(g.nodes[i]))

   VminusR.remove(r)
   # Next node considered 
   pivot = r

   # Liste qui contiendra les sommets ayant été considérés comme pivot
   v2 = []
   v2.append(r)
   id_not_yet_pivot.remove(r)
   
   pred = [0] * g.n
   
   # Les distances entre r et les autres sommets sont initialement infinies
   pi = [sys.float_info.max] * g.n
   pi[r] = 0

   for j in VminusR:
       for y in id_not_yet_pivot:
           found = False
           # verify if pivot points to current node
           for i in range(len(g.getArcs())):
               if(g.getArcs()[i].id1 == pivot and g.getArcs()[i].id2 == y):
                   found = True
                   arc = g.getArcs()[i]
           if found:
               if(pi[int(pivot)] + arc.weight < pi[y]):
                   pi[y] = pi[int(pivot)] + arc.weight
                   pred[y] = pivot
       
       # find the argmin in pi
       argmin = 0
       min = sys.float_info.max
       for z in range(len(id_not_yet_pivot)):
           if(pi[id_not_yet_pivot[z]] < min):
               min = pi[id_not_yet_pivot[z]]
               argmin = id_not_yet_pivot[z]
       pivot = argmin
       id_not_yet_pivot.remove(pivot)


   A2 = []
   for x in VminusR:
       A2.append([pred[x], x])

   return(A2)

   
if __name__ == '__main__':
    main()
