nom = input("Nom : ")
print("\n")
heures_travaillees = input("Combien d'heures as-tu travaillé cette semaine : ")
print("\n")
rendu = input("Où es-tu rendu : ")
print("\n")

with open(nom + ".txt", "w") as fichier:
    fichier.write("Nom : " + nom + "\n")
    fichier.write("Heures travaillées cette semaine : " + heures_travaillees + "\n")
    fichier.write("Où tu es rendu : " + rendu + "\n")

print("Fichier télécharger '"+ nom +".txt'.")
