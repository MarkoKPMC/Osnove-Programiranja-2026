# PROGRAM 1
broj = eval(input("Unesite broj: "))
print(broj, broj * 2, broj * 3, broj * 4, broj * 5, sep="---")

# PROGRAM 2
userInput = eval(input('Unesite vrednost u kilogramima: '))
conversion = userInput * 2.2
print("Konacna konverzija iz kilograma u funte je: ", conversion)

# PROGRAM 3
broj1 = eval(input('Unesite prvi broj: '))
broj2 = eval(input('Unesite drugi broj: '))
broj3 = eval(input('Unesite treci broj: '))

total = broj1 + broj2 + broj3
prosek = total / 3

print("Total: ", total)
print("Prosek: ", prosek)

# PROGRAM 4
iznos = eval(input('Unesite iznos vašeg računa: '))
baksis = eval(input('Unesite koliko želite da ostavite bakšiš (u %): '))
racunBaksis = (iznos * baksis) / 100

total = racunBaksis + iznos
print("Konacan iznos svega bi bilo: ", total)
