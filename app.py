from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Creating sqlite
conn = sqlite3.connect('cal1.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY,
        operation TEXT NOT NULL,
        expression TEXT NOT NULL,
        result REAL NOT NULL
    )
''')
conn.commit()

# Endpoint for addition
@app.route('/api', methods=['POST'])
def solve():
    data = request.json

    result = eval(data['expression'])

    # Save in sqlite
    conn = sqlite3.connect('cal1.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, expression, result) VALUES (?, ?, ?)',
              ('add', data['expression'], result))
    conn.commit()

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
