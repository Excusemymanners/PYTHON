from functools import reduce
from datetime import datetime

print("=" * 60)
print("LAB 3 - Functii - Toate exercitiile")
print("=" * 60)

# -------------------------------------------------------
# EX 1: Rock-Paper-Scissors (vezi lab3.py)
# -------------------------------------------------------
print("\n--- EX 1: Rock-Paper-Scissors - vezi lab3.py ---")

# -------------------------------------------------------
# EX 2: Factura cu **kwargs (vezi lab3ex2.py)
# -------------------------------------------------------
print("\n--- EX 2: Factura - vezi lab3ex2.py ---")

# -------------------------------------------------------
# EX 3: Normalizare date (vezi lab3ex3.py)
# -------------------------------------------------------
print("\n--- EX 3: Normalizare - vezi lab3ex3.py ---")

# -------------------------------------------------------
# EX 4: Lambda - lista ridicata la patrat
# -------------------------------------------------------
print("\n--- EX 4: Lambda patrat ---")
my_list = [1, 2, 3]
squared = list(map(lambda x: x ** 2, my_list))
print(f"Input:  {my_list}")
print(f"Output: {squared}")

my_list2 = [1, 2, 3, 4, 5]
squared2 = list(map(lambda x: x ** 2, my_list2))
print(f"Input:  {my_list2}")
print(f"Output: {squared2}")

# -------------------------------------------------------
# EX 5: Sortare lista de tupluri dupa a 2-a valoare
# -------------------------------------------------------
print("\n--- EX 5: Sortare tupluri dupa a 2-a valoare ---")
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print(f"Original: {a}")
print(f"Sortat:   {sorted_a}")

# -------------------------------------------------------
# EX 6: Filter numere pare si impare cu lambda
# -------------------------------------------------------
print("\n--- EX 6: Filter pare si impare ---")
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list  = list(filter(lambda x: x % 2 != 0, orig_list))
print(f"Original:  {orig_list}")
print(f"Pare:      {even_list}")
print(f"Impare:    {odd_list}")

# -------------------------------------------------------
# EX 7: Filter None + map reducere 10%
# -------------------------------------------------------
print("\n--- EX 7: Filter None + reducere 10% ---")
preturi = [100, None, 250, None, 80, 320, None, 45]
preturi_valide   = list(filter(lambda x: x is not None, preturi))
preturi_reduse   = list(map(lambda x: round(x * 0.9, 2), preturi_valide))
print(f"Preturi originale: {preturi}")
print(f"Fara None:         {preturi_valide}")
print(f"Dupa reducere 10%: {preturi_reduse}")

# -------------------------------------------------------
# EX 8: Lambda - extragere an, luna, zi, ora din datetime
# -------------------------------------------------------
print("\n--- EX 8: Lambda extragere data/ora ---")
dt = datetime(2023, 4, 24, 9, 3, 32, 744178)
print(f"Datetime: {dt}")

get_year   = lambda d: str(d.year)
get_month  = lambda d: str(d.month).zfill(2)
get_day    = lambda d: str(d.day).zfill(2)
get_time   = lambda d: f"{str(d.hour).zfill(2)}:{str(d.minute).zfill(2)}:{str(d.second).zfill(2)}.{d.microsecond}"

print(get_year(dt))
print(get_month(dt))
print(get_day(dt))
print(get_time(dt))

# -------------------------------------------------------
# EX 9: zip - suma elementelor corespunzatoare
# -------------------------------------------------------
print("\n--- EX 9: zip - suma listelor ---")

def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = sum_lists(list1, list2)
print(f"list1:  {list1}")
print(f"list2:  {list2}")
print(f"Suma:   {result}")

# -------------------------------------------------------
# EX 10: List Comprehension
# -------------------------------------------------------
print("\n--- EX 10: List Comprehension ---")

# Numere pare 0-100
pare_100 = [x for x in range(0, 101) if x % 2 == 0]
print(f"Pare 0-100: {pare_100}")

# Cuburile primelor 10 numere intregi
cuburi = [x ** 3 for x in range(1, 11)]
print(f"Cuburi 1-10: {cuburi}")

# Elemente comune din doua liste
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
comune = [x for x in lista_a if x in lista_b]
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Comune:  {comune}")

# -------------------------------------------------------
# EX 11: Set Comprehension
# -------------------------------------------------------
print("\n--- EX 11: Set Comprehension ---")

# Primele 10 numere pare
prime_10_pare = {x for x in range(2, 21, 2)}
print(f"Primele 10 numere pare: {sorted(prime_10_pare)}")

# Litere distincte dintr-un string
text = "hello world python"
litere_distincte = {c for c in text if c != ' '}
print(f"Litere distincte din '{text}': {sorted(litere_distincte)}")

# Cuvinte cu cel putin 5 litere
propozitie = "programming in python is very interesting and fun"
cuvinte_lungi = {w for w in propozitie.split() if len(w) >= 5}
print(f"Cuvinte >= 5 litere: {cuvinte_lungi}")

# -------------------------------------------------------
# EX 12: Dictionary Comprehension
# -------------------------------------------------------
print("\n--- EX 12: Dictionary Comprehension ---")

# Numere 1-10 cu patratele lor
patrate = {x: x ** 2 for x in range(1, 11)}
print(f"Patrate 1-10: {patrate}")

# Litere cu numarul de aparitii
sir = "mississippi"
aparitii = {c: sir.count(c) for c in set(sir)}
print(f"Aparitii in '{sir}': {aparitii}")

# Numere 1-10 cu lista de divizori
def divizori(n):
    return [i for i in range(1, n + 1) if n % i == 0]

div_dict = {n: divizori(n) for n in range(1, 11)}
print("Divizori 1-10:")
for k, v in div_dict.items():
    print(f"  {k}: {v}")

print("\n" + "=" * 60)
print("TOATE EXERCITIILE LAB 3 COMPLETE!")
print("=" * 60)
