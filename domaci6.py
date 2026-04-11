import random

# ZADATAK 1
l = []
for i in range(10000):
    x, y = random.randint(1, 6), random.randint(1, 6)
    l.append(x + y)
    

print('Verovatnoca za bacanje dve kocke')
for i in range(1, 12):
    
    n = l.count(i + 1)
    v = round((n / 10000) * 100)

    print(i + 1, " (", n, ") -> ", v, "%", sep="")
    
# ZADATAK 2
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = []

for i in range(len(l1)):
    if l1[i] == l1[-1]:
        l2.insert(0, l1[i])
    else:
        l2.append(l1[i])

print(l2)

# ZADATAK 3
l = [1]
for i in range(11):
    l += i * [0]
    l.append(1)

print(l)

# ZADATAK 4
l = [1]
for i in range(100):
    l.append(random.randint(0, 1))

naj, cur = 0, 0
for e in l:
    if e == 0:
        cur += 1
    else:
        if cur > naj:
            naj = cur

        cur = 0

print('Najduzi uzastopni niz nula u listi je bio:', naj)
print(l)

# ZADATAK 5
l = [1, 1, 2, 3, 4, 3, 0, 0]
f = []

print(l)
for e in l:
    if f.count(e) == 0:
        f.append(e)
        
print(f)

# ZADATAK 6

# OPCIJE -> ZA PRINT
o = [
    "Yard (yd)",
    "Miles (mi)",
    "Milimeters (mm)",
    "Centimeters (cm)",
    "Meters (m)",
    "Kilometers (km)"
]

# ZA KONVERZACIJU BROJEVI
l = [
    0.3333333333,
    0.0001893939,
    304.8,
    30.48,
    0.3048,
    0.0003048
]

x = eval(input("Unesite duzinu u feet (ft): "))
print("Izaberite koju duzinu zelite da konvertujete u:")

for i in range(len(o)):
    print(i + 1, " -> ", o[i], sep="")
print("")

y = eval(input("Unesite broj zeljene jedinice: "))
if len(o) >= y - 1:
    f = x * l[y - 1]
    print('Konacna konverzija: Feet (ft) -> ', o[y - 1], ' je: ', f,sep="")
