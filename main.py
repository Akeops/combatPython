pokemons = {
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

def getChoicesInput(choices, error_message):
    entry = input('> ').lower()
    while entry not in choices:
        print(error_message)
        entry = input('> ').lower()
    return choices[entry]

def getPlayer(player_id):
    print("Joueur", player_id, ", quel pokémons chosissez-vous ?")
    pokemon = getChoicesInput(pokemons, "Pokémon invalide")
    pv = int(input("Combien de PV a votre pokémon ?"))
    return {'id' : player_id, 'pokemon' : pokemon, 'pv' : pv}

def get_players():
    print("Pokémons disponiblent :")
    for pokemon in pokemons.values():
        print('-', pokemon['name'])
    return getPlayer(1), getPlayer(2)

def applyAttack(attack, opponent):
    opponent['pv'] -= attack['damages']
    if opponent['pv'] < 0:
        opponent['pv'] == 0

def gameTurn(player, opponent):
    # Si le joueur est KO, il n'attaque pas
    if player['pv'] <= 0:
        return


    print('Joueur', player['id'], 'quelle attaque utilisez-vous ?')
    for name in player['pokemon']['attacks']:
        print('-', name.capitalize(), -attacks[name]['damages'], 'PV')

    attack = getChoicesInput(attacks, 'Attaque invalide')
    applyAttack(attack, opponent)


    print(player['pokemon']['name'], "attaque",
          opponent['pokemon']['name'],
          "qui perd", attack['damages'], "PV, il lui reste",
          opponent['pv'], "PV",
          )

def getWinner(player1, player2):
    if player1['pv'] > player2['pv']:
        return player1
    else:
        return player2

player1, player2 = get_players()

print()
print(player1['pokemon']['name'], player1['pv'], "PV affronte", player2['pokemon']['name'], player2['pv'], "PV ")
print()



while player1['pv'] > 0 and player2['pv'] > 0:
    gameTurn(player1, player2)
    gameTurn(player2, player1)

winner = getWinner(player1, player2)
print('Le joueur', winner['id'], 'remporte le combat avec', winner['pokemon']['name'])

def test_apply_attack():
    player = {'id': 0, 'monster': pokemons['pykachu'], 'pv': 100}

    applyAttack(attacks['brûlure'], player)
    assert player['pv'] == 60

    applyAttack(attacks['tonnerre'], player)
    assert player['pv'] == 10

    applyAttack(attacks['charge'], player)
    assert player['pv'] == 0


def test_get_winner():
    player1 = {'id': 0, 'pokemon': pokemons['pykachu'], 'pv': 100}
    player2 = {'id': 0, 'pokemon': pokemons['grolem'], 'pv': 0}
    assert getWinner(player1, player2) == player1
    assert getWinner(player2, player1) == player1

    player2['pv'] = 120
    assert getWinner(player1, player2) == player2
    assert getWinner(player2, player1) == player2

    player1['pv'] = player2['pv'] = 0
    assert getWinner(player1, player2) == player2
    assert getWinner(player2, player1) == player1

if __name__ == '__main__':
    player1, player2 = get_players()

    print()
    print(player1['pokemon']['name'], player1['pv'], "PV affronte", player2['pokemon']['name'], player2['pv'], "PV ")
    print()

    while player1['pv'] > 0 and player2['pv'] > 0:
        gameTurn(player1, player2)
        gameTurn(player2, player1)

    winner = getWinner(player1, player2)
    print('Le joueur', winner['id'], 'remporte le combat avec', winner['pokemon']['name'])