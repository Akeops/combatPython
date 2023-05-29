personnage1 = input("Entrez le nom du premier joueur").capitalize()
pv1 = int(input("Entre le nombre de pv du premier joueur"))

personnage2 = input("Entrez le nom du deuxième joueur").capitalize()
pv2 = int(input("Entre le nombre de pv du deuxième joueur"))

print()

# Début du combat #
msg1 = f"{personnage1} {str(pv1)} PV) affronte {personnage2} ({str(pv2)} PV)"

print("+" * (len(msg1)+ 4)) # Petites étoiles qui entourent le texte #
print("+ " + msg1 + " +")
print("+" * (len(msg1)+ 4))

print()

# Tour 1 - personnage1 attaque personnage2 #
menu = ''', quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-40 PV)'''

print()
print(personnage1, menu)
att1 = input('> ').lower()
print()

if att1 == "1" or att1 == "charge":
    damages = 20
    attack = "charge"
elif att1 == "2" or att1 == "tonnerre":
    damages = 40
    attack = "tonnerre"
else:
    damages = 0
    attack = ""
    print("Vous n'avez pas choisi",  pv2 , "d'attaque. Vous passez donc le tour.")


pv2 -= damages
msg1 = f"{personnage1} attaque {attack} sur {personnage2} qui perd {str(damages)} PV."
msg2 = f"{personnage2} a maintenant {str(pv2)} PV !"
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))

# Tour 1 = personnage2 attaque personnage1 #
menu = ''', quelle attaque voulez-vous utiliser ?
1. Tacle (-15 PV)
2. Seisme (-50 PV)'''

print()
print(personnage2, menu)
att2 = input('> ').lower()
print()

if att2 == "1" or att2 == "tacle":
    damages = 15
    attack = "tacle"
elif att2 == "2" or att2 == "seisme":
    damages = 50
    attack = "seisme"
else:
    damages = 0
    attack = ""
    print("Vous n'avez pas choisi d'attaque. Vous passez donc le tour.")

print()

pv1 -= damages
msg1 = f"{personnage2} attaque {attack} sur {personnage1} qui perd {str(damages)} PV."
msg2 = f"{personnage1} a maintenant {str(pv1)} PV !"
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))

if pv1 == pv2:
    msg1 = f"{personnage1} et {personnage2} ont tous les deux {pv1}."
    msg2 = "Il y a donc égalité !"
if pv1 > pv2:
    msg1 = f"{personnage1} {str(pv1)} PV, a plus de PV que {personnage2} {str(pv2)} PV."
    msg2 = f"{personnage1} est le vainqueur du combat !"
elif pv2 > pv1:
    msg1 = f"{personnage2} {str(pv2)} PV, a plus de PV que {personnage1} {str(pv1)} PV."
    msg2 = f"{personnage2} est le vainqueur du combat !"

print()

max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))
