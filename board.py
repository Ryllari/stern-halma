import pygame as pg


colors = {
    'p1': (0, 100, 30),
    'p2': (200, 30, 30),
    'empty': (255, 255, 255),
}


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def get_position(self):
        return self.x, self.y

    def is_clicking_me(self, pos_x, pos_y):
        return (self.x - 10 <= pos_x <= self.x + 10) and (self.y - 10 <= pos_y <= self.y + 10)

    def is_to_jump(self, other):
        if other.y == self.y:
            return other.x in [self.x -20, self.x + 20]
        elif other.y in [self.y - 20, self.y + 20]:
            return other.x in [self.x - 10, self.x + 10]
        return False

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def render(self, screen):
        return pg.draw.circle(screen, colors[self.color], (self.x, self.y), 10, 10)


def create_line(x, y, color, count):
    line = []
    for i in range(count):
        line.append(Point(x, y, color))
        x += 20
    return line


class Table(object):
    def __init__(self):
        self.board = [
            create_line(820, 200, 'p1', 1),
            create_line(810, 220, 'p1', 2),
            create_line(800, 240, 'p1', 3),
            create_line(790, 260, 'p1', 4),

            create_line(700, 280, 'empty', 13),
            create_line(710, 300, 'empty', 12),
            create_line(720, 320, 'empty', 11),
            create_line(730, 340, 'empty', 10),

            create_line(740, 360, 'empty', 9),

            create_line(730, 380, 'empty', 10),
            create_line(720, 400, 'empty', 11),
            create_line(710, 420, 'empty', 12),
            create_line(700, 440, 'empty', 13),

            create_line(790, 460, 'p2', 4),
            create_line(800, 480, 'p2', 3),
            create_line(810, 500, 'p2', 2),
            create_line(820, 520, 'p2', 1),
        ]

    def render(self, screen):
        for array in self.board:
            for point in array:
                point.render(screen)
        pg.display.flip()

    def get_point_by_coord(self, x, y):
        for i, array in enumerate(self.board):
            for j, point in enumerate(array):
                if point.is_clicking_me(x, y):
                    return point
        return None

    def move_points(self, player_point, other_point):
        other_point.set_color(player_point.get_color())
        player_point.set_color('empty')

    def verify_win(self, playerid):
        if playerid == 1:
            win_board = self.board[-4:]
            for array in win_board:
                for point in array:
                    if point.get_color() != 'p1':
                        return False
            return True
        else:
            win_board = self.board[:4]
            for array in win_board:
                for point in array:
                    if point.get_color() != 'p2':
                        return False
            return True

# ------- Funcoes para melhorar visual -------- #
def view_playertime(screen, font, player):
    pg.draw.rect(screen, (72, 72, 72), (730, 600, 300, 50))
    screen.blit(font.render(f'Vez do Player {player}!', True, (255, 255, 255)), (750, 600))
    pg.display.flip()