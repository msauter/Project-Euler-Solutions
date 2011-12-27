#Problem 33
#20 December 2002
#The fraction 49 / 98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49 / 98 = 4 / 8 ,
# which is correct, is obtained by cancelling the 9s.  We shall consider
# fractions like, 30 / 50 = 3 / 5 , to be trivial examples.  There are exactly
# four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.  If the product o
#f these four fractions is given in its lowest common terms, find the value of
# the denominator.
#
#----------

from fractions import Fraction

prod = 1

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				frac = Fraction((a * 10 + b), (c * 10 + d))
				if frac < 1 and (frac == Fraction(a, d) or frac == Fraction(b, c)) and (a == d or b == c):
					print (a * 10 + b), (c * 10 + d), frac
					prod = prod * frac
					
print Fraction(prod)