from random import randint

# ZADATAK 1 (13.5)
def digitalni_koren(n = 45893):
    while len(str(n)) != 1:
        t = [int(i) for i in str(n)]
        n = sum(t)

    return n

# ZADATAK 2 (13.6)
def prva_razlika(s1 = "123", s2 = "456"):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return i
    else:
        return -1

# ZADATAK 3 (13.7)
def faktorijel(n):
    l = 1
    for i in range(n, 0, -1):
        l *= i
    return l
        
def binom(n = 3, k = 2):
    return round(faktorijel(n) / (faktorijel(k) * faktorijel(n - k)), 2)
    

# ZADATAK 4 (13.8)
def slucajan_broj(n = 3):
    s = ""
    while len(s) != n:
        r = randint(0, 9)
        if (r == 0 and len(s) != 0) or r != 0:
            s += str(r)

        print(r, s, len(s))

    return int(s)

# ZADATAK 5 (13.9)
def broj_faktora(n = 12):
    return len(faktori(n))

# ZADATAK 6 (13.10)
def faktori(n = 12):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)

    return l

# ZADATAK 7 (13.11)
def najblizi(l = [1, 6, 3, 9, 11], a = 8):
    l.sort()
    h = 0
    for e in l:
        if e <= a:
            h = e

    return h

# ZADATAK 8 (13.12)
def broj_poklapanja(s1 = "python", s2 = "path"):
    n = 0

    if len(s1) > len(s2):
        n = len(s2)
    elif len(s1) < len(s2):
        n = len(s1)
    else:
        n = len(s1)

    c = 0
    for i in range(n):
        if s1[i] == s2[i]:
            c += 1

    return c

# ZADATAK 9 (13.13)
def findall(s = "hi", l = "i"):
    index = [i for i in range(len(s)) if s[i] == l]
    return index

# ZADATAK 10 (13.14)
def promeni_velicinu(s = "Hello World!"):
    new = ""
    for el in s:
        if el == el.upper():
            new += el.lower()
        else:
            new += el.upper()

    return new

# ZADATAK 11 (13.15)
def is_sorted(l = [1, 2, 3, 5, 4, 6]):
    copy = list(l)
    copy.sort()

    return (l == copy)

# ZADATAK 12 (13.16)
def root(x = 4, n = 2):
    '''x <- Broj koji hocete da korenujete, n <- Na koj broj da bude koren'''
    return (x ** (1 / n))

# ZADATAK 13 (13.17)
def one_away(s1 = "bike", s2 = "hike"):
    if len(s1) != len(s2):
        return False

    c = [s1[i] for i in range(len(s1)) if s1[i] != s2[i]]
    if len(c) != 1:
        return False
    else:
        return True

# ZADATAK 14 (13.18)
def primes(n = 100):
    l = []
    for x in range(2, n):
        c = 0
        for y in range(1, x):
            if x % y == 0:
                c += 1

        if c == 1:
            l.append(x)

    return l
