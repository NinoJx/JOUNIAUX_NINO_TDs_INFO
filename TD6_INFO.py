from logging import root
import tkinter
from tkinter import Tk, Canvas, Button, TOP, LEFT, RIGHT, ALL
import numpy as np
from random import *
#EXERCICE 1
w=tkinter.Tk() #w = root
w.title("Plan")
can = Canvas(w,width=600,height=600,bg="deepsky blue") #can = canvas
can.grid(row=0,column=0,columnspan=3)

graph0 = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

pos = np.array([(random()*600, random()*600)
       for i in range(len(graph0))])

def draw(can, graph, pos):
    can.delete('all')
    for i in range(len(graph)):
        for j in graph[i]:  
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")

draw(can,graph0,pos)
can.grid(row=1,column=1)
#EXERCICE 2 ( force ressort : F = - kl )
tau = 0.1
k = 1
vit = np.array([[(random()-0.5)*10, (random()-0.5)*10]
       for i in range(len(graph0))])

def deplace(event):
    F = []
    global pos
    global vit
    for i in range(len(graph0)):
        x,y = 0,0
        for j in graph0[i]:
            x = x -k*abs(pos[i][0]-pos[j][0])
            y = y -k*abs(pos[i][1]-pos[j][1])
        F.append([x,y])
#FORCE CENTRALE POUR EVITER DE SORTIR ( exo3 )
# on calcule le barycentre des forces pondérées par la position
    a = 0
    for i in range(len(F)):
        a = a + pos[i][0]
    b = 0
    for i in range(len(F)):
        b = b + pos[i][1]
    L = [a/len(graph0),b/len(graph0)]
#   
    for i in range(len(F)):
        for j in range(len(F[i])):
            F[i][j] = F[i][j]*tau + k*L[j]
    vit = vit + F
    for i in range(len(vit)):
        for j in range(len(vit[i])):
            vit[i][j] = vit[i][j]*tau
    pos = pos + vit
    draw(can,graph0,pos)
    
w.bind("<f>",deplace)
w.mainloop()
