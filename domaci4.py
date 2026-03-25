from random import randint
import math

# IF STATEMENT - ZADACI
# ZADATAK 1
n = eval(input('Unesite godinu: '))
if n % 4 == 0 and not (n % 400 == 0 and n % 100 != 0):
    print('Godina je prestupna!')
else:
    print('Godina nije prestupna!')

# ZADATAK 2
n = eval(input('Unesite bilo koji broj: '))
for i in range(1, n+1):
    if n % i == 0:
        print(n, 'je deljiv je broj sa:', i)

# ZADATAK 3
print("# ================= # ================= #")
print("#        The Multiplication Game        #")
print("# ================= # ================= #")

tacno, netacno = 0, 0
for i in range(10):
    x, y = randint(1, 10), randint(1, 10)
    result = x * y

    print('Tacno:', tacno, 'Netacno:', netacno, end='\n\n')
    print('Izracunaj:',x,"*",y)
    n = eval(input('Unesite vas odgovor: '))

    if n == result:
        print("Odgovor je tacan!")
        tacno += 1
    else:
        print("Odgover je netacan! Tacan odgovor je bio:", result)
        netacno += 1

    print("# ================= # ================= #")

print(" ")
print("# ================= # ================= #")
print("#            KONACAN REZULTAT           #")
print("# ================= # ================= #")
print("=> Tacno:", tacno)
print("=> Netacno:", netacno, end="\n\n")
print("Ako zelite da igrate ponovo, molim vas pokrenite program opet!")
print("# ================= # ================= #")

# ZADATAK 4
s = eval(input('Unesite broj sati (1 - 12): '))
t = eval(input('AM (1) ili PM (2): '))
u = eval(input('Za koliko unapred zelite da pomerite sat: '))

if (s >= 1 and s <= 12) and (t == 1 or t == 2):
    x = s + u
    
    if x > 12:
        x = x % 12
        if x == 0:
            x = 12
            
    if t == 1:
        if s + u >= 12:
            print(x, "PM")
        else:
            print(x, "AM")
    else:
        if s + u >= 12:
            print(x, "AM")
        else:
            print(x, "PM")
else:
    if s < 1 or s > 12:
        print("Glavni uneti broj sati je van range-a (1 - 12)")
    elif t != 1 and t != 2:
        print("Invalid argument! Pokrenite program opet!")
    
# ALGORITMI SA BROJEVIMA - ZADACI
# ZADATAK 1
n = 0
for i in range(2, 1001):
    if (i ** 1/2) % 1 == 0 and (i ** 1/3) % 1 == 0 and (i ** 1/5) % 1 == 0:
        n += 1

print("Konacan broj:", n)

# ZADATAK 2
l = []
for i in range(10):
    n = eval(input('Unesite broj poena (1 - 100): '))

    if n > 100:
        print('Uneta je vrednost veca od 100!')
    else:
        l.append(n)

najveca, najmanja = 0, 0
prosecan = 0

for x in l:
    if najmanja == 0:
        najmanja = x
    elif najmanja > x:
        najmanja = x

    if najveca == 0:
        najveca = x
    elif najveca < x:
        najveca = x

    prosecan += x

print('Najveci broj poena je:', najveca)
print('Najmanji broj poena je:', najmanja)
print('Prosecan broj poena je:', prosecan // len(l))

for y in range(2):
    prosecan -= y
    l.pop(y)
    
print('Prosecan broj poena bez najmanje 2 vrednosti je:', prosecan // len(l))

# ZADATAK 3
n = eval(input('Unesite broj koji zelite da izracunate faktorijel: '))
x = 1
for i in range(1, n+1):
    x *= i

print("Faktorijel broja", n, "je:", x)
