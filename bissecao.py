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
antA = x0
antB = x0
conte = 0

while(c > l or math.fabs(f(x0)) > tol):

    if(f(a) * f(x0) < 0.0):
        b = x0
        erro = antB - x0
        antB = b
        print("b: %f" % b)
        print("erro: %f" % erro)

    if(f(a) * f(x0) > 0.0):
        a = x0
        erro = antA - a
        antA = a
        print("a: %f" % a)
        print("erro: %f" % erro)


    c = b - a
    print("f(%f): %f" % (x0, f(x0)))
    print("Xn: %f" % x0)
    x0 = (a + b) / 2.0


    conte = conte + 1
    print("d: %d\n\n" % conte)
    #print("erro: %f\n\n" % erro)
    if(conte >= Max):
        break

print("\n\n\nRaiz: %f\n" % x0)
print("Interações %i\n" % conte)
print("f(%f) = %f" % (x0, f(x0)))


