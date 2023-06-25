import fractions
n = int(input("Введите целое число n: "))
m = int(input("Введите целое число m: "))
n1 = int(input("Введите целое число n1: "))
m1 = int(input("Введите целое число m1: "))
print(n, "/", m, sep="")
print(n1, "/", m1, sep="")
print(n * n1, "/", m*m1, sep="" )
if m == m1:
    print(n + n1, "/", m, sep="" )
elif  m*m1 % (n*m1 + n1*m) == 0:
    print(int(m*m1 / (m*m1)), "/", int(m*m1 / (n*m1 + n1*m)), sep="")
else:
    print(n*m1 + n1*m, "/", m*m1, sep="")
print()
f1 = fractions.Fraction(n, m)
print(f1)
f2 = fractions.Fraction(n1, m1)
print(f2)
print(f1 * f2)
print(f1 + f2)