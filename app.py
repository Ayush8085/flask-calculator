from flask import Flask, request, jsonify
app = Flask(__name__)

# -------------Addition---------------
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    print(data)
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = sum(data['numbers'])
    return jsonify({'result': result})

# -------------Substraction---------------
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['numbers'][0] - sum(data['numbers'][1:])
    return jsonify({'result': result})

# -------------Multiplication---------------
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = 1
    for num in data['numbers']:
        result *= num
    return jsonify({'result': result})

# -------------Division---------------
@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    if 0 in data['numbers'][1:]:
        return jsonify({'error': 'Division by zero'}), 400

    result = data['numbers'][0]
    for num in data['numbers'][1:]:
        result /= num
    return jsonify({'result': result})

# -------------Division---------------
@app.route('/modulo', methods=['POST'])
def mod():
    data = request.json
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['numbers'][0]
    for num in data['numbers'][1:]:
        result /= num
    return jsonify({'result': result})


if __name__=='__main__':
    app.run(debug=True)