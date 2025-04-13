


import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)


turtle.register_shape("Images/Girl_right.gif")
turtle.register_shape("Images/Gir_left.gif")
turtle.register_shape("Images/Sparkle.gif")
turtle.register_shape("Images/Wall.gif")


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
          self.shape("Images/Girl_right.gif")
          self.color("blue")
          self.penup()
          self.speed(0)
          self.white = 0

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

          self.shape("Images/Gir_left.gif")

          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)

               
     def go_right(self):

          move_to_x = player.xcor() + 24
          move_to_y = player.ycor()
          
          self.shape("Images/Girl_right.gif")

          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)

     def is_collision(self, other):
          a = self.xcor()-other.xcor()
          b = self.ycor()-other.ycor()
          distance = math.sqrt((a ** 2) + (b ** 2))

          if distance < 5:
               return True
          else:
               return False

class Sparkle(turtle.Turtle):
     def __init__(self, x, y):
          turtle.Turtle.__init__(self)
          self.shape("Images/Sparkle.gif")
          self.color("white")
          self.penup()
          self.speed(0)
          self.white = 100
          self.goto(x, y)

     def destroy(self):
          self.goto(2000, 2000)
          self.hideturtle()


levels = [""]


level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX            XXX",
"X  XXXXXXX   XXXXXX   XXX",
"X            XXXXXX   XXX",
"XXXXXXXXXX   XX S     XXX",
"XXXXXXXXXX   XXXXXX   XXX",
"X                XXXXXXXX",
"X    XXXXXXXXX   XXXXXXXX",
"X    XXXXXXXXX          X",
"X         S             X",
"X    XXXXXXXXXXXXXX     X",
"X    XXXXXXXXXXXXXX     X",
"X         XXXXXXXXX     X",
"XXXXX     XXXXX         X",
"XXXXX     XXXXX         X",
"XXXXX     XXXXX    XXXXXX",
"X         XXXXX  S XXXXXX",
"XS        XXXXXXXXXXXXXXX",
"XXXXX                XXXX",
"XXXXXX               XXXX",
"XXXXXXXXXXXXXXXXX    XXXX",
"XXXXXXXXXXXXXXXXX    XXXX",
"X S   XXXXXXXXXXX    XXXX",
"X                       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]


treasures = []


levels.append(level_1)


def setup_maze(level):
            for y in range(len(level)):
                for x in range(len(level[y])):


                    character = level[y][x]

                    screen_x = -288 + (x * 24)
                    screen_y = 288 - (y * 24)


                    if character == "X":
                        pen.goto(screen_x, screen_y)
                        pen.shape("Images/Wall.gif")
                        pen.stamp()

                        walls.append((screen_x, screen_y))


                    if character == "P":
                             player.goto(screen_x, screen_y)

                             
                    if character == "S":
                         sparkles.append(Sparkle(screen_x, screen_y))


pen = Pen()
player = Player()


walls = []
sparkles = []


setup_maze(levels[1])
print (walls)


turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


wn.tracer(0)


while True:


     for sparkle in sparkles:
          if player.is_collision(sparkle):

               player.white += sparkle.white
               print ("Player White: {}".format(player.white))

               sparkle.destroy()

               sparkles.remove(sparkle)



     wn.update()