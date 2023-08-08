from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for addition
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] + data['num2']
    return jsonify({'result': result})

# Endpoint for subtraction
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] - data['num2']
    return jsonify({'result': result})

# Endpoint for multiplication
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = data['num1'] * data['num2']
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
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
