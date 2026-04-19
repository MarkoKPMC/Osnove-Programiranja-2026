from random import randint

# ZADATAK 1
l = [0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0
]

i = 0
while i != 10:
    r = randint(0, len(l) - 1)

    if l[r] != 1:
        l[r] = 1
        i += 1

print("Koncana lista:")
print(l)

# ZADATAK 2
l = [1, 1, 1, 1, 0, 1, 1]

for i in range(len(l)):
    if l[i] == 0:
        l[i] = 1

        print("Index prve nule u listi:", i)
        break
else:
    print("Nema ni jedna 0 u datoj listi!")

print(l)

# ZADATAK 3
kompjuter_score = 0
igrac_score = 0

print("* ================================== *",
      "  ->  Rock, Paper, Scissors Game  <-",
      "   Prvi ko dodje do 3 je pobednik!",
      "* ================================== *",
      "         Made by: Marko Kocic",
      sep="\n", end="\n\n")

potezi = ["papir", "kamen", "makaze"]
result = ""
while True:
    print("Izaberite jedan od 3 opcije: ", end="")
    for e in potezi:
        if potezi[-1] == e:
            print(e, end="\n")
        else:
            print(e, ",", sep="", end=" ")
        
    user_input = input("Vas potez: ").lower()
    if user_input in potezi:
        komp_input = potezi[randint(0, len(potezi) - 1)]

        # Result Check
        if user_input == "papir":
            if komp_input == "papir":
                result = "Tie"
            elif komp_input == "kamen":
                result = "Win"
            else:
                result = "Lose"
                
        elif user_input == "kamen":
            if komp_input == "kamen":
                result = "Tie"
            elif komp_input == "papir":
                result = "Lose"
            else:
                result = "Win"
                
        elif user_input == "makaze":
            if komp_input == "makaze":
                result = "Tie"
            elif komp_input == "kamen":
                result = "Lose"
            else:
                result = "Win"

        # Handling Results
        print("\nPotez Igraca:", user_input, "| Potez Kompjutera:", komp_input)
        if result == "Tie":
            print("* ======= * TIE! * ======= *\n",
                    "Trenutan score:\n",
                    "Kompjuter: ", kompjuter_score, " | Igrac: ", igrac_score, "\n",
                    "* ======= * TIE! * ======= *",
                    sep="", end="\n\n")
        elif result == "Lose":
            kompjuter_score += 1
            print("* ======= * LOSE! * ======= *\n",
                    "Trenutan score:\n",
                    "Kompjuter: ", kompjuter_score, " | Igrac: ", igrac_score, "\n",
                    "* ======= * LOSE! * ======= *",
                    sep="", end="\n\n")
        elif result == "Win":
            igrac_score += 1
            print("* ======= * WIN! * ======= *\n",
                    "Trenutan score:\n",
                    "Kompjuter: ", kompjuter_score, " | Igrac: ", igrac_score, "\n",
                    "* ======= * WIN! * ======= *",
                    sep="", end="\n\n")

        # Checks
        if igrac_score == 3:
            print("* ======= * ! GAME OVER ! * ======= *\n",
                  "Congratulations, pobedili ste!\n",
                  "Pokreni program opet da bi igrao opet!",
                  "* ======= * ! GAME OVER ! * ======= *\n",
                  sep="")

            break
        elif kompjuter_score == 3:
            print("* ======= * ! GAME OVER ! * ======= *\n",
                  "Izgubili ste, nazalost!\n",
                  "Pokreni program opet da bi igrao opet!\n",
                  "* ======= * ! GAME OVER ! * ======= *\n",
                  sep="")

            break
            
    else:
        print("Uneliste opciju koja nije validna, pokusajte ponovo!", end="\n\n")

# ZADATAK 4
print("* =================================== *",
      "          THE PREDICTION GAME",
      "* =================================== *",
      "Pogodite na koju stranu ce novcic da padne, heads or tails!",
      "Igra se zavrsava kad stignete do $200 ili vise ILI ako ostanete bez para!",
      sep="\n", end="\n\n")
balance = 100
opcije = ["heads", "tails"]
while True:
    print("CURRENT BALANCE: $", balance, sep="")
    user_input = input("Heads or Tails: ").lower()

    landed = opcije[randint(0, len(opcije) - 1)]
    if user_input in opcije:
        if user_input == landed:
            print("Pogodili ste na koju stranu je novic pao!")
            balance += 9
        else:
            print("Pogresan odgovor!")
            balance -= 10

        if balance <= 0:
            print("BANKRUPT! Ostali ste bez para nazalost!")
            break
        elif balance >= 200:
            print("CONGRATS! Stigli ste do >$200, igra je zavrsena!")
            break
    else:
        print("Invalid opcija, pokusajte ponovo!")

print("Pokrenite program opet da bi ste igrali opet!")

# ZADATAK 5
l = []
for i in range(36):
    s = randint(0, 1)

    if s == 1:
        if l.count(1) != 12:
            l.append(1)
        else:
            l.append(0)
    else:
        l.append(0)

print(l)

# ZADATAK 6
# Nisam uspesno mogao da pokrenem program do kraja...
l = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

row, index = 0, 0
count = 0
while count != 72:
    check = False
    r = randint(1, 9)

    if l[row].count(r) == 0:
        for l2 in l:
            if l2[index] == r:
                check = True
                
        if not check:
            l[row][index] = r

            if l[row].count(0) == 0:
                print("Row ", row + 1, ": ", l[row], sep="")
                
                row += 1
                index = 0
            else:
                index += 1

            count += 1
