# Collections : (Tableaux : Array), Listes, Tuples...
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> modifiable : rajouter/supprimer des éléments ou les modifiers
# len (): c'est "lense" en anglais qui veut dire "longueur" en français
# Plusieurs éléments

a = 5
b = "toto"

personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1]) # -1 pour le dernier element

# for i in range(0, len(personnes)):
    # print(personnes[i])

#for i in personnes:
#    print(i)
#    print(len(i))
#    print(i[-1])

# (0, 1, 2, 3, 4, 5)
valeurs = range(0, 5)
print(valeurs[-1])