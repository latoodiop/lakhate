def demander_age():

    age_v = 0
    while age_v==0:

        age = input("ton age: ")

        try:
            age_v = int(age)+1
        except:
            print("oups une erreur")
        else:
            print("tu auras",age_v)
    return demander_age()
