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



def poser_question(question):
    global score

    titre_question=question[0]
    liste=question[1]
    choix_bonne_reponce=question[2]
    
    print(titre_question)
    liste
    compteur= len(liste)
    for i in liste:
        print(compteur-1, "-",i)

    reponse= input("votre reponse (entre 1 et " + str(compteur+1) +"): ")
    if reponse.lower() == choix_bonne_reponce:
        print("bonne reponse")
        score+=1
    else:
        print("c'est pas sa")



score=0
question1 = ("quelle est la capitale de france?:", (" marseille"," nice", " paris", " nantes"), "paris")
question2 = ("quelle est la capitale d' italie?:", (" rome"," inter", " torrino", " juventive"), "rome")

poser_question(question1)
poser_question(question2)
print("l'score final", score)