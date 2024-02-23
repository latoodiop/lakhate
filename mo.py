personne = [
    ("latoo", 20, 1.83),
    ("basse", 26, 1.70),
    ("ouz", 23, 1.80),
    ("adya", 24, 1.60)
]

def obtenir_info(nom, liste):
    for i in liste:
        if i[0]==nom:
            return i
        return None
#--------------------------------
    
infos = obtenir_info("lat",personne)
print(infos)