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
        "attacks" : ["charge", "ecume"],
        "damages" : [20, 35]
    }
}

attacks = {
    "charge" : {"damages" : 20},
    "tacle" : {"damages" : 15},
    "tonnerre" : {"damages" : 40},
    "seisme" : {"damages" : 40},
    "ecume" : {"damages" : 35},
}


# Choix Pokémon du Personnage1
print("Pokémon disponible :")
for pokemon in monsters.values():
    print("-", pokemon["name"])

players = []

# Boucle pour créer 2 joueurs sans se répéter
for i in range(2):
    player_id = i + 1
    print("Joueur", player_id, "quel pokémon choisissez-vous ?")

    name = input('> ').lower()
    while name not in monsters:
        print('Pokémon invalide')
        name = input('> ').lower()

    print("Quel est son nombre de PV ?")
    pv_str = input('> ')
    while not pv_str.isdigit():
        print("Ce n'est pas un nombre")
        pv_str = input('> ')

    pv = int(pv_str)
    players.append({"id": player_id, "pokemon": monsters[name], "pv": pv})


print()
print(players[0]['pokemon']['name'], players[0]['pv'], "PV affronte", players[1]['pokemon']['name'], players[1]['pv'],"PV ")
print()

# Représente les tours de jeu, liste de couples (joueur, opposant)
turns = [
    (players[0], players[1]),
    (players[1], players[0]),
]

# Début du combat
i = 0
nombreDeTour = 1
while players[0]['pv'] > 0 and players[1]['pv'] > 0:
    print()
    print("Tour", nombreDeTour)
    for player, opponent in turns:
        if player['pv'] > 0:
            print("Joueur", player['id'], ", quel attaque utilisez-vous ?")
            for name in player['pokemon']['attacks']:
                print('-', name.capitalize(), attacks[name]['damages'], 'PV')

            att_name = input('> ').lower()
            while att_name not in attacks:
                print("Vous n'avez pas pris d'attaque existente")
                att_name = input('> ').lower()
            attack = attacks[att_name]

            opponent['pv'] -= attack['damages']

            print()

            print(player['pokemon']['name'], "attaque",
                  opponent['pokemon']['name'],
                  "qui perd", attack['damages'], "PV, il lui reste",
                  opponent['pv'], "PV"
            )
            nombreDeTour += 1
            print()

if players[0]['pv'] <= 0:
    winner = players[1]
    print(players[0]['pokemon']['name'], "n'a plus de PV, le joueur", winner['id'], "remporte le combat avec", players[1]['pokemon']['name'])
else:
    winner = players[0]
    print(players[1]['pokemon']['name'], "n'a plus de PV, le joueur", winner['id'], "remporte le combat avec", players[0]['pokemon']['name'])