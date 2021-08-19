from http import HTTPStatus

from flask import Flask, jsonify, request

from battleship.ship import Ship

app = Flask(__name__)

ship = Ship()

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    data = request.get_json()

    is_valid_start = ship.start_new_game(data)

    if not is_valid_start:
        return jsonify({}), HTTPStatus.BAD_REQUEST

    return jsonify(data), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    shot = request.get_json()
    x = shot.get('x')
    y = shot.get('y')
    shot_point = [x, y]
    status = ship.do_shot(shot_point)
    if status == 'OUT':
        return jsonify({}), HTTPStatus.BAD_REQUEST

    return jsonify({"result": status}), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    if ship.delete_game():
        return jsonify({}), HTTPStatus.OK

    return jsonify({}), HTTPStatus.BAD_REQUEST