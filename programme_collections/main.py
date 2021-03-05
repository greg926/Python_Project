# Collections : (Tableaux : Array), Listes, Tuples...
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> modifiable : rajouter/supprimer des éléments ou les modifiers
# len (): c'est "lense" en anglais qui veut dire "longueur" en français
# Plusieurs éléments

# -------------- TUPLES -------------------
# personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1]) # -1 pour le dernier element

# for i in range(0, len(personnes)):
    # print(personnes[i])

#for i in personnes:
#    print(i)
#    print(len(i))
#    print(i[-1])

# (0, 1, 2, 3, 4, 5)
# valeurs = range(0, 5)
# print(valeurs[-1])

# -------------- lISTES -------------------
personnes = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"

# print(personnes)

personnes.append(nouvelle_personne) # append veut dire "ajouter"
del personnes[1]

# print(personnes)

def afficher_personnes(c):
    for i in c:
        print(i)

def modifier_valeur(a):
    a[0] = 10



test = [1, 2, 3, 4]
print(test)
modifier_valeur(test)
print(test)

# afficher_personnes(personnes)
