# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Personnage :
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv



personnage1 = input("Entrez le nom du premier joueur").capitalize()
pv1 = int(input("Entre le nombre de pv du premier joueur"))

personnage2 = input("Entrez le nom du deuxième joueur").capitalize()
pv2 = int(input("Entre le nombre de pv du deuxième joueur"))

print()

# Début du combat #
msg1 = personnage1 + " (" + str(pv1) + "pv) affronte " + personnage2 + " (" + str(pv2) + "pv)"

print("+" * (len(msg1)+ 4)) # Petites étoiles qui entourent le texte #
print("+ " + msg1 + " +")
print("+" * (len(msg1)+ 4))

print()


# Tour 1 - personnage1 attaque personnage2 #
att1 = int(input(personnage1 + " combien de dégats infligez-vous à " + personnage2 + " ?"))

print()

pv2 -= att1
msg1 = personnage1 + " attaque " + personnage2 + " qui perd " + str(att1)
msg2 = personnage2 + " a maintenant " + str(pv2) + " PV"
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))

# Affichage de l'attaque #
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))

print()

# Tour 1 = personnage2 attaque personnage1 #
att2 = int(input(personnage2 + " combien de dégats infligez-vous à " + personnage1 + " ?"))
pv1 -= att2
msg1 = personnage2 + " attaque " + personnage1 + " qui perd " + str(att2)
msg2 = personnage1 + " a maintenant " + str(pv1) + " PV"
max_size = (max(len(msg1), len(msg2)))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))

print()

# Affichage de l'attaque #
print("+" * (max_size + 4))
print("+", msg1,  "+")
print("+",  msg2,  "+")
print("+" * (max_size + 4))

print()

# Fin du combat #
msg1 = "Fin du combat"
msg2 = personnage1 + " a " + str(pv1) + " PV"
msg3 = personnage2 + " a " + str(pv2) + " PV"
max_size = max(len(msg1), len(msg2), len(msg3))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
msg3 += ' ' * (max_size - len(msg3))

print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+", msg3, "+")
print("+" * (max_size+4))