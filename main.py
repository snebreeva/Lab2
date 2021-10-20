import decimal
from math import factorial

def pi(n):
  decimal.getcontext().prec = n + 1
  p = 0
  k = 0
  x = 426880 * decimal.Decimal('10005').sqrt()
  a = factorial(6 * p)
  b = 545140134 * p + 13591409
  d = a * b
  c = factorial(3 * p)
  f = factorial(p) ** 3
  e = (-262537412640768000) ** p
  y = decimal.Decimal(c * f * e)
  k += d / y
  return print(x / k)
