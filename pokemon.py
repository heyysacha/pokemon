import requests
import random

def random_pokemon():
    pokemon_number = random.randint(1,151)
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

player_pokemon = random_pokemon()
computer_pokemon = random_pokemon()

print("Your Pokemon is number %i: %s. Your opponent's Pokemon is number %i: %s."  % (player_pokemon['id'], player_pokemon['name'], computer_pokemon['id'], computer_pokemon['name']))

while True:
    player_stat = input("Which stat would you like to use? (Height, weight, HP, attack, defense, or speed): ").lower()
    if player_stat == 'height' or player_stat == 'weight' or player_stat == 'hp' or player_stat == 'attack' or player_stat == 'defense' or player_stat == 'speed':
       break
    else:
        print('Please choose one of the given stats.')
        continue
        break

print("Your %s was: %i, your opponent's %s was: %i." % (player_stat, player_pokemon[player_stat], player_stat, computer_pokemon[player_stat]))

if player_pokemon[player_stat] > computer_pokemon[player_stat]:
    print("You win!")
else:
    print("You lose!")
