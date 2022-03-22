from flask import Flask
from settings.database import DB
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/pokemon/', methods=['GET'])
def pokemon():
    cursor = DB.cursor()

    cursor.execute("SELECT * FROM pokemon WHERE ID=%s", (1,))
    return json.dumps(cursor.fetchall()[0])


if __name__ == '__main__':
    app.run()
