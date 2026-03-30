import json
import random

element = []

with open("jsontest.json", "r", encoding="UTF-8") as truc:
    salut = json.load(truc)

print(f"Il y a {len(salut)} questions dans le fichier JSON :")

for q in salut:
    print(f"\nQuestion {int(q)+1} : {salut[q]["question"]}")
    for i in range(1,5):
        if salut[q][str(i)] != None:
            print(f"Réponse {i} : {salut[q][str(i)]}")
    print(f"Bonne réponse : {salut[q]["reponse"]}")
    element.append(q)

print(element)
print(random.choice(element))