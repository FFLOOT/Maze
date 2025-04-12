


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

class Player(turtle.Turtle):
     def __init__(self):
          turtle.Turtle.__init__(self)
          self.shape("square")
          self.color("blue")
          self.penup()
          self.speed(0)

     def go_up(self):

          move_to_x = player.xcor()
          move_to_y = player.ycor() + 24


          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)
            
     def go_down(self):
          move_to_x = player.xcor()
          move_to_y = player.ycor() - 24


          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)
               
     def go_left(self):
          move_to_x = player.xcor() - 24
          move_to_y = player.ycor()


          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)
               
     def go_right(self):
          move_to_x = player.xcor() + 24
          move_to_y = player.ycor()


          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)


levels = [""]


level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX            XXX",
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

                        walls.append((screen_x, screen_y))


                    if character == "P":
                             player.goto(screen_x, screen_y)


pen = Pen()
player = Player()


walls = []


setup_maze(levels[1])
print (walls)


turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


wn.tracer(0)


while True:

     wn.update()