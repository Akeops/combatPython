monsters = {
    "pikachu" : {
        "name" : "Pikachu",
        "attacks" : ["charge", "tonnerre"],
        "damages" : [20, 40]
    },
    "grolem" : {
        "name" : "Grolem",
        "attacks" : ["tacle", "seisme"],
        "damages" : [15, 45]
    },
    "carapuce" : {
        "name" : "Carapuce",
        "attacks" : ["charge", "pistolet à O"],
        "damages" : [20, 35]
    }
}

attacks = {
    "charge" : {"damages" : 20},
    "tacle" : {"damages" : 15},
    "tonnerre" : {"damages" : 40},
    "seisme" : {"damages" : 40},
    "pistolet à O" : {"damages" : 35},
}




# Choix Pokémon du Personnage1
print("Pokémon disponible :")
for pokemon in monsters.values():
    print("-", pokemon["name"])

players = []

print("Joueur 1, quel pokémon choisissez-vous ?")
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

print("Joueur 2, quel pokémon choisissez-vous ?")
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

msg1 = f"{players[0].get('name')} {str(players[0].get('PV'))} (PV) affronte {players[1].get('name')} ({str(players[1].get('PV'))} PV)"

print("+" * (len(msg1)+ 4)) # Petites étoiles qui entourent le texte #
print("+ " + msg1 + " +")
print("+" * (len(msg1)+ 4))

print()


# Début du combat
i = 0
while players[0].get('PV') > 0 and players[1].get('PV') > 0:
    print("Tour numéro :", i)
    if i < 1:
        pv1 = players[0].get('PV')
        pv2 = players[1].get('PV')
        player1 = players[0].get('name')
        player2 = players[1].get('name')

    print()

    print(players[0].get('name'), ", Veuillez choisir l'attaque que vous voulez lancer ?")
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
    elif players[0].get('name') == 'grolem':
        print('1 -', monsters['grolem']['attacks'][0].capitalize(), '(', attacks['tacle']['damages'], ' dégats)')
        print('2 -', monsters['grolem']['attacks'][1].capitalize(), '(', attacks['seisme']['damages'], ' dégats)')
        att1 = input('> ')
        while not att1.isdigit() or not 1 <= int(att1) <= len(monsters['grolem']['attacks']):
            print("Réponse incorrect, veuillez réessayer")
            att1 = input('> ')
        att1_idx = int(att1) - 1
        attaque1 = monsters['grolem']['attacks'][att1_idx]
        damage1 = monsters['grolem']['damages'][att1_idx]
    elif players[0].get('name') == 'carapuce':
        print('1 -', monsters['carapuce']['attacks'][0].capitalize(), '(', attacks['charge']['damages'], ' dégats)')
        print('2 -', monsters['carapuce']['attacks'][1].capitalize(), '(', attacks['pistolet à O']['damages'], ' dégats)')
        att1 = input('> ')
        while not att1.isdigit() or not 1 <= int(att1) <= len(monsters['carapuce']['attacks']):
            print("Réponse incorrect, veuillez réessayer")
            att1 = input('> ')
        att1_idx = int(att1) - 1
        attaque1 = monsters['carapuce']['attacks'][att1_idx]
        damage1 = monsters['carapuce']['damages'][att1_idx]

    print()


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

    if pv2 <= 0:
        msg1 = f"{player2} n'a plus de PV."
        msg2 = f"{player1} est le vainqueur de ce combat combat !"
        break

    print()

    # Personnage2 attaque Personnage1

    print(players[1].get('name'), "Veuillez choisir l'attaque que vous voulez lancer ?")
    if players[1].get('name') == 'pikachu':
        print('1 -', monsters['pikachu']['attacks'][0].capitalize(), '(', attacks['charge']['damages'], ' dégats)')
        print('2 -', monsters['pikachu']['attacks'][1].capitalize(), '(', attacks['tonnerre']['damages'], ' dégats)')
        att2 = input('> ')
        while not att2.isdigit() or not 1 <= int(att2) <= len(monsters['pikachu']['attacks']):
            print("Réponse incorrect, veuillez réessayer")
            att2 = input('> ')
        att2_idx = int(att2) - 1
        attaque2 = monsters['pikachu']['attacks'][att2_idx]
        damage2 = monsters['pikachu']['damages'][att2_idx]
    elif players[1].get('name') == 'grolem':
        print('1 -', monsters['grolem']['attacks'][0].capitalize(), '(', attacks['tacle']['damages'], ' dégats)')
        print('2 -', monsters['grolem']['attacks'][1].capitalize(), '(', attacks['seisme']['damages'], ' dégats)')
        att2 = input('> ')
        while not att2.isdigit() or not 1 <= int(att2) <= len(monsters['grolem']['attacks']):
            print("Réponse incorrect, veuillez réessayer")
            att2 = input('> ')
        att2_idx = int(att2) - 1
        attaque2 = monsters['grolem']['attacks'][att2_idx]
        damage2 = monsters['grolem']['damages'][att2_idx]
    elif players[1].get('name') == 'carapuce':
        print('1 -', monsters['carapuce']['attacks'][0].capitalize(), '(', attacks['charge']['damages'], ' dégats)')
        print('2 -', monsters['carapuce']['attacks'][1].capitalize(), '(', attacks['pistolet à O']['damages'],
              ' dégats)')
        att2 = input('> ')
        while not att2.isdigit() or not 1 <= int(att2) <= len(monsters['carapuce']['attacks']):
            print("Réponse incorrect, veuillez réessayer")
            att2 = input('> ')
        att2_idx = int(att2) - 1
        attaque2 = monsters['carapuce']['attacks'][att2_idx]
        damage2 = monsters['carapuce']['damages'][att2_idx]

    pv1 -= damage2
    msg1 = f"{player2} attaque {attaque2} sur {player1} qui perd {damage2} PV."
    msg2 = f"{player2} a maintenant {str(pv1)} PV !"
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    print("+" * (max_size + 4))
    print("+", msg1, "+")
    print("+", msg2, "+")
    print("+" * (max_size + 4))


    if pv1 <= 0:
        msg1 = f"{player1} n'a plus de PV."
        msg2 = f"{player2} est le vainqueur de ce combat combat !"
        break

    i += 1

print()

max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print("+" * (max_size + 4))
print("+", msg1, "+")
print("+", msg2, "+")
print("+" * (max_size + 4))