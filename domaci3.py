from random import randint
import math

# ZADATAK 1
n = eval(input("Unesite godinu [mora biti veca od 1600-te]: "))

x1 = (n // 4) - (1599 // 4)
x2 = (n // 100) - (1599 // 100)
x3 = (n // 400) - (1599 // 400)
x = x1 - x2 + x3

print("Od 1600 do",n,"je bilo:",x,"prestupnih godina!")
        
# ZADATAK 2
x = eval(input("Unesite sirinu modularnog pravougaonika: "))
y = eval(input("Unesite visinu modularnog pravougaonika: "))

z = -1
for i in range(y):
    for n in range(x + 1):
        z = (z + 1) % 10
        print(z ,end=' ')

    print('', end='\n')
    
# ZADATAK 3
parni = 0
neparni = 0

printNums = False
for i in range(20):
    x = randint(1, 100)

    if x % 2 == 0:
        parni += 1

        if printNums == True:
            print("[",i,"]",x,"-> Paran Broj")
    else:
        neparni += 1

        if printNums == True:
            print("[",i,"]",x,"-> Neparan Broj")

print("Broj parnih brojeva:",parni)
print("Broj neparnih brojeva:",neparni)

# ZADATAK 4
n = eval(input("Unesite koliko brojeva zelite da generiste: "))

t = 0
printNums = False
for i in range(n):
    x = randint(1, 10)
    t += x

    if printNums == True:
        print("[",i,"]",x)

print("Total svih brojeva je:", t)
print("Prosecna vrednost svih brojeva je:",t/n)

# ZADATAK 5
n = eval(input("Unesite bilo koji broj po zelji: "))
t = str(n)

x = 0
for i in range(len(t), 0, -1):
    y = n % 10
    n = n // 10
    x += y

print(x)

# ZADATAK 6
# BROJ PONAVLJANJA
x = 10

for i in range(x):
    y = randint(100, 999)
    
    n = ((10 ** 3) -1) // (10 - 1)
    n = n * (y % 10)

    if y == n:
        print("[",i,"]",y,"-> DA")
    else:
        print("[",i,"]",y,"-> NE")

# ZADATAK 7
n = eval(input("Unesite do kog broja da ide program: "))
for i in range(1, n + 1):
    print(i,"->",i**2,",",i**3)
