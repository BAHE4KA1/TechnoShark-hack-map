from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешает CORS-запросы. Настройте по необходимости.

# Глобальные переменные для хранения данных
map_data = {}


@app.route('/send_map_data', methods=['POST'])
def receive_map_data():
    global map_data
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data received'}), 400

    # Здесь вы можете обработать полученные данные
    map_data = data
    print("Полученные данные:", map_data)

    return jsonify({'status': 'success', 'message': 'Data received'}), 200


@app.route('/get_map_data', methods=['GET'])
def get_map_data():
    return jsonify(map_data)


if __name__ == '__main__':
    app.run(debug=True)

