
jucator1 = input("Nume jucator 1: ")
jucator2 = input("Nume jucator 2: ")

print (f"{jucator1} vs {jucator2}")

reguli ={
    "piatra": "foarfeca",
    "foarfeca": "hartie",
    "hartie": "piatra"
}


def castigator(mana1, mana2):
    if mana1 == mana2:
        return "Remiza"
    elif reguli[mana1] == mana2:
        return jucator1
    else:
        return jucator2

scor = {jucator1: 0, jucator2: 0}
while True:
    
    
    mana_aleasa = input("Alege mana (piatra, foarfeca, hartie): ")
    print(f"{jucator1} a ales {mana_aleasa}")
    mana_aleasa2 = input("Alege mana (piatra, foarfeca, hartie): ")
    print(f"{jucator2} a ales {mana_aleasa2}")  
    if mana_aleasa not in ["piatra", "foarfeca", "hartie"] or mana_aleasa2 not in ["piatra", "foarfeca", "hartie"]:
        print("Mana aleasa nu este valida. Incearca din nou.")
        continue
    

    rezultat = castigator(mana_aleasa, mana_aleasa2)
    scor[rezultat] += 1
    print(f"Castigatorul este: {rezultat}")
    print (f"Scor: {jucator1} - {scor[jucator1]}, {jucator2} - {scor[jucator2]}")   

    restarta = input("Vrei sa joci din nou? (da/nu): ")
    if restarta.lower() == "nu":
        break
    

