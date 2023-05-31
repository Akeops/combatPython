monsters = {
    "pikachu" : {
        "name" : "Pikachu",
        "attacks" : ["charge", "tonnerre"],
        "damages" : [20, 40]
    },
    "grolem" : {
        "name" : "Grolem",
        "attacks" : ["tacle", "seisme"]
    },
    "carapuce" : {
        "name" : "Carapuce",
        "attacks" : ["charge", "pistolet à O"]
    }
}

attacks = {
    "charge" : {"damages" : 20},
    "tacle" : {"damages" : 15},
    "tonnerre" : {"damages" : 35},
    "seisme" : {"damages" : 40},
    "pistolet à O" : {"damages" : 35},
}




# Choix Pokémon du Personnage1
print("Pokémon disponible :")
for pokemon in monsters.values():
    print("-", pokemon["name"])

players = []

print("Personnage 1, quel monstre choisissez-vous ?")
name = input("> ").lower()
while name not in monsters:
    print("Ce pokémon n'est pas disponible")
    name = input("> ").lower()

# On vérifie que l'utilisateur mette bien un nombre
print("Coisissez le nombre de PV que vous voulez affecter")
pv1_str = input("> ")
while not pv1_str.isdigit():
    print("Vous n'avez pas entré un nombre, veuillez réessayer")
    pv1_str = input("> ")

# int(), str(), bool() etc... permet de transformer la variable dans le type que l'on veut.
pv = int(pv1_str)
players.append({"id" : "1", "name" : name, "PV" : pv})







# Choix Pokémon du Personnage2
print("Pokémon disponible :")
for pokemon in monsters.values():
    print("-", pokemon["name"])

print("Personnage 2, quel monstre choisissez-vous ?")
name = input("> ").lower()
while name not in monsters:
    print("Ce pokémon n'est pas disponible")
    name = input("> ").lower()

print("Coisissez le nombre de PV que vous voulez affecter")
pv2_str = input("> ")
while not pv2_str.isdigit():
    print("Vous n'avez pas entré un nombre, veuillez réessayer")
    pv2_str = input("> ")

pv = int(pv2_str)
players.append({"id" : "2", "name" : name, "PV" : pv})

print()
#print(monsters[0].get('attacks'))
#print()
msg1 = f"{players[0].get('name')} {str(players[0].get('PV'))} (PV) affronte {players[1].get('name')} ({str(players[1].get('PV'))} PV)"

print("+" * (len(msg1)+ 4)) # Petites étoiles qui entourent le texte #
print("+ " + msg1 + " +")
print("+" * (len(msg1)+ 4))

print()


# Début du combat
while players[0].get('PV') > 0 and players[1].get('PV') > 0:

    pv1 = players[0].get('PV')
    pv2 = players[1].get('PV')
    player1 = players[0].get('name')
    player2 = players[1].get('name')

    print("Veuillez choisir l'attaque que vous voulez lancer ?")
    if players[0].get('name') == 'pikachu':
            print('1 -', monsters['pikachu']['attacks'][0].capitalize(), '(', attacks['charge']['damages'], ' dégats)')
            print('2 -', monsters['pikachu']['attacks'][1].capitalize(), '(', attacks['tonnerre']['damages'], ' dégats)')
            att1 = input('> ')
            while not att1.isdigit() or not 1 <= int(att1) <= len(monsters['pikachu']['attacks']):
                print("Réponse incorrect, veuillez réessayer")
                att1 = input('> ')
            att1_idx = int(att1) - 1
            attaque1 = monsters['pikachu']['attacks'][att1_idx]
            damage1 = monsters['pikachu']['damages'][att1_idx]


    pv2 -= damage1
    msg1 = f"{player1} attaque {attaque1} sur {player2} qui perd {damage1} PV."
    msg2 = f"{player2} a maintenant {str(pv2)} PV !"
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    print("+" * (max_size + 4))
    print("+", msg1, "+")
    print("+", msg2, "+")
    print("+" * (max_size + 4))

    # Personnage1 attaque Personnage2


    print()
    print(players[0].get('name'), menu)
    i = 0
    for name in attack_names:
        print(f"{i + 1}. {attack_names[i].capitalize()} ({attack_damages[i]} Dégats)")
        i += 1

    att1 = input('> ')
    while not att1.isdigit or not 1 <= int(att1) <= len(attack_names):
        print("Veuillez entrer une bonne réponse")
        att1 = input('> ')


    att1_idx = int(att1) - 1
    damages = monsters['pikachu']['damages'][att1_idx]

    pv2 -= damages
    msg1 = f"{players[0]} attaque {attack_names[att1_idx]} sur {personnage2} qui perd {damages} PV."
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

    # Personnage2 attaque Personnage1
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
    msg1 = f"{personnage2} attaque {attack_names2[att2_idx]} sur {players[0]} qui perd {str(damages)} PV."
    msg2 = f"{players[0]} a maintenant {str(players[0, 2])} PV !"
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    print("+" * (max_size + 4))
    print("+", msg1, "+")
    print("+", msg2, "+")
    print("+" * (max_size + 4))


    if pv1 <= 0:
        msg1 = f"{players[0]} est K.O"
        msg2 = f"{personnage2} est le vainqueur du combat !"


print()

max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))
