from logging import root
import tkinter
import random
from tkinter import Tk, Canvas, Button, TOP, LEFT, RIGHT, ALL

w=tkinter.Tk() #w = root
w.title("Cible")
can = Canvas(w,width=400,height=400,bg="red") #can = canvas
can.grid(row=0,column=0,columnspan=3)
#cercles
can.create_oval(30,30,370,370, outline="red",fill="ivory")
can.create_oval(60,60,340,340,outline="red",fill="ivory")
can.create_oval(90,90,310,310,outline="red",fill="ivory")
can.create_oval(120,120,280,280,outline="red",fill="ivory")
can.create_oval(150,150,250,250,outline="red",fill="red")
can.create_oval(180,180,220,220,outline="red",fill="ivory")
#lignes
can.create_line(200,0,200,400,fill="red")
can.create_line(0,200,400,200,fill="red")
#numéros
can.create_text(200,45,text='1',font=('Times','12','bold'),fill="red")
can.create_text(200,75,text='2',font=('Times','12','bold'),fill="red")
can.create_text(200,105,text='3',font=('Times','12','bold'),fill="red")
can.create_text(200,135,text='4',font=('Times','12','bold'),fill="red")
can.create_text(200,165,text='5',font=('Times','12','bold'),fill="ivory")
can.create_text(200,195,text='6',font=('Times','12','bold'),fill="red")
#boutons
b1=Button(w)
b2=Button(w)
b1["text"]="Feu!"
b2["text"]="Quitte"
b1.grid(row=3,column=0,sticky=tkinter.W)
b2.grid(row=3,column=2,sticky=tkinter.E)
b2["command"]=w.destroy

#fonctions

Compteurglobal = 0

def tir():
    global a
    global Compteurglobal
    X=[]
    Y=[]
    compteur=0
    for i in range(5-a):
        tiragex=random.randint(0,400)
        tiragey=random.randint(0,400)
        X.append(tiragex) # on conserve les coordonnées du point pour calculer les scores par la suite
        Y.append(tiragey)
        can.create_oval(tiragex-8,tiragey-8,tiragex+8,tiragey+8, outline="red",fill="black") #créé le cercle du à l'impact
        if (X[i]-200)**2+(Y[i]-200)**2<=15**2:
            compteur+=6
        elif (X[i]-200)**2+(Y[i]-200)**2<=45**2:
            compteur+=5
        elif (X[i]-200)**2+(Y[i]-200)**2<=75**2:
            compteur+=4
        elif (X[i]-200)**2+(Y[i]-200)**2<=105**2:
            compteur+=3
        elif (X[i]-200)**2+(Y[i]-200)**2<=135**2:
            compteur+=2
        elif (X[i]-200)**2+(Y[i]-200)**2<=165**2:
            compteur+=1       
    Compteurglobal+=compteur
    lab=tkinter.Label(w,text=f"Score : {Compteurglobal} ")
    lab.grid(row=3,column=1,sticky=tkinter.W)
    a = 0
b1["command"]=tir  
a = 0  # cette variable sert à ce que quand on tire 2 fois à l'aide de "f", on tire que 3 fois si on appuie sur "feu" etc...
def tirunique(event):
    global Compteurglobal
    global a
    tiragex=random.randint(0,400)
    tiragey=random.randint(0,400)
    can.create_oval(tiragex-8,tiragey-8,tiragex+8,tiragey+8, outline="red",fill="black")
    if (tiragex-200)**2+(tiragey-200)**2<=30**2:
            Compteurglobal+=6
    elif (tiragex-200)**2+(tiragey-200)**2<=45**2:
            Compteurglobal+=5
    elif (tiragex-200)**2+(tiragey-200)**2<=75**2:
            Compteurglobal+=4
    elif (tiragex-200)**2+(tiragey-200)**2<=105**2:
            Compteurglobal+=3
    elif (tiragex-200)**2+(tiragey-200)**2<=135**2:
            Compteurglobal+=2
    elif (tiragex-200)**2+(tiragey-200)**2<=165**2:
            Compteurglobal+=1
    lab=tkinter.Label(w,text=f"Score : {Compteurglobal} ")
    lab.grid(row=3,column=1,sticky=tkinter.W)
    a = a + 1

w.bind("<f>",tirunique)

w.mainloop()