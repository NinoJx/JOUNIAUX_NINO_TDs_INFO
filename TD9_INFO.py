#EXO 1
class Polynomial_Zq:
    def __init__(self, coefficients,q,n):
        self.q = q
        self.n = n
        self.coefficients = [coeff % q for coeff in coefficients]
        self.reduce_mod_xn_plus_1()

    def reduce_mod_xn_plus_1(self):
        if len(self.coefficients) > self.n:
            for i in range(self.n, len(self.coefficients)):
                indic = (-1)**(i//self.n-i%self.n)
                self.coefficients[i % self.n] = (self.coefficients[i%self.n]+indic*self.coefficients[i])%self.q
                self.coefficients = self.coefficients[:self.n]

    def __str__(self):
        polynomial_str = ""
        degree = len(self.coefficients) - 1
        for index, coef in enumerate(self.coefficients):
            power = degree - index
            if coef != 0:
                if power == 0:
                    polynomial_str += str(coef)
                elif power == 1:
                    if coef == 1:
                        polynomial_str += f"X"
                    else:
                        polynomial_str += f"{coef}*X"
                else:
                    if coef == 1:
                        polynomial_str += f"X**{power}"
                    else:
                        polynomial_str += f"{coef}*X**{power}"
                if index < len(self.coefficients) - 1:
                    polynomial_str += " + "
        return polynomial_str
#EXO 2
    def add(self, other):
        assert self.q == other.q
        assert self.n == other.n
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_length - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_length - len(other.coefficients))
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial_Zq(result_coefficients)
#EXO 3
    def mul(self, other):
        assert self.q == other.q
        assert self.n == other.n
        max_length = len(self.coefficients) + len(other.coefficients)
        padded_self = self.coefficients + [0] * (max_length - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_length - len(other.coefficients))
        result_coefficients = []
        for i in range(0,max_length):
            r = 0
            for k in range(0,i):
                r = r + padded_self[k]*padded_other[i-k]
            result_coefficients.append(r)
        return Polynomial_Zq(result_coefficients)
#EXO 4
    def scalar(self, c): 
        l = len(self.coefficients)
        for i in range(l):
            self.coefficients[i] *= c
            result_coefficients = [coeff % q for coeff in coefficients]
        return Polynomial_Zq(result_coefficients)

    def rescale(self, r):
        new_coefficients = [coeff % r for coeff in coefficients]
        return Polynomial_Zq(new_coefficients)
        
    def evaluer(self,a):
        r = 0
        for i in range(len(self.coefficients)):
            r = r + self.coefficients[i]*(a**i)
        return r
            
    def fscalar(self,r,alpha):
        Q_coefficients = []
        for i in range(self.n):
            Q_coefficients.append(round(self.evaluer(i)*alpha)%r)
        return Polynomial_Zq(Q_coefficients)

#test 
A=Polynomial_Zq([8,7,2,7,4,1],3,5)
print(str(A)) # it works

    