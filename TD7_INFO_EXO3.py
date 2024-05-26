
import tkinter
from tkinter import Canvas
import numpy as np
import random 

w = tkinter.Tk()
w.title("Plan")
can = Canvas(w, width=600, height=600, bg="grey")
can.grid(row=0, column=0, columnspan=3)

graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])

COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

colors = random.sample(range(12), 12) #met les couleurs sur les points aléatoirement

    
def draw(can, graph, pos, colors):
    N = len(graph)
    can.delete('all')
    for i in range(N):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for i in range(N):
        x, y = pos[i]
        can.create_oval(x-6, y-6, x+6, y+6, fill=COLORS[colors[i]])
        can.create_text(x-12,y,text=f"{i}")
        
def min_local(i,graph,colors):
    L = [i] #liste des voisins et le sommet lui même
    for j in graph[i]:
        L.append(j)
    for h in range(len(graph)):
        if i in graph[h]:
            L.append(h)
    LL = []
    for k in range(len(L)):
        LL.append(colors[L[k]])
    a = min(LL)
    colors[i] = a
    for j in L:
        colors[j] = a

# on veut commencer par appliquer min local sur le sommet de colors le plus faible
# crée une liste des index 
index_liste = list(range(len(colors)))

# trie la liste des index en fonction des valeurs correspondantes dans colors
index_trie = sorted(index_liste, key=lambda i: colors[i])

for i in range(len(index_trie)):
    min_local(index_trie[i],graph,colors)
    
draw(can, graph, pos,colors)
can.grid(row=1, column=1)
w.mainloop()


        

