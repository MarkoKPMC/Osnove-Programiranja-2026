# ZADATAK 1 (6.9)
n = eval(input('Unesite broj:'))
for i in range(1, n + 1):
    s = " " * i + "" + str(i)
    print(s)

# ZADATAK 2 (6.10)
s = input('Unesite text (string): ')
for c in s:
    print(c * 2)

# ZADATAK 3 (6.11)
s = input('Unesite text (string) koji sardzi slovo A:\n')

s1, s2 = '', ''
flag = False
if 'a' in s.lower():
    for i in range(len(s)):
        if not flag:
            if s[i].lower() == "a":
                flag = True
                
            s1 += s[i]
        else:
            s2 += s[i]
            
    print('Tekst do slova A:', s1)
    print('Tekst posle slova A:', s2)
else:
    print('U tekstu nema ni jedno slovo A!')

# ZADATAK 4 (6.12)
s = input('Unesite text (string): ')

final = ''
for i in range(0, len(s)):
    if (i + 1) % 2 == 0:
        final += s[i].upper()
    else:
        final += s[i].lower()

print(final)

# ZADATAK 5 (6.13)
print('UPUSTVO ZA KORISCENJE PROGRAMA:')
print('MOLIM VAS UNESITE 2 TEXT-A (STRINGS) KOJI IMAJU ISTU DUZINU TEKSTA!')
print('U SUPROTNO DOBICETE ERROR I PROGRAM CE BITI TERMINATED.', end="\n\n")
s1 = input('Unesite prvi text (string): ')
s2 = input('Unesite drugi text (string): ')

if len(s1) == len(s2):
    final = ''
    
    for i in range(len(s1)):
        final += (s1[i] + s2[i])

    print(final)
else:
    print('Tekstovi nisu iste duzine! Pokrenite program opet i pokusajte opet!')

# ZADATAK 6 (6.14)
ime = input('Unesite vase ime malim slovima: ')
prezime = input('Unesite vase prezime malim slovima: ')

if ime == ime.lower() and prezime == prezime.lower():
    ime = ime[0].upper() + ime[1:]
    prezime = prezime[0].upper() + prezime[1:]

    print(ime, prezime)
else:
    print('\nERROR:')
    print('Uneliste tekst sa nekim/svim velikim slovima. Pokrenite program opet!')

# ZADATAK 7 (6.15)
s = input('Enter your name: ')
print('\n')

ime = ''
flag = False
for c in s:
    if not flag:
        if c == " ":
            flag = True
        else:
            ime += c


print('Dear ', s, ',', sep='', end='\n\n')
print('I am pleased to offer you our new Platinum Plus Reward\n',
      'card at a special introductory APR of 47.99%. ', ime, ',\n',
      'an offer like this does not come along every day, so I\n',
      'urge you to call now toll-free at 1-800-314-1592. We\n',
      'cannot offer such a low rate for long, ', ime, ', so call\n',
      'right away.',
      sep='', end='')
