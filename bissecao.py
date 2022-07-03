import math
import numpy as np

def f(x):
    return (0.2 * math.pow(x, 3) - 3.006 * math.pow(x, 2) + 15.06 * x - 25.15)


a = float(input("[a, b] (a): "))
b = float(input("[a, b] (b): "))

l = 0.001
tol = 0.0001
conte = 0
Max = 100
c = b - a

x0 = (a + b) / 2.0
antB = 0
antA = 0

while(c > l or math.fabs(f(x0)) > tol):

    if(f(a) * f(x0) < 0.0):
        b = x0
        erro = antB - b
        antB = b
        print("b: %f" % b)

    if(f(a) * f(x0) > 0.0):
        a = x0
        erro = antA - a
        antA = a
        print("a: %f" % a)


    c = b - a
    x0 = (a + b) / 2.0
    print("Xn: %f" % x0)
    print("f(x): %f" % c)

    conte = conte + 1
    print("d: %d\n\n" % conte)
    #print("erro: %f\n\n" % erro)
    if(conte >= Max):
        break

print("\n\n\nRaiz: %f\n" % x0)
print("Interações %i\n" % conte)
print("f(%f) = %f" % (x0, f(x0)))