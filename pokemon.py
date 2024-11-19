import requests
import random

print("Welcome to the Pokemon challenge!")

def random_pokemon():
    pokemon_number = random.randint(1,1025)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'].title(),
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat']
    }

player_score = 0
computer_score = 0

def play_round():
    player_pokemon = random_pokemon()
    computer_pokemon = random_pokemon()

    global player_score
    global computer_score

    print("Your Pokemon is number %i: %s."  % (player_pokemon['id'], player_pokemon['name']))
    print("Height: %i" % (player_pokemon['height']))
    print("Weight: %i" % (player_pokemon['weight']))
    print("HP: %i" % (player_pokemon['hp']))
    print("Attack: %i" % (player_pokemon['attack']))
    print("Defense: %i" % (player_pokemon['defense']))
    print("Speed: %i" % (player_pokemon['speed']))
    print("Your opponent's Pokemon is number %i: %s." % (computer_pokemon['id'], computer_pokemon['name']))

    trade_choice = input("\nWould you like to trade your Pokémon for a new one? (yes/no): ").lower()
    if trade_choice in ['yes', 'y']:
        print("Trading your Pokémon...")
    player_pokemon = random_pokemon()
    print("Your new Pokemon is number %i: %s." % (player_pokemon['id'], player_pokemon['name']))
    print("Height: %i" % (player_pokemon['height']))
    print("Weight: %i" % (player_pokemon['weight']))
    print("HP: %i" % (player_pokemon['hp']))
    print("Attack: %i" % (player_pokemon['attack']))
    print("Defense: %i" % (player_pokemon['defense']))
    print("Speed: %i" % (player_pokemon['speed']))

    while True:
        player_stat = input("Which stat would you like to use? (Height, weight, HP, attack, defense, or speed): ").lower()
        if player_stat == 'height' or player_stat == 'weight' or player_stat == 'hp' or player_stat == 'attack' or player_stat == 'defense' or player_stat == 'speed':
           break
        else:
            print('Please choose one of the given stats.')
            continue

    print("Your %s was: %i, your opponent's %s was: %i." % (player_stat, player_pokemon[player_stat], player_stat, computer_pokemon[player_stat]))

    if player_pokemon[player_stat] > computer_pokemon[player_stat]:
        print("You win!")
        player_score = player_score + 1
    elif computer_pokemon[player_stat] > player_pokemon[player_stat]:
        print("You lose!")
        computer_score = computer_score + 1
    else:
        print("Draw!")
        play_round()

for item in range(3):
    play_round()

if player_score > computer_score:
    print("You win! Final score %i to %i" % (player_score, computer_score))
else:
    print("You lose! Better luck next time. Final score %i to %i" % (computer_score, player_score))
