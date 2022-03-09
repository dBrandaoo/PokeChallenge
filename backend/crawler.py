import requests
import json

for i in range(1, 900):
    r = requests.get(f'https://pokeapi.glitch.me/v1/pokemon/{i}')
    x = r.json()
    name = x[0]["name"]
    with open(f'pokemons\\{name}.json', 'w') as f:
        json.dump(x, f)








