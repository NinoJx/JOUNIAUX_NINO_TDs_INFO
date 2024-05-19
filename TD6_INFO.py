import tkinter
from tkinter import Canvas
import numpy as np
from random import random

w = tkinter.Tk()
w.title("Plan")
can = Canvas(w, width=600, height=600, bg="deepsky blue")
can.grid(row=0, column=0, columnspan=3)


graph0 = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
          [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

pos = np.array([(random() * 600, random() * 600) for i in range(len(graph0))])

def draw(can, graph, pos):
    can.delete('all')
    for i in range(len(graph)):
        for j in graph[i]:
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#f3e1d4")

draw(can, graph0, pos)
can.grid(row=1, column=1)

# constantes
tau = 0.1
k = 1

vit = np.array([[(random() - 0.5) * 10, (random() - 0.5) * 10]
                for i in range(len(graph0))])

def deplace(event):
    global pos
    global vit

    # Calcul du barycentre des positions
    barycentre = np.mean(pos, axis=0)
    centre = np.array([300, 300])
    
    F = []

    for i in range(len(graph0)):
        fx, fy = 0, 0
        for j in graph0[i]:
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dist = np.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                fx += k * (dx / dist)
                fy += k * (dy / dist)
        
        # Force centripète vers le centre du canevas
        fx += (centre[0] - barycentre[0])
        fy += (centre[1] - barycentre[1])

        F.append([fx, fy])

    for i in range(len(F)):
        for j in range(len(F[i])):
            F[i][j] *= tau

    vit = vit + F

    for i in range(len(vit)):
        vit[i][0] = min(max(vit[i][0], -5), 5)
        vit[i][1] = min(max(vit[i][1], -5), 5)

    pos = pos + vit

    draw(can, graph0, pos)

w.bind("<f>", deplace)
w.mainloop()
