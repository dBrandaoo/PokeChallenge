import os
import json
import requests
from settings.database import DB
import shutil


def catch_all(first_index=1, api="https://pokeapi.co/api/v2/pokemon/"):
    """
    Catches all the pokemon available.
    :param first_index: Defines the start of the catch. [first_index, ...]
    :param api: Defines the API to get the data 'https://pokeapi.co/api/v2/pokemon/' (dafault)
    'https://pokeapi.glitch.me/v1/pokemon/'
    :return:
    """
    folder = "pokemon2"  # complex API
    folder2 = "pokemon"  # simple API

    while True:
        if api == "https://pokeapi.co/api/v2/pokemon/":
            if f"{first_index}.json" not in os.listdir(folder):

                pokemon_path = os.path.join(folder, f"{first_index}.json")

                r = requests.get(f"{api}{first_index}")

                if r.status_code != 200:
                    raise Exception

                with open(pokemon_path, "w") as f:
                    json.dump(json.loads(r.text), f, indent=4)

                first_index += 1
            else:
                print(f"File '{first_index}.json' already present in the machine")
                first_index += 1
        elif api == "https://pokeapi.glitch.me/v1/pokemon/":
            if f"{first_index}.json" not in os.listdir(folder2):

                pokemon_path = os.path.join(folder2, f"{first_index}.json")

                r = requests.get(f"{api}{first_index}")

                if r.status_code != 200:
                    raise Exception

                with open(pokemon_path, "w") as f:
                    json.dump(json.loads(r.text), f, indent=4)
                first_index += 1
            else:
                print(f"File '{first_index}.json' is already present in the machine")
                first_index += 1
        else:
            raise Exception


def single_catch(poke_id, api="https://pokeapi.co/api/v2/pokemon/"):
    """
    Gets a single pokemon using its ID if it isn't already in the machine
    :param poke_id: Select the ID of the pokemon to get
    :param api: Defines the API to get the data 'https://pokeapi.co/api/v2/pokemon/' (dafault)
    'https://pokeapi.glitch.me/v1/pokemon/'
    :return:
    """
    folder = "pokemon2"  # complex API
    folder2 = "pokemon"  # simple API

    if api == "https://pokeapi.co/api/v2/pokemon/":
        if f'{poke_id}.json' not in os.listdir(folder):
            pokemon_path = os.path.join(folder, f"{poke_id}.json")

            r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}")

            if r.status_code != 200:
                raise Exception

            with open(pokemon_path, "w") as f:
                json.dump(json.loads(r.text), f, indent=4)
        else:
            print(f"pokemon {poke_id} is already in the machine")
    elif api == "https://pokeapi.glitch.me/v1/pokemon/":
        if f'{poke_id}.json' not in os.listdir(folder2):
            pokemon_path = os.path.join(folder2, f"{poke_id}.json")

            r = requests.get(f"{api}{poke_id}")

            if r.status_code != 200:
                raise Exception

            with open(pokemon_path, "w") as f:
                json.dump(r.json()[0], f, indent=4)
        else:
            print(f"pokemon {poke_id} is already in the machine")
    else:
        raise Exception


def catch_range(first_catch=1, last_catch=None, api="https://pokeapi.co/api/v2/pokemon/"):
    """
    Gets every pokemon in the given range. If both parameters are ignored, gets every pokemon
    :param first_catch: Defines the start of the range (Default is 1)
    :param last_catch: Defines the end of the range. If ignored catches every pokemon
    :param api: Defines the API to get the data 'https://pokeapi.co/api/v2/pokemon/' (dafault)
    'https://pokeapi.glitch.me/v1/pokemon/'
    :return:
    """
    folder = "pokemon2"  # complex API
    folder2 = "pokemon"  # simple API

    if api == "https://pokeapi.co/api/v2/pokemon/":
        if first_catch <= 0:
            first_catch = 1

        if last_catch == None:
            catch_all(first_catch)
        else:
            current_index = first_catch
            for i in range(first_catch, last_catch + 1):
                if f'{current_index}.json' not in os.listdir(folder):
                    pokemon_path = os.path.join(folder, f"{current_index}.json")

                    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{current_index}")

                    if r.status_code != 200:
                        raise Exception

                    with open(pokemon_path, "w") as f:
                        json.dump(json.loads(r.text), f, indent=4)

                    current_index += 1
                else:
                    print(f"File '{current_index}.json' is already present in the machine")
                    current_index += 1
    elif api == "https://pokeapi.glitch.me/v1/pokemon/":
        if first_catch <= 0:
            first_catch = 1

        if last_catch is None:
            catch_all(first_catch)
        else:
            current_index = first_catch
            for i in range(first_catch, last_catch + 1):
                if f'{current_index}.json' not in os.listdir(folder2):
                    pokemon_path = os.path.join(folder2, f"{current_index}.json")

                    r = requests.get(f"{api}{current_index}")

                    if r.status_code != 200:
                        raise Exception

                    with open(pokemon_path, "w") as f:
                        json.dump(json.loads(r.text), f, indent=4)

                    current_index += 1
                else:
                    print(f"File '{current_index}.json' is already present in the machine")
                    current_index += 1
    else:
        raise Exception


def poke_parse(p1, p2):
    """
    Loads the stats of the pokemon
    :param p1: The loaded JSON file from the main API folder
    :param p2: The path of the file from the secondary API folder
    :return:
    """
    height = p1["height"]
    # original height is in decimeters. Multiply by .1 to convert it to meters.
    height = round(height * 0.1, 2)

    weight = p1["weight"]
    # original weight is in hectograms. Multiply by .1 to convert to Kg
    weight = round(weight * 0.1, 2)

    number = p1["id"]
    base_xp = p1["base_experience"]
    hp = p1["stats"][0]["base_stat"]
    attack = p1["stats"][1]["base_stat"]
    defense = p1["stats"][2]["base_stat"]
    special_attack = p1["stats"][3]["base_stat"]
    special_defense = p1["stats"][4]["base_stat"]
    speed = p1["stats"][5]["base_stat"]

    if p2 is None:
        name = p1["forms"][0]["name"]
        male = None
        female = None
        gen = 8
        species = None
        description = None
    else:
        name = p2["name"]
        if "-" in name:
            name = name.split(" - ")[0]
        if len(p2["gender"]) > 0:
            male = p2["gender"][0]
            female = p2["gender"][1]
        else:
            male = None
            female = None

        gen = p2["gen"]
        sprite = str(p2["sprite"])
        description = p2["description"]
        species = p2["species"]

    return name, number, base_xp, hp, attack, defense, special_attack, \
           special_defense, speed, height, weight, description, species, male, female, gen


def abilities_parse(file):
    """
    Parses the ability of the pokemon
    :param file: File of the pokemon (ex: 1.json)
    :return:
    """
    normal_ability = file["abilities"][0]["ability"]["name"]
    if len(file["abilities"]) < 2:
        hidden_ability = None
    else:
        normal_ability = file["abilities"][0]["ability"]["name"]
        hidden_ability = file["abilities"][1]["ability"]["name"]

    return normal_ability, hidden_ability


def types_parse(file):
    """
    Parses the type(s) of the pokemon
    :param file:
    :return:
    """
    type1 = file["types"][0]["type"]["name"]
    if len(file["types"]) < 2:
        type2 = None
    else:
        type1 = file["types"][0]["type"]["name"]
        type2 = file["types"][1]["type"]["name"]

    return type1, type2


def load_file_complex(pokemon_index):
    """
    Loads the files scraped from the complex API
    :param pokemon_index: Index of the pokemon
    :return:
    """
    folder1 = "pokemon2"  # complex API

    filename = f"{pokemon_index}.json"
    x = os.path.join(folder1, filename)

    if x not in os.listdir(folder1):
        try:
            single_catch(pokemon_index)
        except:
            print("Pokemon not found!")

    try:
        with open(x, "r") as f:
            a = json.load(f)
    except FileNotFoundError:
        print("File not Found")
        return None

    return a


def load_file_simple(pokemon_index):
    """
    Loads the files scraped from the simple API
    :param pokemon_index: Index of the pokemon
    :return:
    """
    folder2 = "pokemon"  # simple API

    filename = f"{pokemon_index}.json"
    y = os.path.join(folder2, filename)

    if y not in os.listdir(folder2):
        try:
            single_catch(pokemon_index, "https://pokeapi.glitch.me/v1/pokemon/")
        except:
            print("Pokemon not found!")

    try:
        with open(y, "r") as f:
            b = json.load(f)
    except FileNotFoundError:
        print("File not Found")
        return None

    return b


############################################################
def insert_pokemon(pokemon_index):
    """
    Inserts the selected pokemon in the database
    :param pokemon_index: index of the pokemon to insert
    :return:
    """
    file1 = load_file_complex(pokemon_index)
    file2 = load_file_simple(pokemon_index)

    stats = poke_parse(file1, file2)

    cursor = DB.cursor()

    cursor.execute("INSERT INTO pokemon (ID, name, base_xp, hp, attack, defense, special_attack, special_defense, speed, height, weight, description, species, male, female, generation) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (stats[1], stats[0], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7],
                    stats[8], stats[9],
                    stats[10], stats[11], stats[12], stats[13], stats[14], stats[15]))
    DB.commit()
    cursor.close()

    return cursor.lastrowid


#########################
def check_pokemon(p):
    """
    Checks if the POKEMON already has an entry on the Database
    :param p: Index of the pokemon
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM pokemon WHERE ID=%s LIMIT 1", (p,))
    check = cursor.fetchall()
    return bool(check), check[0][0] if check else None


def check_abilities(a):
    """
    Checks if an ABILITY already has an entry on the Database
    :param a: Name of the ability
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM abilities WHERE ability_name=%s LIMIT 1", (a,))
    check = cursor.fetchall()
    return bool(check), check[0][0] if check else None


def check_types(t):
    """
    Checks if a TYPE already has an entry on the Database
    :param t: Name of the type
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM types WHERE type_name=%s LIMIT 1", (t,))
    check = cursor.fetchall()
    # print(check)
    return bool(check), check[0][0] if check else None


def check_ability_relation(p, a):
    """
    Checks if there is already a relation between the pokemon and the ability
    :param p: pokemonID
    :param a: abilityID
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM relAbilitiesPokemon WHERE pokemonID=%s AND abilityID=%s", (p, a))
    check = cursor.fetchall()

    return bool(check), check[0][0] if check else None


def check_type_relation(p, t):
    """
    Checks if there is already a relation between the pokemon and the type
    :param p: pokemonID
    :param t: typeID
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM relTypesPokemon WHERE pokemonID=%s AND typeID=%s", (p, t))
    check = cursor.fetchall()

    return bool(check), check[0][0] if check else None


############################################################
def insert_ability(ability_name, ability_type):
    """
    Inserts the ability of the pokemon and marks it as either normal or hidden
    :param ability_name: Name of the ability
    :param ability_type: Type of the ability (Normal or Hidden)
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("INSERT INTO abilities (ability_name, ability_type) VALUES (%s, %s)", (ability_name, ability_type))
    DB.commit()

    cursor.close()

    return cursor.lastrowid


def insert_types(value):
    """
    Inserts the type(s) of the pokemon into the table
    :param value: Type(s) of the pokemon
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("INSERT INTO types (type_name) VALUES (%s)", (value,))
    DB.commit()

    cursor.close()

    return cursor.lastrowid


def insert_rel_abilities(pokemon_id, ability_id):
    """
    Makes the relation with the pokemon and the ability
    :param pokemon_id: ID of the pokemon
    :param ability_id: ID of the ability
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("INSERT INTO relAbilitiesPokemon (pokemonID, abilityID) VALUES (%s, %s)", (pokemon_id, ability_id))
    DB.commit()
    cursor.close()


def insert_rel_types(pokemon_id, type_id):
    """
    Makes the relation with the pokemon and the type.
    :param pokemon_id: ID of the pokemon
    :param type_id: ID of the type
    :return:
    """
    cursor = DB.cursor()

    cursor.execute("INSERT INTO relTypesPokemon (pokemonID, typeID) VALUES (%s, %s)", (pokemon_id, type_id))
    DB.commit()
    cursor.close()


def insert_all(poke_id):
    """
    Inserts the pokemons in the database.
    :param poke_id: The first pokemon to be inserted in the database.
    Every pokemon that comes after will also be inserted
    :return:
    """
    while True:
        file1 = load_file_complex(poke_id)
        file2 = load_file_simple(poke_id)

        poke_parse(file1, file2)
        types = types_parse(file1)
        abilities = abilities_parse(file1)

        #####################
        # checks if the pokemon already has an entry in the database, if not, it creates it.
        if check_pokemon(poke_id)[0] is True:
            p_id = check_pokemon(poke_id)[1]
        else:
            p_id = insert_pokemon(poke_id)

        print(f"pokemon id: {p_id}")

        # checks if the abilities already have an entry in the database...
        c = 1  # to keep track of the ability type. If there are more than one, the first is always the "normal" type
        for i in abilities:
            if i:
                if c == 1:
                    value = "normal"
                else:
                    value = "hidden"
                if check_abilities(i)[0] is False:
                    a_id = insert_ability(i, value)
                    if check_ability_relation(p_id, a_id)[0] is False:
                        insert_rel_abilities(p_id, a_id)
                else:
                    a_id = check_abilities(i)[1]
                    if check_ability_relation(p_id, a_id)[0] is False:
                        insert_rel_abilities(p_id, a_id)
            c += 1

        # checks if the type...
        for i in range(2):
            val = types[i]
            if check_types(types[i])[0] is False:
                if types[i] is not None:
                    t_id = insert_types(val)
                    if check_type_relation(p_id, t_id)[0] is False:
                        insert_rel_types(p_id, t_id)
            else:
                t_id = check_types(types[i])[1]
                if check_type_relation(p_id, t_id)[0] is False:
                    insert_rel_types(p_id, t_id)

        poke_id += 1


def get_images(num):
    """
    Gets the HD picture (portrait) and sprite of a single pokemon
    :param num: ID of the pokemon
    :return:
    """
    a = load_file_complex(num)
    b = load_file_simple(num)

    portrait = b["sprite"]
    sprite = a["sprites"]["front_default"]

    portrait_folder = "images/portraits"
    sprite_folder = "images/sprites"
    filename_portrait = f"{str(num)}.png"
    filename_sprite = f"{str(num)}.png"
    portrait_path = os.path.join(portrait_folder, filename_portrait)
    sprite_path = os.path.join(sprite_folder, filename_sprite)

    r = requests.get(portrait, stream=True)

    print(r.status_code)

    if filename_portrait not in portrait_path:
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(portrait_path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            print("Something went wrong.")
    else:
        print("Image already present locally")

    r2 = requests.get(sprite, stream=True)
    if filename_sprite not in sprite_path:
        if r2.status_code == 200:
            r2.raw.decode_content = True

            with open(sprite_path, 'wb') as f:
                shutil.copyfileobj(r2.raw, f)
        else:
            print("Something went wrong.")
    else:
        print("Image already present locally")


def get_all_images(first_index=1):
    """
    Scrapes the HD images (portraits) of the pokemon and their respective sprites. (Saved in different folders)
    :param first_index: Select the starting point for the crawler
    :return:
    """
    portrait_folder = "images/portraits"
    sprite_folder = "images/sprites"

    while True:
        a = load_file_complex(first_index)
        b = load_file_simple(first_index)

        portrait = b["sprite"]
        sprite = a["sprites"]["front_default"]

        filename_portrait = f"{str(first_index)}.png"
        filename_sprite = f"{str(first_index)}.png"
        portrait_path = os.path.join(portrait_folder, filename_portrait)
        sprite_path = os.path.join(sprite_folder, filename_sprite)

        r = requests.get(portrait, stream=True)

        print(r.status_code)

        if filename_portrait not in portrait_folder:
            if r.status_code == 200:
                r.raw.decode_content = True

                with open(portrait_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                raise Exception
        else:
            print("Image already available locally")

        r2 = requests.get(sprite, stream=True)
        if filename_sprite not in sprite_folder:
            if r2.status_code == 200:
                r2.raw.decode_content = True

                with open(sprite_path, 'wb') as f:
                    shutil.copyfileobj(r2.raw, f)
            else:
                raise Exception
        else:
            print("Image already available locally")

        first_index += 1


def get_sprites(first_index):
    """
    Scrapes only the sprites
    :param first_index: Starting point of the crawler
    :return:
    """
    sprite_folder = "images/sprites"

    while True:
        a = load_file_complex(first_index)

        sprite = a["sprites"]["front_default"]
        filename_sprite = f"{str(first_index)}.png"
        sprite_path = os.path.join(sprite_folder, filename_sprite)

        r2 = requests.get(sprite, stream=True)

        print(r2.status_code)

        if filename_sprite not in sprite_folder:
            if r2.status_code == 200:
                r2.raw.decode_content = True

                with open(sprite_path, 'wb') as f:
                    shutil.copyfileobj(r2.raw, f)
            else:
                raise Exception
        else:
            print("Image already available locally")

        first_index += 1


def get_portraits(first_index):
    """
    Scrapes only the portraits (HD pics) of the pokemon
    :param first_index: Starting point of the crawler
    :return:
    """
    portrait_folder = "images/portraits"

    while True:
        a = load_file_simple(first_index)
        portrait = a[1]["sprite"]

        filename_portrait = f"{str(first_index)}.png"
        portrait_path = os.path.join(portrait_folder, filename_portrait)

        r = requests.get(portrait, stream=True)

        if filename_portrait not in portrait_folder:
            if r.status_code == 200:
                r.raw.decode_content = True

                with open(portrait_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                raise Exception
        else:
            print("Image already available locally")

        first_index += 1


insert_all(1)
