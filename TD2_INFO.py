from math import gcd
# EXO 1 & 2
# Nous voulons représenter des fractions.
# Définir la classe Fraction permettant de créer et d’afficher des fractions
# Étendre cette classe pour offrir les méthodes add, mult et simplify
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def mult(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        new_numerator = self.numerator // common_divisor
        new_denominator = self.denominator // common_divisor
        return Fraction(new_numerator, new_denominator)

# Fractions de test
fraction1 = Fraction(3, 4)
fraction2 = Fraction(2, 3)

# Test add
result_add = fraction1.add(fraction2)
assert str(result_add) == "17 / 12"

# Test mult
result_mult = fraction1.mult(fraction2)
assert str(result_mult) == "6 / 12"

# Test simplify
fraction3 = Fraction(6, 8)
result_simplify = fraction3.simplify()
assert str(result_simplify) == "3 / 4"

print("Tous les tests ont été validés (fractions)")


# EXO 3
def H(n):
    total = Fraction(0, 1)
    for i in range(1, n+1):
        total = total.add(Fraction(1, i))
    return total

h1000 = H(1000)
print("H(1000) sous forme de fraction:", h1000)
    
# EXO 4
def leibniz(n):
    total = Fraction(0, 1)
    for i in range(0, n):
        total = total.add(Fraction((-1)^i, 2*i + 1))
    return total
    
leibniz1000 = leibniz(1000)
print("Approximation de pi/4 avec la formule de Leibniz pour n=1000 sous forme de fraction:", leibniz1000)

#pour n = 10000 j'ai un problème de limite d'entiers dans la mémoire donc j'ai tout fait avec 1000 les codes fonctionnent

# EXO 5
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

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

    def add(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_length - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_length - len(other.coefficients))
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

# Tests
polynomial1 = Polynomial([1, 0, 1])  
polynomial2 = Polynomial([0, 3, 4]) 

# Test add
result_add = polynomial1.add(polynomial2)
assert str(result_add) == "X**2 + 3*X + 5"

print("Tous les tests ont été validés (polynômes)")

            



   
        