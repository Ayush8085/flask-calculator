from flask import Flask, request, jsonify, render_template
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

@app.route('/', methods=['GET'])
def home():
    return render_template('calcu.html')


# Endpoint for addition
@app.route('/api', methods=['POST'])
def solve():
    data = request.json


    result = eval(str(data['expression']))
    print(data['expression'])
    print(result)

    # Connect to DB
    conn = sqlite3.connect('cal1.sqlite')
    cur = conn.cursor()
    # Save in sqlite
    cur.execute('INSERT INTO calculations (operation, expression, result) VALUES (?, ?, ?)',
              ('add', data['expression'], result))
    conn.commit()

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
