from flask import Flask
from settings.database import DB
import json
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/pokemon/preview/', methods=['GET'])
def pokemon():
    args = request.args.to_dict()
    data = []
    conditions = []

    for arg in args:
        conditions.append(f"{arg}=%s")
        data.append(args.get(arg))

    filters = " AND ".join(conditions)

    query = """
    SELECT rtp.pokemonID, p.name, JSON_ARRAYAGG(JSON_OBJECT('ID', t.ID, 'NAME', t.type_name))
    FROM relTypesPokemon AS rtp
    INNER JOIN pokemon AS p ON rtp.pokemonID = p.ID
    INNER JOIN types AS t ON rtp.typeID = t.ID
    """

    query = " ".join([query, "WHERE", filters, "GROUP BY rtp.pokemonID"])

    cursor = DB.cursor()

    cursor.execute(query, tuple(data))
    # return json.dumps(cursor.fetchall())

    to_return = []
    for pID, pName, pTypes in cursor.fetchall():
        to_return.append({"id": pID,
                          "name": pName,
                          "types": json.loads(pTypes)})
    return {"data": to_return}



@app.route('/pokemon/', methods=['GET'])
def pokemon_all():
    args = request.args.to_dict()
    data = []
    conditions = []

    query = "SELECT * FROM pokemon WHERE"
    for arg in args:
        conditions.append(f"{arg}=%s")
        data.append(args.get(arg))

    filters = " AND ".join(conditions)

    query = " ".join([query, filters])
    cursor = DB.cursor(dictionary=True)
    cursor.execute(query, tuple(data))

    return json.dumps(cursor.fetchall())


if __name__ == '__main__':
    app.run()
