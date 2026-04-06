from itertools import chain

def faktorisiere(n):
    if n == 0: return     # verhindert Endlosschleife 
    l = []  # Lösungsmenge
    # Auf Teilbarkeit durch 2, und alle ungeraden Zahlen von 3..sqrt(n) testen
    for i in chain([2], range(3, n//2 + 1, 2)):
        # Ein Teiler kann mehrfach vorkommen (z.B. 4 = 2 * 2), deswegen:
        while n % i == 0:
            l.append(i)
            n = n // i  # "//" ist ganzzahlige Division und entspricht int(n/i)
        if i*i > n:  # Alle Teiler gefunden? Dann Abbruch.
            if n > 1:
                l.append (n)
            break
    return l

# findet t in N um die Subtraktion von t minus Fsum(REF) auszugeben
def findSUM(N, REF, t):
    for k, item in enumerate(N):
        if item == t:
            r = t - REF[k]
            return r

Nx = []         # Natürliche Zahlen liste
SUMSF = []      # zugehörige Factorial Summen
L3 = []         # Liste für n minus fsum Ergebnisse
ERGEBNISSE = {} # dict für alle weiteren Subtraktions-Ergebnisse (Plot Matrix)
LEnum = 1       # Durchlaufzähler
interationen = 10000

for x in range(interationen):
    Nx.append(x+1)
    s = sum(faktorisiere(x+1))
    SUMSF.append(s)

for k, f in enumerate(SUMSF):
    sub = Nx[k] - f
    L3.append(sub)

summe = 1
Li = L3 # liste zu interieren ist aufsteigend in ERGEBNISSE[LEnum - 1]
while summe != 0: #
    ERGEBNISSE[LEnum] = []
    for k, item in enumerate(Li):
        if item == 1: ERGEBNISSE[LEnum].append(0)
        elif item == 0: ERGEBNISSE[LEnum].append(0)
        else: ERGEBNISSE[LEnum].append(findSUM(Nx, SUMSF, item))
    summe = sum(ERGEBNISSE[LEnum])
    Li = ERGEBNISSE[LEnum]
    if 0 <= summe <= 15: break
    LEnum += 1

print('Die Summe der letzten Ergebnisse liegt zwischen 0 und 15')
print('Anzahl der Durchläufe SUMME gegen Null:', LEnum)


        

