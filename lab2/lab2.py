import random


numar_aleatoriu = random.randint(1, 50)
contor = 3

while contor > 0:
    numar = int(input("Introduceti un numar: "))

    if numar != numar_aleatoriu:
        print("Numarul introdus este diferit de numarul aleatoriu")
    else:
        print("Numarul introdus este egal cu numarul aleatoriu")
        break

    contor -= 1

if contor == 0 and numar != numar_aleatoriu:
    print(f"Ai ramas fara incercari. Numarul era {numar_aleatoriu}.")

    