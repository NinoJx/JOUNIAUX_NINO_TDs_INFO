#Objectif du TD : créer la classe Tree avec toutes ses méthodes
class Tree:
#EXO 2   
    def __init__(self,symbol,*children):
        self._symbol = symbol
        self._children = children
        
    def label(self):
        return str(self._symbol)
    
    def children(self):
        return self._children
    
    def nb_children(self):
        return len(self._children)
    
    def child(self, i : int):
        return self._children[i]
    
    def is_leaf(self):
        return not self._children
#EXO 3    
    def depth(self):
        m = 0
        liste = []
        for i in range(len(self._children)):
            liste.append(self._children[i])
        for arbre in liste:
            if arbre.depth() >= m:
                m = 1 + arbre.depth()
        return m
#EXO 4   
    def __str__(self):
        if not self._children:
            return str(self._symbol)
        else:
            return f"{self._symbol}({','.join(str(child) for child in self._children)})"
    
    def __eq__(self,other):
        if not isinstance(other, Tree):
            return False
        if self._symbol != other._symbol:
            return False
        if len(self._children) != len(other._children):
            return False
        for child1, child2 in zip(self._children, other._children):
            if child1 != child2:
                return False
        return True
#EXO 5   
    def deriv(self, var: str) -> 'Tree':
        if self.is_leaf():
            if self._symbol == var:
                return Tree('1')
            else:
                return Tree('0')
        elif self._symbol == '+':
            return Tree('+', self._children[0].deriv(var), self._children[1].deriv(var))
        elif self._symbol == '*':
            return Tree('+',Tree('*', self._children[0].deriv(var), self._children[1]),Tree('*', self._children[0], self._children[1].deriv(var)))
#EXO 6       
    def substitute(self, t1, t2):
        if self == t1: # afin d'éviter de faire tourner le programme pour rien
            return t2
        else:
            childrenv2 = [arbre.substitute(t1, t2) for arbre in self._children]
            return Tree(self._symbol, childrenv2)
        
# TESTS
    
# test exos 1 à 4
# tests manuels , testsmanuel() pour les lancer et on a bien les bons retours
def testsmanuel():    
    exemple = Tree('f',Tree('a'),Tree('b'))
    faussecopie = Tree('f',Tree('a'),Tree('b'))
    print(exemple.label())
    print(exemple.children())
    print(exemple.nb_children())
    print(exemple.child(1))
    print(exemple.is_leaf())
    print(exemple.depth())
    print(exemple.__str__())
    print(exemple.__eq__(faussecopie))
# j'ai également effectué le test dans la fonction test_TD3_INFO.py grâce à UnitTest et tout est ok

# test exo 5
expression =  Tree('+', Tree('*', Tree('3'), Tree('^', Tree('X'), Tree('2'))), Tree('*', Tree('5'), Tree('X')), Tree('7'))          
print("Expression originale:", expression)
print("Dérivée par rapport à 'X':", expression.deriv('X'))

#test exo 6
e1 = Tree('+', Tree('a'), Tree('X'))
e2 = Tree('b')
e3 = e1.substitute(Tree('X'), e2)
