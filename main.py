personnage1 = input("Entrez le nom du premier joueur").capitalize()
pv1_str = input("Entre le nombre de pv du premier joueur")
while not pv1_str.isdigit():
    print("Vous n'avez pas entré un nombre, veuillez réessayer")
    pv1_str = input("Entre le nombre de pv du premier joueur")
pv1 = int(pv1_str)
personnage2 = input("Entrez le nom du deuxième joueur").capitalize()
pv2_str = input("Entre le nombre de pv du deuxième joueur")
while not pv2_str.isdigit():
    print("Vous n'avez pas entré un nombre, veuillez réessayer")
    pv2_str = input("Entre le nombre de pv du premier joueur")
pv2 = int(pv2_str)

print()

msg1 = f"{personnage1} {str(pv1)} (PV) affronte {personnage2} ({str(pv2)} PV)"

print("+" * (len(msg1)+ 4)) # Petites étoiles qui entourent le texte #
print("+ " + msg1 + " +")
print("+" * (len(msg1)+ 4))

# Début du combat #
while pv1 > 0 and pv2 > 0:

    attack_names = ["charge", "tonnerre"]
    attack_damages = [20, 40]

    print()

    # Personnage1 attaque Personnage2 #
    menu = f''', quelle attaque voulez-vous utiliser ?'''

    print()
    print(personnage1, menu)
    i = 0
    for name in attack_names:
        print(f"{i + 1}. {attack_names[i].capitalize()} ({attack_damages[i]} Dégats)")
        i += 1

    att1 = input('> ')
    while not att1.isdigit or not 1 <= int(att1) <= len(attack_names):
        print("Veuillez entrer une bonne réponse")
        att1 = input('> ')


    att1_idx = int(att1) - 1
    damages = attack_damages[att1_idx]

    pv2 -= damages
    msg1 = f"{personnage1} attaque {attack_names[att1_idx]} sur {personnage2} qui perd {damages} PV."
    msg2 = f"{personnage2} a maintenant {str(pv2)} PV !"
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    print("+" * (max_size + 4))
    print("+", msg1, "+")
    print("+", msg2, "+")
    print("+" * (max_size + 4))

    if pv2 <= 0:
        msg1 = f"{personnage2} est K.O"
        msg2 = f"{personnage1} est le vainqueur du combat !"
        break

    # Tour 1 = personnage2 attaque personnage1 #
    attack_names2 = ["tacle", "séisme"]
    attack_damages2 = [15, 45]
    menu = f''', quelle attaque voulez-vous utiliser ?'''

    print()
    print(personnage2, menu)
    i = 0
    for name in attack_names2:
        print(f"{i + 1}. {attack_names2[i].capitalize()} ({attack_damages2[i]} Dégats)")
        i += 1

    att2 = input('> ')
    while not att2.isdigit or not 1 <= int(att2) <= len(attack_names2):
        print("Veuillez entrer une bonne réponse")
        att2 = input('> ')

    att2_idx = int(att2) - 1
    damages = attack_damages2[att2_idx]

    pv1 -= damages
    msg1 = f"{personnage2} attaque {attack_names2[att2_idx]} sur {personnage1} qui perd {str(damages)} PV."
    msg2 = f"{personnage1} a maintenant {str(pv1)} PV !"
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    print("+" * (max_size + 4))
    print("+", msg1, "+")
    print("+", msg2, "+")
    print("+" * (max_size + 4))


    if pv1 <= 0:
        msg1 = f"{personnage1} est K.O"
        msg2 = f"{personnage2} est le vainqueur du combat !"


print()

max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))
