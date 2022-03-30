const searchInput = document.querySelector('.searchBar')

function resetConditionsBtn() {
    const typeValue = document.querySelector('#type');
    typeValue.value = 'default';
    const weaknessValue = document.querySelector('#weakness');
    weaknessValue.value='default';
    const abilityValue = document.querySelector('#ability');
    abilityValue.value = 'default';
    const heightValue = document.querySelector('#height');
    heightValue.value = 'default';
    const weightValue = document.querySelector('#weight');
    weightValue.value = 'default';
}


function getValue() {
    return document.getElementById('searchBar').value;
}
function search(pokemonID) {
    let x
    if (isNaN(parseInt(pokemonID)) === false) {
        x = '?pokemonid='
    } else if (pokemonID === null) {
        throw new Error('Empty Value')
    } else {
        x = '?name='
    }

    fetch(`http://localhost:5000/pokemon/preview/${x}${pokemonID}`)
        .then(res => {
            if(res.ok) {
                console.log('SUCCESS')
                return res.json();
            }
            throw new Error('Not successful')
        })
        .then(data => {
            console.log(data["data"]["0"]["id"]);
            let pID = data["data"]["0"]["id"];
            console.log(data["data"]["0"]["name"]);
            let pName = data["data"]["0"]["name"];
            // console.log(data["data"]["0"]["types"]["length"]);
            createCard([pID, pName])

            let pokemonTypes = document.getElementById(`previewTypes-${pID}`) //need fix
            console.log(pokemonTypes)
            if (data["data"]["0"]["types"]["length"] === 1) {
                let pType = data["data"]["0"]["types"]["0"]["NAME"]
                let code = `
                    <p class="rounded ${typeColor(pType).replace("'", '')}">${pType}</p>            
                `
                pokemonTypes.innerHTML = code
                console.log(code)
            } else {
                let pType1 = data["data"]["0"]["types"]["0"]["NAME"]
                let pType2 = data["data"]["0"]["types"]["1"]["NAME"]
                let code = `
                    <p class="rounded ${typeColor(pType1).replace("'", '')}">${pType1}</p>    
                    <p class="rounded ${typeColor(pType2).replace("'", '')}">${pType2}</p>    
                `
                pokemonTypes.innerHTML = code
                console.log(code)
            }
        })
        .catch(error => console.error(error))
}




let pokemon = document.querySelector('.preview');
function createCard([id, name]) {
    let code = `
    <button class="transition transform hover:-translate-y-1" onclick="searchFull(${id})">
        <div style="background-color: #FFFFFF" class="my-6 w-72 h-48 rounded-3xl shadow-lg card">
            <div class="sprite pl-24">
                <img src="images/sprites/${id}.png">
            </div>
            <div class="pokeID">
                <p>Nº${id}</p>
            </div>
            <div class="pokeName">
                <p>${name}</p>
            </div>
            <div id="previewTypes-${id}" class="previewTypes mx-3 px-12">
                
            </div>
        </div>
    </button>
    `
    pokemon.innerHTML += code;
}

function searchFull(pokemonID) {
    let x
    if (isNaN(parseInt(pokemonID)) === false) {
        x = '?id='
    } else if (pokemonID === null) {
        throw new Error('Empty Value')
    } else {
        x = '?name='
    }


    fetch(`http://localhost:5000/pokemon/${x}${pokemonID}`)
        .then(res => {
            if(res.ok) {
                console.log('SUCCESS')
                return res.json();
            }
            throw new Error('Not successful')
        })
        .then(data => {
            // console.log(data)
            let id = data["0"]["ID"];
            let name = data["0"]["name"];
            let species = data["0"]["species"];
            let attack = data["0"]["attack"];
            let defense = data["0"]["defense"];
            let base_xp = data["0"]["base_xp"];
            let special_attack = data["0"]["special_attack"];
            let special_defense = data["0"]["special_defense"];
            let description = data["0"]["description"];
            let speed = data["0"]["speed"];
            let height = data["0"]["height"];
            let weight = data["0"]["weight"];
            let hp = data["0"]["hp"];

            let total = hp + attack + defense + special_attack + special_defense + speed

            let pokeDisplay = document.querySelector('.sidebar')

            let code = `
                <img src="images/portraits/${id}.png">

                <div class="displayID">
                    <p>#${id}</p>
                </div>

                <div class="displayName">
                    <p>${name}</p>
                </div>

                <div class="text-m text-center text-gray-500">
                    <p>${species}</p>
                </div>

                <div class="types text-center py-4"> <!-- Change -->
                    <p class="bg-green-600 mx-12 h-7 rounded-md text-white">Lorem</p>
                    <p class="bg-purple-600 mx-12 h-7 rounded-md text-white self-start">Ipsum</p>
                </div> <!-- ### -->

                <div class="text-center">
                    <p class="font-bold">POKÉDEX ENTRY</p>
                    <p>${description}</p>
                </div>

                <div class="text-center pt-4"> <!-- abilities -->
                    <p class="font-bold">ABILITIES</p>
                    <div class="abilities py-6"> <!-- Change -->
                        <div class="border rounded-3xl border-teal-700 mx-6 py-3 ">
                            <p class="text-left indent-3 text-sm font-bold align-middle">Lorem</p>
                        </div>
                        <p class="border rounded-3xl border-red-700 mx-6 py-3 text-left indent-3 text-sm font-bold">Ipsum<span><i class="material-icons text-gray-400 text-right">visibility_off</i></span></p>
                    </div> <!-- ### -->
                </div>

                <div class="pokeAttributes"> <!-- grid: height, weight, weakness, base exp -->
                    <div> <!-- height -->
                        <p>HEIGHT</p>
                        <p>${height}m</p>
                    </div>
                    <div> <!-- weight -->
                        <p>WEIGHT</p>
                        <p>${weight}Kg</p>
                    </div>
                    <div> <!-- weakness -->
                        <p>WEAKNESSES</p>
                        <p>x y z</p>
                    </div>
                    <div> <!-- base exp -->
                        <p>BASE EXP</p>
                        <p>${base_xp}</p>
                    </div>
                </div>

                <p class="text-center font-bold pt-4 pb-2">STATS</p>
                <div class="stats">
                    <div>
                        <p class="roundStat bg-red-600 ml-3.5">HP</p>
                        <p>${hp}</p>
                    </div>
                    <div>
                        <p class="roundStat bg-orange-500 ml-3.5">ATK</p>
                        <p>${attack}</p>
                    </div>
                    <div>
                        <p class="roundStat bg-yellow-500 ml-3.5">DEF</p>
                        <p>${defense}</p>
                    </div>
                    <div>
                        <p class="roundStat bg-cyan-500 ml-3.5">SpA</p>
                        <p>${special_attack}</p>
                    </div>
                    <div>
                        <p class="roundStat bg-green-500 ml-3.5">SpD</p>
                        <p>${special_defense}</p>
                    </div>
                    <div>
                        <p class="roundStat bg-pink-300 ml-3.5">SPD</p>
                        <p>${speed}</p>
                    </div>
                    <div class="rounded-t-[40%] rounded-b-[40%] bg-indigo-300 w-12">
                        <p class="roundStat bg-indigo-400 ml-1.5">TOT</p>
                        <p>${total}</p>
                    </div>
                </div>
                `
            pokeDisplay.innerHTML = code;
            scroll(0, 0)

        })
        .catch(error => console.error(error))
}


let lastID = 12
function loadMore() {
    search(lastID + 1)
    lastID += 1
}




let item1 = ['1', 'Bulbasaur'];
let item2 = ['2', 'Ivysaur'];
let item3 = ['3', 'Venusaur'];

let item4 = ['4', 'Charmander'];
let item5 = ['5', 'Charmeleon'];
let item6 = ['6', 'Charizard'];

let item7 = ['7', 'Squirtle'];
let item8 = ['8', 'Wartortle'];
let item9 = ['9', 'Blastoise'];

let item10 = ['10', 'Caterpie'];
let item11 = ['11', 'Metapod'];
let item12 = ['12', 'Butterfree'];

createCard(item1);
createCard(item2);
createCard(item3);

createCard(item4);
createCard(item5);
createCard(item6);

createCard(item7);
createCard(item8);
createCard(item9);

createCard(item10);
createCard(item11);
createCard(item12);






function weaknesses(w) {
    switch (w.toLowerCase()) {
        case 'normal':
            return ['Rock', 'Ghost', 'Steel', 'Fighting']
        case 'fighting':
            return ['Flying', 'Poison', 'Psychic', 'Bug', 'Ghost', 'Fairy']
        case 'flying':
            return ['Rock', 'Steel', 'Electric']
        case 'poison':
            return ['Poison', 'Ground', 'Rock', 'Ghost', 'Steel', 'Psychic']
        case 'ground':
            return ['Flying', 'Bug', 'Grass', 'Water', 'Ice']
        case 'rock':
            return ['Fighting', 'Ground', 'Steel', 'Water', 'Grass']
        case 'bug':
            return ['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy', 'Rock']
        case 'ghost':
            return ['Normal', 'Dark', 'Ghost']
        case 'steel':
            return ['Steel', 'Fire', 'Water', 'Electric', 'Fighting', 'Ground']
        case 'fire':
            return ['Rock', 'Fire', 'Water', 'Dragon', 'Ground']
        case 'water':
            return ['Water', 'Grass', 'Dragon', 'Electric']
        case 'grass':
            return ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon', 'Ice']
        case 'electric':
            return ['Ground', 'Grass', 'Electric', 'Dragon']
        case 'psychic':
            return ['Steel', 'Psychic', 'Dark', 'Bug', 'Ghost']
        case 'ice':
            return ['Steel', 'Fire', 'Water', 'Ice', 'Fighting', 'Rock']
        case 'dragon':
            return ['Steel', 'Fairy', 'Ice', 'Dragon']
        case 'fairy':
            return ['Poison', 'Steel', 'Fire']
        case 'dark':
            return ['Fighting', 'Dark', 'Fairy', 'Bug']
        default:
            return 'unknown'
    }
}


function typeColor(type) {
    switch(type.toLowerCase()) {
        case 'normal':
            return 'bg-gray-400'
        case 'fighting':
            return 'bg-red-400 text-white'
        case 'flying':
            return 'bg-purple-200'
        case 'poison':
            return 'bg-fuchsia-700 text-white'
        case 'ground':
            return 'bg-yellow-200'
        case 'rock':
            return 'bg-amber-100'
        case 'bug':
            return 'bg-lime-600'
        case 'ghost':
            return 'bg-purple-900 text-white'
        case 'steel':
            return 'bg-slate-500 text-white'
        case 'fire':
            return 'bg-amber-600 text-white'
        case 'water':
            return 'bg-blue-500 text-white'
        case 'grass':
            return 'bg-green-700 text-white'
        case 'electric':
            return 'bg-yellow-500 text-white'
        case 'psychic':
            return 'bg-pink-600 text-white'
        case 'ice':
            return 'bg-cyan-300'
        case 'dragon':
            return 'bg-indigo-500 text-white'
        case 'fairy':
            return 'bg-pink-300'
        case 'dark':
            return 'bg-zinc-900 text-white'
        default:
            return ''
    }
}





















