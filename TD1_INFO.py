from copy import deepcopy #pour copier une liste sans quelles soient liées

#EXERCICE 2

#Entrée : un tirage de n lettres
#Sortie : le mot le plus long (appartenant au lexique) pouvant être écrit avec ces lettres
def motlong(tirage):
    #on commence par importer le lexique sous la forme d'une liste de mots
    f = open("frenchssaccent.dic",'r')
    lexique = []
    for ligne in f:
        lexique.append(ligne[0:len(ligne)-1]) #on enlève bien le passage à la ligne qui est dans le fichier de base
    f.close()
    #on a désormais le lexique sous la forme d'une liste de mots
    motsfaisable = []
    for mot in lexique:
        a = 1
        copie = deepcopy(tirage)
        for i in range(0,len(mot)):
            if mot[i] not in copie:
                a = 0
            else:
                copie.remove(mot[i])
        if a == 1:   
            motsfaisable.append(mot)
    #on a la liste des mots faisable, maitenant on cherche le plus grand
    motsfaisable.sort(key=len)
    return motsfaisable[-1]
    #ici le plus grand retourné sera toujours celui de plus loin dans l'alphabet, je pense pas que cela pose problème on en veut juste un
    
tirage = ['a','r','b','g','e','s','c','j']

#appeler motlong(tirage)
#on a 'scare'

#FIN EXERCICE 2

#EXERCICE 3

def mot_max_score(tirage):
    #on commence par importer le lexique sous la forme d'une liste de mots
    f = open("frenchssaccent.dic",'r')
    lexique = []
    for ligne in f:
        lexique.append(ligne[0:len(ligne)-1]) #on enlève bien le passage à la ligne qui est dans le fichier de base
    f.close()
    #on a désormais le lexique sous la forme d'une liste de mots
    n = len(tirage)
    motsfaisable = []
    for mot in lexique:
        a = 1
        copie = deepcopy(tirage)
        for i in range(0,len(mot)):
            if mot[i] not in copie:
                a = 0
            else:
                copie.remove(mot[i])
        if a == 1:   
            motsfaisable.append(mot)
    #on a la liste des mots faisable
    m = score(motsfaisable[0])
    res = motsfaisable[0]
    for x in motsfaisable:
        if score(x)>m:
            m = score(x)
            res = x
    return m,res

dicopoints = {'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}

def score(mot):
    r = 0
    for x in mot:
        r = r + dicopoints[x]
    return r
        
#appeler mot_max_score(tirage)
# on a (12,'jaser')

#FIN EXERCICE 3

#EXERCICE 4



