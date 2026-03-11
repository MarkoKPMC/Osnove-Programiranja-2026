# ZADATAK 1
n = eval(input("Unesite broj: ")) + 1
for i in range(1, n):
    print("*"*(n - i))

# ZADATAK 2
n = 2 * eval(input("Unesite velicinu dijamanta: "))
for i in range(1, n, 2):
    x = (n - i) // 2
    print(" "*x + "*"*i)

for i in range(n - 3, 0, -2):
    x = (n - i) // 2
    print(" "*x + "*"*i)

# ZADATAK 3
n = eval(input("Unesite velicinu slova A: "))
center = (n + 1) // 2
print("Velicina:", n, "Centar:", center)
print(" " * n + "*")

for i in range(1, n - center):
    x = (i * 2)
    print(" " * (n - i) + "*" + " " * (i * 2 - 1) + "*")

if n % 2 == 0:
    print(" " * (n - center) + "*" * (center * 2 + 1))
else:
    print(" " * (n - center + 1) + "*" * (center * 2 - 1))

for i in range(n // 2, n):
    x = (i * 2 + 1)
    print(" " * (n - i - 1) + "*" + " " * x + "*")
