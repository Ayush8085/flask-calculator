from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Creating sqlite
conn = sqlite3.connect('cal.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY,
        operation TEXT NOT NULL,
        num1 REAL NOT NULL,
        num2 REAL NOT NULL,
        result REAL NOT NULL
    )
''')
conn.commit()

# Endpoint for addition
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] + data['num2']

    # Save in sqlite
    conn = sqlite3.connect('cal.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)',
              ('add', data['num1'], data['num2'], result))
    conn.commit()

    return jsonify({'result': result})

# Endpoint for subtraction
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] - data['num2']

    # Save in sqlite
    conn = sqlite3.connect('cal.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)',
              ('subtract', data['num1'], data['num2'], result))
    conn.commit()
    
    return jsonify({'result': result})

# Endpoint for multiplication
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] * data['num2']

    # Save in sqlite
    conn = sqlite3.connect('cal.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)',
              ('multiply', data['num1'], data['num2'], result))
    conn.commit()
    
    return jsonify({'result': result})

# Endpoint for division
@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    if data['num2'] == 0:
        return jsonify({'error': 'Division by zero'}), 400

    result = data['num1'] / data['num2']

    # Save in sqlite
    conn = sqlite3.connect('cal.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)',
              ('divide', data['num1'], data['num2'], result))
    conn.commit()
    
    return jsonify({'result': result})

# Endpoint for division
@app.route('/modulo', methods=['POST'])
def modulo():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    if data['num2'] == 0:
        return jsonify({'error': 'Division by zero'}), 400

    result = data['num1'] % data['num2']

    # Save in sqlite
    conn = sqlite3.connect('cal.sqlite')
    cur = conn.cursor()

    cur.execute('INSERT INTO calculations (operation, num1, num2, result) VALUES (?, ?, ?, ?)',
              ('modulo', data['num1'], data['num2'], result))
    conn.commit()

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
