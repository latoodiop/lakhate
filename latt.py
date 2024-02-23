def demander_age(exe):

    age_v = 0
    while age_v==0:

        age = input("ton age: ")

        try:
            age_v = int(age)+1
        except:
            print("oups une erreur")
       
            

    return age_v
#_____________
age = input("ton age: ")
age_v1=demander_age(age)
age_v2=demander_age(age)

print("tu auras",age_v1)
print("tu auras",age_v2)

