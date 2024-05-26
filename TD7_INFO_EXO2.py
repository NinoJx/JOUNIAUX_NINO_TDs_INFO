import tkinter
from tkinter import Canvas
import numpy as np
import random

w = tkinter.Tk()
w.title("Plan")
can = Canvas(w, width=600, height=600, bg="grey")
can.grid(row=0, column=0, columnspan=3)

graph = [[2], [], [4], [1], [6], [3], [7], [5]]

COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

pos = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]

colors = []
for i in range(len(graph)):
    colors.append(random.randint(0,7))

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

# J'APPLIQUE MIN LOCAL SUR LE POINT 3
min_local(3,graph,colors)
draw(can, graph, pos,colors)
can.grid(row=1, column=1)
    
w.mainloop()
    

        


