import os
import mysql.connector
import json

# variables to access the database
schema = None
user = None
password = None

# gets the information needed from .env to connect to the database
x = os.path.join("../", ".env")
with open(x, "r") as info_file:
    for i in info_file:
        if i.startswith("DB_SCHEMA"):
            schema = i.split("=")[1].strip()
        elif i.startswith("DB_USER"):
            user = i.split("=")[1].strip()
        elif i.startswith("DB_PASSWORD"):
            password = i.split("=")[1].strip()
info_file.close()

# INFO EXTRACTION
folder = 'pokemons2'
for filename in os.listdir(folder):
    x = os.path.join(folder, filename)
    if os.path.isfile(x):
        with open(x, "r") as f:
            a = json.load(f)

    # in case it has only 1 type
    if len(a["types"]) < 2:
        type1 = a["types"][0]["type"]["name"]
        type2 = None
    else:
        type1 = a["types"][0]["type"]["name"]
        type2 = a["types"][1]["type"]["name"]

    # in case it has only 1 ability
    if len(a["abilities"]) < 2:
        ability1 = a["abilities"][0]["ability"]["name"]
        ability2 = None
    else:
        ability1 = a["abilities"][0]["ability"]["name"]
        ability1 = a["abilities"][1]["ability"]["name"]

    height = a["height"]
    # original height is in decimeters. Multiply by .1 to convert to meters.
    height = round(height * 0.1, 2)

    weight = a["weight"]
    # original weight is in hectograms. Multiply by .1 to convert to Kg
    weight = round(weight * 0.1, 2)

    name = a["forms"][0]["name"]
    number = a["id"]
    base_xp = a["base_experience"]
    hp = a["stats"][0]["base_stat"]
    attack = a["stats"][1]["base_stat"]
    defense = a["stats"][2]["base_stat"]
    special_attack = a["stats"][3]["base_stat"]
    special_defense = a["stats"][4]["base_stat"]
    speed = a["stats"][5]["base_stat"]
# END OF INFO EXTRACTION

# connects to the database
db = mysql.connector.connect(
    host="localhost",
    user=user,
    passwd=password,
    database=schema
)

mycursor = db.cursor()

# inserts the data into the database
mycursor.execute("INSERT INTO pokemon (name, number, base_xp, hp, attack, defense, special_attack, special_defense, speed, height, weight) VALUES (name, number, base_xp, hp, attack, defense, special_attack, special_defense, speed, height, weight)")
db.commit()



