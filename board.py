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

    def get_color(self):
        return self.color

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
