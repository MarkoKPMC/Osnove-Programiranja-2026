from random import randint, shuffle

# ZADATAK 1
# PRVI DEO - DODAVANJE FUNKCIJA
lista = {}
brojevi = "1234567890"

while True:
    ime = input("Unesite ime tima (unesite EXIT da izadjete iz programa!): ")
    if ime.lower() == "exit":
        break
    elif ime not in lista:
        stats = input("\nUnesite broj pobeda i poraza,\nKoristite / da bi ste podelili pobede i poraze!\nExample: 10/5 (pobede/porazi)\nVas unos: ")
        
        if "/" in stats:
            razmak = stats.index("/")
            w, l = stats[:razmak].replace(" ", ""), stats[razmak + 1:].replace(" ", "")

            Flag = False
            for x in range(len(w)):
                if not Flag:
                    if brojevi.count(w[x]) == 0:
                        flag = True
                        break
                else:
                    break

            for y in range(len(l)):
                if not Flag:
                    if brojevi.count(l[y]) == 0:
                        flag = True
                        break
                else:
                    break

            if not Flag:
                lista[ime] = [int(w), int(l)]
                print("Uspesno ste uneli tim u recnik!", end="\n\n")
            else:
                print("Napravili ste gresku u unosu! Pokusajte ponovo.", end="\n\n")
        else:
            print("Napravili ste gresku u unosu! Pokusajte ponovo.", end="\n\n")

            
    else:
        print("Tim sa tim imenom vec postoji u programu!", end="\n\n")

# DRUGI DEO - SEARCH FUNCKIJA
while True:
    ime = input("Unesite ime tima koji zelite da vidite\nUnesite LIST ako zelite da vidime sve timove\nUnesite EXIT da izadjete iz programa!\nVas input: ")
    if ime.lower() == "exit":
        break
    elif ime.lower() == "list":
        if len(lista) == 0:
            print("Nema ni jednog tima u listi!")
        else:
            i = 1
            
            print("\n* Svi timovi u recniku:", "------------------------------", sep="\n")
            for t in lista:
                print(i, ". ", t, sep="")
            print("------------------------------", end="\n\n")
    elif ime in lista:
        calc = round((lista[ime][0] / sum(lista[ime])) * 100, 1)
        print("\nProsecan procenat pobeda tima ", ime, " je: ", calc, "%.",sep="", end="\n\n")
    else:
        print("Tim sa ovim imenom ne postoji u recnkiu! Pokusajte ponovo.", end="\n\n")

# TRECI DEO - LISTA SAMO SA POBEDAMA
pobede = list(lista.items())
pobede = [i[1][0] for i in pobede]
print("\nLista samo sa pobedama iz recnika:", pobede)

# CETVRI DEO - LISTA GDE SU TIMOVI KOJI IMAJU VISE POBEDA NEGO GUBITAKA
plustimovi = list(lista.items())
plustimovi = [i[0] for i in plustimovi if i[1][0] > i[1][1]]
print("\nLista timova koji imaju vise pobeda nego gubitaka:", plustimovi)

# ZADATAK 2
brojevi = "1234567890"
scores = {}
while True:
    unos = input("Unesite rezultate utakmice\nEXAMPLE: tim1 golovi - tim2 golovi\nUnesite EXIT kako biste izasli iz programa!\nVas unos: ")
    if unos.lower() == "exit":
        break

    words = unos.split()    
    if len(words) > 4:
        # DOBIJANJE REZULTATA
        score = [["",  -1], ["", -1]]
        tim = 0
        for word in words:
            Flag = False
            if word != "-" and word != " ":
                for i in range(len(word)):
                    if brojevi.count(word[i]) == 0:
                        Flag = True
                        break

                if Flag:
                    if score[tim][0] == "":
                        score[tim][0] = word
                    else:
                        score[tim][0] = score[tim][0] + " " + word
                else:
                    if score[tim][1] == -1:
                        score[tim][1] = int(word)
            elif word == "-":
                tim += 1
                
        # PROVERA (ZA RECNIK)
        Flag2 = False
        for tim in score:
            if tim[0] not in scores and tim[0] != "":
                scores[tim[0]] = [0, 0]
            elif tim[0] == "":
                Flag2 = True

        # PROVERA REZULTATA
        if not Flag2:
            if score[0][1] > score[1][1]:
                scores[score[0][0]][0] += 1
                scores[score[1][0]][1] += 1
            else:
                scores[score[0][0]][1] += 1
                scores[score[1][0]][0] += 1

            print("Unos je uspesno unesen u program!", end="\n\n")
        else:
            print("Vas unos je bio neuspesan, niste uneli sve podatke!", end="\n\n")
    else:
        print("Vas unos je bio neuspesan, niste uneli sve podatke!", end="\n\n")

# KRAJ PROGRAMA
print(scores)

# ZADATAK 3
lista = []
recnik = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
}

# KREIRANJE LISTE 5x5
for i in range(25):
    lista.append(randint(1, 5))

# UNOSENJE U RECNIK
for i in range(5):
    recnik[str(i + 1)] = lista.count(i + 1)

# SORTIRANJE
sortList = list(recnik.items())
sortList = [(i[1], i[0]) for i in sortList]
sortList.sort()

for i in range(2):
    sortList.pop(i)
    
print("Tabela:", lista, "\nRecnik:", recnik, "\n3 broja sa najvise ponavljanja:", [i[1] for i in sortList])

# ZADATAK 4
spil = [{'vrednost':i, 'boja':c}
        for c in ['pik', 'tref', 'herc', 'karo']
        for i in range(2, 15)]

shuffle(spil)
spil1, spil2 = [], []
for i in range(3):
    spil1.append(spil[randint(0, len(spil) - 1)])
    spil2.append(spil[randint(0, len(spil) - 1)])

print(spil1, spil2)
curRound = 0
while curRound != 3:
    print("Igrac 1:", spil1[curRound]['vrednost'], "Igrac 2:", spil1[curRound]['vrednost'])
    if spil1[curRound]['vrednost'] > spil2[curRound]['vrednost']:
        print("Igrac 1 je pobedio!")
        break
    elif spil1[curRound]['vrednost'] < spil2[curRound]['vrednost']:
        print("Igrac 2  je pobedio!")
        break
    else:
        curRound += 1
        print("Nereseno, sledeca runda!")
        if curRound == 3:
            print("Nereseno je!")
