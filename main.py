from decimal import Decimal as de
from decimal import *

n = int(input())
getcontext().prec = n + 1

def pink(n):
    p = de(13591409)
    ak = de(1)
    k = 1
    while k < n:
        ak *= -de((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / de(k * k * k * 26680 * 640320 * 640320)

        val = ak * (13591409 + 545140134 * k)

        d = de((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / de(k * k * k * 26680 * 640320 * 640320)

        p += val
        k += 1
    p = p * de(10005).sqrt() / 4270934400
    p = p ** (-1)
    return p

print(pink(n))
