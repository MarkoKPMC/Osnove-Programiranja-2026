# ZADATAK 1
x = 0
for i in range(10, 1000000):
    y = str(i)[::-1]
    if str(i) == str(y):
        if i - x <= 20:
            print(x, y)

        x = i
        
# ZADATAK 2
brojevi = "1690"
for x in range(1, 1000000):
    y = str(x)[::-1]

    for z in range(len(y)):
        if brojevi.count(y[z]) == 0:
            y = y[:z] + "a" + y[z + 1:]
        elif y[z] == "6":
            y = y[:z] + "9" + y[z + 1:]
        elif y[z] == "9":
            y = y[:z] + "6" + y[z + 1:]

    if str(x) == y:
        print(x)
        
# ZADATAK 3
for i in range(1, 10000):
    x = 1
    y = 0

    for e in str(i):
        x *= int(e)
        y += int(e)

    if x + y == i:
        print(i)

# ZADATAK 5
x = 1
for i in range(1000, 0, -1):
    x *= i

nule = 0
for e in range(len(str(x))):
    if str(x)[e] == "0":
        nule += 1
    else:
        nule = 0

print("Na kraju broja 1000! ima:", nule, "nula.")

# ZADATAK 6
n = eval(input("Unesite broj inca: "))

pos = 0
for i in range(len(str(n))):
    if str(n)[i] == ".":
        pos = i
        break

if pos != 0:
    x = int(str(n)[0:pos])
    y = float(str(n)[pos:])

    print(n, "inca je u fite i incima:", x, "fita i", round(y * 12), "inca.")
else:
    print(n, "inca je u fite i incima:", n, "fita i 0 inca.")

# ZADATAK  7
pobede = []
porazi = []
brojevi = "1234567890"
while True:
    e = input("Unesite fudbalski skor (broj pobeda-broj poraza)\nUnesite KRAJ ako zelite da zavrsite unos.\n\nUnos: ")

    if e.lower() == "kraj":
        break
    elif "-" not in e:
        print("Invalid unos! Pokusajte ponovo.\n")
    else:
        razmak = e.index("-")
        w, l = e[:razmak].replace(" ", ""), e[razmak + 1:].replace(" ", "")

        print(w, l)
        flag = False
        for x in range(len(w)):
            if brojevi.count(w[x]) == 0:
                flag = True
                break
            
        for y in range(len(l)):
            if brojevi.count(l[y]) == 0:
                flag = True
                break

        if not flag:
            pobede.append(int(w))
            porazi.append(int(l))

            print("Unos je uspoosno unesen!\n")
        else:
            print("Invalid unos! Pokusajte ponovo.\n")

pobede.sort()
porazi.sort()
print("Pobede:", pobede, "\n >> Najveci broj pobeda:", pobede[-1], "\n >> Najnizi broj pobeda:", pobede[0])
print("Porazi:", porazi, "\n >> Najveci broj poraza:", porazi[-1], "\n >> Najnizi broj poraza:", porazi[0])

# ZADATAK 8
datumi = [
    [], # DANI
    [] # MESECI
]
brojevi = "0123456789"
while True:
    n = input("Unesite datum rodjenja (format: dan/mesec)\nUnesite KRAJ ako zelite da zavrsite unos.\n\nUnos: ")

    if n.lower() == "kraj":
        break
    elif "/" not in n:
        print("Invalidan unos! Pokusajte ponovo.\n")
    else:
        razmak = n.index("/")
        dan, mesec = n[:razmak].replace(" ", ""), n[razmak + 1:].replace(" ", "")

        flag = False
        for x in range(len(dan)):
            if brojevi.count(dan[x]) == 0:
                flag = True
                break

        for y in range(len(mesec)):
            if brojevi.count(mesec[y]) == 0:
                flag = True
                break

        if not flag:
            if int(mesec) <=  12  and ((int(mesec) == 2 and int(dan) <= 29) or (int(mesec) % 2 == 0 and int(dan) <= 30) or (int(mesec) % 2 != 0 and int(dan) <= 31)):
                datumi[0].append(int(dan))
                datumi[1].append(int(mesec))
                print("Unos je uspesno unesen!\n")
            else:
                print("Invalidan unos! Pokusajte ponovo.\n")
        else:
            print("Invalidan unos! Pokusajte ponovo.\n")

print("Lista datuma: ",end="")
for i in range(len(datumi[0])):
    if len(datumi[0]) == i + 1:
        print(datumi[0][i], "/", datumi[1][i],sep="", end="")
    else:
        print(datumi[0][i], "/", datumi[1][i],sep="", end=", ")
        
print("\n  >> Broj rodjendana u februaru:", datumi[1].count(2), "\n",
      " >> Broj rodjendan koji su 25-tog:", datumi[0].count(25))
