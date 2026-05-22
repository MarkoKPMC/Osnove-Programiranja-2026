from random import shuffle, randint
# ZADATAK 1 (10.10)
spil = [{'vrednost':i, 'boja':c}
        for c in ['pik', 'tref', 'herc', 'karo']
        for i in range(2, 15)]

shuffle(spil)
ponavljanja = 100
uspeh, neuspeh = 0, 0
for x in range(ponavljanja):
    l = []
    for y in range(5):
        l.append(spil[randint(0, len(spil) - 1)])

    l = [e['boja'] for e in l]
    s = set(l)

    for boja in s:
        if l.count(boja) >= 3:
            uspeh += 1
            break
    else:
        neuspeh += 1

print("Verovatnoca da su od 5 karata 3 karte istih boja iz ", ponavljanja, " ponavljanja je: ", str((uspeh / ponavljanja) * 100), "%.",sep="")
print("Broj uspeha:", uspeh, "| Broj neuspeha:", neuspeh)

# pik pik pik herc karo
# pik herc karo

# ZADATAK 2 (10.11)
u1 = input('Unesite bilo koji string: ')
u2 = input('Unesite sifriranu verziju istog string-a: ')

l1, l2 = list(u1), list(u2)
if len(l1) == len(l2):
    last1, last2 = "", ""
    for i in range(len(l1)):
        if l1[i] == l2[i] and l1[i] != "":
            print("Uneliste invalidan string i sifriranu verziju stringa. Pokusajte ponovo.")
            break
        elif (last1 == l1[i] and last2 != l2[i]) or (last1 != l1[i] and last2 == l2[i]):
            print("Uneliste invalidan string i sifriranu verziju stringa. Pokusajte ponovo.")
            break
        else:
            last1, last2 = l1[i], l2[i]
    else:
        print("Unesena sifriranu verziju stringa je validan!")
else:
    print("Oba stringa nisu iste duzine! Pokusajte ponovo.")
