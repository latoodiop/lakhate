"""print("quelle est la capitale de france?:")
capitales = ["(a) marseille","(b) nice", "(c) paris", "(d) nantes"]
for i in capitales:
    print(i)
print("choisiser parmis les differents lettres la capitale")
reponse= input("entres la lettre correcte: ")
if reponse == "c":
    print("bonne reponse")
else:
    print("c'est pas sa")"""

""""print()

print("quelle est la capitale de l'itali?:")
capitales = ["(a) rome","(b) venise", "(c) pise", "(d) florence"]
for i in capitales:
    print(i)
print("choisiser parmis les differents lettres la capitale")
reponse= input("entres la lettre correcte: ")
if reponse == "a":
    print("bonne reponse")
else:
    print("mauvaise reponse")"""



def poser_question(question, liste, choix_bonne_reponce):
    print(question)
    capitales = liste
    for i in capitales:
        print(i)
    print("choisiser parmis les differents lettres la capitale")
    reponse= input("entres la lettre correcte: ")
    if reponse == choix_bonne_reponce:
        print("bonne reponse")
    else:
        print("c'est pas sa")

poser_question("quelle est la capitale de france?:", ["(a) marseille","(b) nice", "(c) paris", "(d) nantes"], "c")