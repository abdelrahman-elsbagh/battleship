
import numpy as np

class Ship():
    global initial_ships
    global created_ships
    global success_shots
    global board

    initial_ships = {}
    points_list = []
    created_ships = {}
    success_shots = []
    board = np.zeros((10, 10))
    WATER = 'WATER'
    SINK = 'SINK'
    HIT = 'HIT'
    OUT = 'OUT'

    def start_new_game(self, ships):

        initial_ships = ships

        sh_index = 0
        try:
            shapes = initial_ships['ships']
            for shape in shapes:
                sh_index += 1
                points_list = []
                direction = shape.get('direction')
                x = shape.get('x')
                y = shape.get('y')
                size = shape.get('size')
                if direction == 'H':
                    for i in range(size):
                        move = size - i
                        if move > 0:
                            points_list.append([x, ((y) + (move - 1))])
                            if board[y - 1, ((x - 1) + (move - 1))] != 1:
                                board[y - 1, ((x - 1) + (move - 1))] = 1
                            else:
                                return False

                if direction == 'V':
                    for i in range(size):
                        move = size - i
                        if move > 0:
                            points_list.append([(x + (move - 1)), y])
                            if board[(y - 1) + (move - 1), (x - 1)] != 1:
                                board[(y - 1) + (move - 1), (x - 1)] = 1
                            else:
                                return False

                created_ships['ship' + str(sh_index)] = points_list
        except IndexError as error:
            return False

        return True

    def do_shot(self, shot_point):
        status = self.WATER

        if shot_point[0] > 10 or shot_point[1] > 10:
            return self.OUT

        if self.shoted_before(shot_point):
            status = self.HIT
            return status

        for key, ship_points in created_ships.items():
            for point in ship_points:
                if shot_point == point:
                    points = list(created_ships.get(key))
                    status = self.check_shot(points, point, key)
                    return status
        return status

    def check_shot(self, points, shot, ship):
        status = self.WATER
        if self.is_match_shot(points, shot) and self.is_last_point(points):
            self.updated_points(points, shot, ship)
            status = self.SINK
            return status

        if self.shoted_before(shot) or self.is_match_shot(points, shot):
            self.updated_points(points, shot, ship)
            status = self.HIT
            return status

        return status

    def is_match_shot(self, points, shot):
        if shot in points:
            return True
        return False

    def updated_points(self, points, shot, ship):
        if self.is_match_shot:
            global success_shots
            success_shots.append(shot)
            points.pop(points.index(shot))
            created_ships[ship] = points
            return True
        return False

    def shoted_before(self, shot):
        if shot in success_shots:
            return True
        return False

    def is_last_point(self, points):
        if len(points) == 1:
            return True
        return False

    def delete_game(self):
        global initial_ships
        global created_ships
        global board
        global success_shots
        initial_ships = {}
        points_list = []
        success_shots = []
        created_ships = {}
        board = np.zeros((10, 10))
        return True