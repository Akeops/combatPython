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
pv1 = input("Entre le nombre de pv du premier joueur").capitalize()

personnage2 = input("Entrez le nom du deuxième joueur").capitalize()
pv2 = input("Entre le nombre de pv du deuxième joueur").capitalize()

afficher = personnage1 + " (" + str(pv1) + "pv) affronte " + personnage2 + " (" + str(pv2) + "pv)"
print("+" * (len(afficher)+ 4) )
print(afficher)
print("+" * (len(afficher)+ 4) )
