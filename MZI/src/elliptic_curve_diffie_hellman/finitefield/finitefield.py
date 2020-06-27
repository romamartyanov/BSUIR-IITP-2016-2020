import random

from .modp import *
from .polynomial import polynomialsOver


# isIrreducible: Polynomial, int -> bool
# determine if the given monic polynomial with coefficients in Z/p is
# irreducible over Z/p where p is the given integer
# Algorithm 4.69 in the Handbook of Applied Cryptography
def is_irreducible(polynomial, p):
    zmod_p = IntegersModP(p)
    if polynomial.field is not zmod_p:
        raise TypeError("Given a polynomial that's not over %s, but instead %r" %
                        (zmod_p.__name__, polynomial.field.__name__))

    poly = polynomialsOver(zmod_p).factory
    x = poly([0, 1])
    power_term = x
    is_unit = lambda p: p.degree() == 0

    for _ in range(int(polynomial.degree() / 2)):
        power_term = power_term.powmod(p, polynomial)
        gcd_over_zmodp = gcd(polynomial, power_term - x)
        if not is_unit(gcd_over_zmodp):
            return False

    return True


# generateIrreduciblePolynomial: int, int -> Polynomial
# generate a random irreducible polynomial of a given degree over Z/p, where p
# is given by the integer 'modulus'. This algorithm is expected to terminate
# after 'degree' many irreducilibity tests. By Chernoff bounds the probability
# it deviates from this by very much is exponentially small.
def generate_irreducible_polynomial(modulus, degree):
    Zp = IntegersModP(modulus)
    polynomial = polynomialsOver(Zp)

    while True:
        coefficients = [Zp(random.randint(0, modulus - 1)) for _ in range(degree)]
        random_monic_polynomial = polynomial(coefficients + [Zp(1)])
        print(random_monic_polynomial)

        if is_irreducible(random_monic_polynomial, modulus):
            return random_monic_polynomial


# create a type constructor for the finite field of order p^m for p prime, m >= 1
@memoize
def FiniteField(p, m, polynomial_modulus=None):
    Zp = IntegersModP(p)
    if m == 1:
        return Zp

    polynomial = polynomialsOver(Zp)
    if polynomial_modulus is None:
        polynomial_modulus = generate_irreducible_polynomial(modulus=p, degree=m)

    class Fq(FieldElement):
        fieldSize = int(p ** m)
        primeSubfield = Zp
        idealGenerator = polynomial_modulus
        operator_precedence = 3

        def __init__(self, poly):
            if type(poly) is Fq:
                self.poly = poly.poly
            elif type(poly) is int or type(poly) is Zp:
                self.poly = polynomial([Zp(poly)])
            elif isinstance(poly, polynomial):
                self.poly = poly % polynomial_modulus
            else:
                self.poly = polynomial([Zp(x) for x in poly]) % polynomial_modulus

            self.field = Fq

        @typecheck
        def __add__(self, other):
            return Fq(self.poly + other.poly)

        @typecheck
        def __sub__(self, other):
            return Fq(self.poly - other.poly)

        @typecheck
        def __mul__(self, other):
            return Fq(self.poly * other.poly)

        @typecheck
        def __eq__(self, other):
            return isinstance(other, Fq) and self.poly == other.poly

        def __pow__(self, n):
            return Fq(pow(self.poly, n))

        def __neg__(self):
            return Fq(-self.poly)

        def __abs__(self):
            return abs(self.poly)

        def __repr__(self):
            return repr(self.poly) + ' \u2208 ' + self.__class__.__name__

        @typecheck
        def __divmod__(self, divisor):
            q, r = divmod(self.poly, divisor.poly)
            return Fq(q), Fq(r)

        def inverse(self):
            if self == Fq(0):
                raise ZeroDivisionError

            x, y, d = extended_euclidean_algorithm(self.poly, self.idealGenerator)
            if d.degree() != 0:
                raise Exception('Somehow, this element has no inverse! Maybe intialized with a non-prime?')

            return Fq(x) * Fq(d.coefficients[0].inverse())

    Fq.__name__ = 'F_{%d^%d}' % (p, m)
    return Fq


if __name__ == "__main__":
    F23 = FiniteField(2, 3)
    x = F23([1, 1])

    F35 = FiniteField(3, 5)
    y = F35([1, 1, 2])
