


import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


levels = [""]


level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX            XXX",
            "X  XXXXXXX   XXXXXX   XXX",
            "X            XXXXXX   XXX",
            "XXXXXXXXXX   XX       XXX",
            "XXXXXXXXXX   XXXXXX   XXX",
            "X                XXXXXXXX",
            "X    XXXXXXXXX   XXXXXXXX",
            "X    XXXXXXXXX          X",
            "X                       X",
            "X    XXXXXXXXXXXXXX     X",
            "X    XXXXXXXXXXXXXX     X",
            "X         XXXXXXXXX     X",
            "XXXXX     XXXXX         X",
            "XXXXX     XXXXX         X",
            "XXXXX     XXXXX    XXXXXX",
            "X         XXXXX    XXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "XXXXX                XXXX",
            "XXXXXX               XXXX",
            "XXXXXXXXXXXXXXXXX    XXXX",
            "XXXXXXXXXXXXXXXXX    XXXX",
            "X     XXXXXXXXXXX    XXXX",
            "X                       X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
        ]


levels.append(level_1)


def setup_maze(level):
            for y in range(len(level)):
                for x in range(len(level[y])):


                    character = level[y][x]

                    screen_x = -288 + (x * 24)
                    screen_y = 288 - (y * 24)


                    if character == "X":
                        pen.goto(screen_x, screen_y)
                        pen.stamp()


pen = Pen()


setup_maze(levels[1])


while True:
    pass