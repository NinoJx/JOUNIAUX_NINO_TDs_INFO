from logging import root
import tkinter
import random
from tkinter import Tk, Canvas, Button, TOP, LEFT, RIGHT, ALL

w=tkinter.Tk() #w = root
w.title("Cible")
can = Canvas(w,width=400,height=400,bg="red") #can = canvas
can.grid(row=0,column=0,columnspan=3)
#cercles
can.create_oval(30,30,370,370, outline="red",fill="white")
can.create_oval(60,60,340,340,outline="red",fill="white")
can.create_oval(90,90,310,310,outline="red",fill="white")
can.create_oval(120,120,280,280,outline="red",fill="white")
can.create_oval(150,150,250,250,outline="red",fill="red")
can.create_oval(180,180,220,220,outline="red",fill="white")
#lignes
can.create_line(200,0,200,400,fill="red")
can.create_line(0,200,400,200,fill="red")
#numéros
can.create_text(200,45,text='1',font=('Times','12','bold'),fill="red")
can.create_text(200,75,text='2',font=('Times','12','bold'),fill="red")
can.create_text(200,105,text='3',font=('Times','12','bold'),fill="red")
can.create_text(200,135,text='4',font=('Times','12','bold'),fill="red")
can.create_text(200,165,text='5',font=('Times','12','bold'),fill="white")
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
    global Compteurglobal
    X=[]
    Y=[]
    compteur=0
    for i in range(5):
        tiragex=random.randint(8,392)
        tiragey=random.randint(8,392)
        X.append(tiragex) # on conserve les coordonnées du point pour calculer les scores par la suite
        Y.append(tiragey)
        can.create_oval(tiragex-8,tiragey-8,tiragex+8,tiragey+8, outline="red",fill="black") #créé le cercle du à l'impact
        if (X[i]-200)**2+(Y[i]-200)**2<=30**2:
            compteur+=6
        elif (X[i]-200)**2+(Y[i]-200)**2<=60**2:
            compteur+=5
        elif (X[i]-200)**2+(Y[i]-200)**2<=90**2:
            compteur+=4
        elif (X[i]-200)**2+(Y[i]-200)**2<=120**2:
            compteur+=3
        elif (X[i]-200)**2+(Y[i]-200)**2<=150**2:
            compteur+=2
        elif (X[i]-200)**2+(Y[i]-200)**2<=180**2:
            compteur+=1       
    Compteurglobal+=compteur
    lab=tkinter.Label(w,text=f"Le score est {Compteurglobal} ")
    lab.grid(row=3,column=1,sticky=tkinter.W)
b1["command"]=tir  

def tirunique(event):
    global Compteurglobal
    tiragex=random.randint(8,392)
    tiragey=random.randint(8,392)
    can.create_oval(tiragex-8,tiragey-8,tiragex+8,tiragey+8, outline="red",fill="black")
    if (tiragex-200)**2+(tiragey-200)**2<=30**2:
            Compteurglobal+=6
    elif (tiragex-200)**2+(tiragey-200)**2<=60**2:
            Compteurglobal+=5
    elif (tiragex-200)**2+(tiragey-200)**2<=90**2:
            Compteurglobal+=4
    elif (tiragex-200)**2+(tiragey-200)**2<=120**2:
            Compteurglobal+=3
    elif (tiragex-200)**2+(tiragey-200)**2<=150**2:
            Compteurglobal+=2
    elif (tiragex-200)**2+(tiragey-200)**2<=180**2:
            Compteurglobal+=1
    lab=tkinter.Label(w,text=f"Le score est {Compteurglobal} ")
    lab.grid(row=3,column=1,sticky=tkinter.W)

w.bind("<f>",tirunique)

w.mainloop()