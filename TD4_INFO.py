# imports
import matplotlib.pyplot as plt

# fonction de hashage
def h(chaine):
    h = 0
    n = len(chaine)
    for i in range(n):
        h = h + ord(chaine[i])
    return h
       
assert h('abc') == 294  #un test de la fonction de hashage

# création de la classe
class Hashtable:
    def __init__(self,f=h,size=20):
        self._hashfunction = f
        self._size = size
        self._table = [[] for _ in range(size)]
        self.threshold = 1.2 * size
        
    def put(self,key,value):
        n = self._size
        if sum(len(table) for table in self._table) > self.threshold:
            self.resize()
        a = self._hashfunction(key)%n
        for j in range(len(self._table[a])):
            if key == self._table[a][j][0]:
                del(self._table[a][j])
        self._table[a].append((key,value))
        
    def get(self,key):
        for i in range(self._size):
            for j in range(len(self._table[i])):
                if key == self._table[i][j][0]:
                    return (key,self._table[i][j][1])
        return None
    
    def repartition(self):
        N = self._size
        x = range(N)
        y = [len(self._table[i]) for i in range(N)]
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
        
    def resize(self):
        new_size = self._size * 2
        new_tables = [[] for _ in range(new_size)]
        for table in self._table:
            for key, value in table:
                new_index = self._hashfunction(key, new_size)
                new_tables[new_index].append((key, value))
        self._size = new_size
        self._table = new_tables
         
# tests
if __name__ == '__main__':
    H = Hashtable()
    H.put('abc',3)
    print(H.get('aaa'))
    print(H.get('abc'))
    H.put('bbb',5)
    H.repartition()
# Résultat : affiche None et ('abc',3), ce qui est logique
# le diagramme en barres a 1 barre de hauteur 2 après l'ajout , tout est ok

def exo5(nombre_entrees):
    H0 = Hashtable(h,nombre_entrees)
    f = open("frenchssaccent.dic",'r')
    lexique = []
    for ligne in f:
        lexique.append(ligne[0:len(ligne)-1]) #on enlève bien le passage à la ligne qui est dans le fichier de base
    f.close()
    for i in range(len(lexique)):
        H0.put(lexique[i],len(lexique[i]))
    H0.repartition()

# exo5(320) affiche un graphe d'allure similaire avec celui de l'énoncé
# on a un problème avec exo5(10000), il faut donc changer de fonction de hashage

# on change de fonction de hashage
def jenkins_hashage(chaine):
    n = len(chaine)
    h = 0
    for i in range(n):
        h += ord(chaine[i])
        h += (h << 10)
        h ^= (h >> 6)
    h += (h << 3)
    h ^= (h >> 11)
    h += (h << 15)
    return h

def exo5bis(nombre_entrees):
    H0 = Hashtable(jenkins_hashage,nombre_entrees)
    f = open("frenchssaccent.dic",'r')
    lexique = []
    for ligne in f:
        lexique.append(ligne[0:len(ligne)-1]) #on enlève bien le passage à la ligne qui est dans le fichier de base
    f.close()
    for i in range(len(lexique)):
        H0.put(lexique[i],len(lexique[i]))
    H0.repartition()

# la répartition est beaucoup plus uniforme

# exo 6 : voir la fin du constructeur pour la méthode resize()
# + voir lignes 20, 24 et 25 pour la modification de put
                    


        
        

        
        
                    
            
        
        