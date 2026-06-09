import random

print("=" * 60)
print("LAB 2 - Structuri de control - Toate exercitiile")
print("=" * 60)

# -------------------------------------------------------
# EX 1: Tricky Picture
# -------------------------------------------------------
print("\n--- EX 1: Tricky Picture ---")
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
for row in picture:
    for pixel in row:
        print("*" if pixel == 1 else " ", end="")
    print()

# -------------------------------------------------------
# EX 2: Nota examen cu validare
# -------------------------------------------------------
print("\n--- EX 2: Nota examen ---")

def calificativ(nota):
    if nota >= 9:
        return "Excelent"
    elif nota >= 7:
        return "Bine"
    elif nota >= 5:
        return "Suficient"
    else:
        return "Reexaminare"

def ex2_interactiv():
    while True:
        try:
            nota = float(input("Introduceți nota examenului (1-10): "))
            if nota < 1 or nota > 10:
                print("Notă invalidă! Introduceți o valoare între 1 și 10.")
                continue
            print(f"Calificativ: {calificativ(nota)}")
            break
        except ValueError:
            print("Notă invalidă! Introduceți un număr.")

# Demo fara input
for n in [9.5, 8, 6, 3]:
    print(f"Nota {n} => {calificativ(n)}")

# ex2_interactiv()  # decomentati pentru rulare interactiva

# -------------------------------------------------------
# EX 3: Ghiceste numarul (1-50)
# -------------------------------------------------------
print("\n--- EX 3: Ghiceste numarul (1-50) ---")

def joc_ghicire():
    numar_secret = random.randint(1, 50)
    incercari = 0
    while True:
        try:
            ghicit = int(input("Ghiceste numarul (1-50): "))
            incercari += 1
            if ghicit < numar_secret:
                print("Numarul este mai mare!")
            elif ghicit > numar_secret:
                print("Numarul este mai mic!")
            else:
                print(f"Felicitari! Ai ghicit numarul in {incercari} incercari.")
                return
        except ValueError:
            print("Introduceti un numar valid.")

# Demo simulat
print("Demo simulat (numar secret = 25):")
numar_demo = 25
for ghicit in [20, 30, 25]:
    if ghicit < numar_demo:
        print(f"Ghiceste numarul (1-50): {ghicit} => Numarul este mai mare.")
    elif ghicit > numar_demo:
        print(f"Ghiceste numarul (1-50): {ghicit} => Numarul este mai mic.")
    else:
        print(f"Ghiceste numarul (1-50): {ghicit} => Felicitari! Ai ghicit numarul in 3 incercari.")

# joc_ghicire()  # decomentati pentru rulare interactiva

# -------------------------------------------------------
# EX 4: Orase cu enumerate
# -------------------------------------------------------
print("\n--- EX 4: Orase cu enumerate ---")
orase = ["București", "Cluj-Napoca", "Timișoara", "Iași"]
for i, oras in enumerate(orase, 1):
    print(f"{i}. {oras}")

# -------------------------------------------------------
# EX 5: Loterie
# -------------------------------------------------------
print("\n--- EX 5: Loterie ---")

def loterie_demo(numere_utilizator):
    numere_extrase = random.sample(range(1, 50), 6)
    ghicite = sorted([n for n in numere_utilizator if n in numere_extrase])

    print("Bine ai venit la Loteria Python!")
    print(f"Numerele tale:   {numere_utilizator}")
    print(f"Numere extrase:  {numere_extrase}")
    print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")

    if len(ghicite) == 6:
        print("Felicitari! Jackpot!")
    elif len(ghicite) >= 4:
        print("Felicitari! Ai castigat un premiu mare!")
    elif len(ghicite) >= 2:
        print("Felicitari! Ai castigat un premiu mic!")
    else:
        print("Mai incearca data viitoare!")

def loterie_interactiv():
    print("Bine ai venit la Loteria Python!")
    print("Alege 6 numere intre 1 si 49.")
    numere = []
    for i in range(1, 7):
        while True:
            try:
                n = int(input(f"Numarul {i}: "))
                if 1 <= n <= 49 and n not in numere:
                    numere.append(n)
                    break
                else:
                    print("Numar invalid sau deja ales.")
            except ValueError:
                print("Introduceti un numar valid.")
    loterie_demo(numere)

# Demo cu valori fixe din cerinta
print("Demo cu valori fixe:")
numere_u = [7, 15, 23, 31, 40, 45]
numere_e = [12, 7, 31, 23, 8, 40]
ghicite = sorted([n for n in numere_u if n in numere_e])
print(f"Numerele tale:   {numere_u}")
print(f"Numere extrase:  {numere_e}")
print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")
print("Felicitari! Ai castigat un premiu mic!")

# loterie_interactiv()  # decomentati pentru rulare interactiva

# -------------------------------------------------------
# EX 6: Aventura in padurea magica
# -------------------------------------------------------
print("\n--- EX 6: Aventura in padurea magica ---")

def aventura():
    inventar = []
    print("\nBine ai venit in Padurea Magica!")
    print("Esti la inceputul unui drum si trebuie sa alegi o directie.")

    directie = input("Mergi la stanga sau la dreapta? (stanga/dreapta): ").strip().lower()

    if directie == "stanga":
        print("Mergi la stanga si intalnesti un lup amenintator!")
        actiune = input("Ce faci? (fugi/ascunzi): ").strip().lower()
        if actiune == "fugi":
            print("Fugi cat poti de repede si scapi, dar pierzi rucsacul cu provizii.")
        elif actiune == "ascunzi":
            print("Te ascunzi dupa un copac. Lupul trece pe langa tine.")
            print("In spatele arborelui gasesti o sabie ruginita!")
            inventar.append("sabie")
        else:
            print("Nu stii ce sa faci si lupul te sperie. Fugi!")

        directie2 = input("Dupa aceasta intalnire, continui sau te intorci la sat? (continui/intoarce): ").strip().lower()
        if directie2 == "continui":
            print("Gasesti o pestera cu cristale stralucitoare. Iei unul!")
            inventar.append("cristal magic")
        else:
            print("Te intorci la sat in siguranta.")

    elif directie == "dreapta":
        print("Mergi la dreapta si dai de o caseta de comori ingropata!")
        inventar.append("aur")
        print("Continui drumul si ajungi la un pod peste un rau.")
        actiune2 = input("Treci podul sau ocolesti prin padure? (pod/padure): ").strip().lower()
        if actiune2 == "pod":
            print("Pe pod gasesti un pergament cu o harta a comorilor!")
            inventar.append("harta comorilor")
        else:
            print("In padure gasesti un elf prietenos care iti da o cheie magica!")
            inventar.append("cheie magica")
    else:
        print("Directie necunoscuta. Ramai pe loc, derutat.")

    print(f"\nAventura s-a incheiat! Inventar: {inventar if inventar else ['gol']}")

# aventura()  # decomentati pentru rulare interactiva
print("(Decomentati aventura() pentru a juca interactiv)")

# -------------------------------------------------------
# EX 7: Analiza sentiment comentariu
# -------------------------------------------------------
print("\n--- EX 7: Analiza sentiment ---")

cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor", "urat"]

def analiza_sentiment(comentariu):
    cuvinte = comentariu.lower().split()
    are_pozitiv = any(c in cuvinte for c in cuvinte_pozitive)
    are_negativ = any(c in cuvinte for c in cuvinte_negative)

    if are_pozitiv and not are_negativ:
        return "Comentariu pozitiv!"
    elif are_negativ and not are_pozitiv:
        return "Comentariu negativ!"
    else:
        return "Comentariu neutru."

# Demo
teste = [
    "Filmul este super si frumos",
    "Acest produs este groaznic si prost",
    "Produsul a sosit ieri",
    "Este excelent dar cam dezamăgitor",
]
for t in teste:
    print(f'  "{t}"')
    print(f'  => {analiza_sentiment(t)}\n')

# -------------------------------------------------------
# EX 8: Sistem bancar - detectare tranzactii suspecte
# -------------------------------------------------------
print("\n--- EX 8: Sistem bancar ---")

TARI_RISC = ["Coreea de Nord", "Siria", "Iran"]
LIMITA_SUSPECTA = 10000

def verifica_tranzactie(suma, tara):
    if tara in TARI_RISC:
        return "Frauduloasă (țară cu risc ridicat)"
    elif suma > LIMITA_SUSPECTA:
        return "Suspicioasă (sumă mare)"
    else:
        return "Sigură"

def proceseaza_tranzactii(tranzactii):
    suspecte = 0
    print("Procesăm tranzacțiile...")
    for suma, tara in tranzactii:
        status = verifica_tranzactie(suma, tara)
        print(f"  Tranzacție: {suma} RON din {tara} → {status}")
        if status != "Sigură":
            suspecte += 1
        if suspecte >= 3:
            print(f"\n  {suspecte} tranzacții suspecte detectate! Cont blocat.")
            return
    print(f"\n  Total tranzacții suspecte: {suspecte}. Contul este activ.")

# Demo cu datele din cerinta
tranzactii_demo = [
    (5000, "România"),
    (15000, "Germania"),
    (2000, "Coreea de Nord"),
    (12000, "SUA"),
]
proceseaza_tranzactii(tranzactii_demo)

def tranzactii_manuale():
    tranzactii = []
    print("\nIntroduceti tranzactii (tastati 'stop' la suma pentru a termina):")
    while True:
        suma_str = input("Suma (RON): ").strip()
        if suma_str.lower() == "stop":
            break
        try:
            suma = float(suma_str)
            tara = input("Tara: ").strip()
            tranzactii.append((suma, tara))
        except ValueError:
            print("Suma invalida.")
    if tranzactii:
        proceseaza_tranzactii(tranzactii)

# tranzactii_manuale()  # decomentati pentru rulare interactiva

print("\n" + "=" * 60)
print("TOATE EXERCITIILE LAB 2 COMPLETE!")
print("=" * 60)
