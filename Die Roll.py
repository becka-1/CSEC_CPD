from fractions import Fraction

a, b = map(int, input().split())
x = Fraction(6-(max(a,b)-1), 6)
print(f"{x.numerator}/{x.denominator}")
