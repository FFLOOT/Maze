


import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)
wn.tracer(0)


images = ["Images/Girl_right.gif", "Images/Gir_left.gif",
          "Images/Sparkle.gif", "Images/Wall.gif",
          "Images/Enemy_right.gif", "Images/Enemy_left.gif"]
for image in images:
     turtle.register_shape(image)


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

class Enemy(turtle.Turtle):
     def __init__(self, x, y):
          turtle.Turtle.__init__(self)
          self.shape("Images/Enemy_left.gif")
          self.color("blue")
          self.penup()
          self.speed(0)
          self.white = 25
          self.goto(x, y)
          self.direction = random.choice(["up", "down", "left", "right"])

     def move(self):
          if self.direction == "up":
               dx = 0
               dy = 24
          elif self.direction == "down":
               dx = 0
               dy = -24
          elif self.direction == "left":
               dx = -24
               dy = 0
               self.shape("Images/Enemy_left.gif")
          elif self.direction == "right":
               dx = 24
               dy = 0
               self.shape("Images/Enemy_right.gif")
          else:
               dx = 0
               dy = 0



          if self.is_close(player):
               if player.xcor() < self.xcor():
                    self.direction = "left"
               elif player.xcor() > self.xcor():
                    self.direction = "right"
               elif player.xcor() > self.ycor():
                    self.direction = "down"
               elif player.xcor() > self.ycor():
                    self.direction = "up"




          move_to_x = self.xcor() + dx
          move_to_y = self.ycor() + dy


          if (move_to_x, move_to_y) not in walls:
               self.goto(move_to_x, move_to_y)
          else:

               self.direction = random.choice(["up", "down", "left", "right"])


          turtle.ontimer(self.move, t=random.randint(250, 400))

     def is_close(self, other):
          a = self.xcor()-other.xcor()
          b = self.ycor()-other.ycor()
          distance = math.sqrt((a ** 2) + (b ** 2) )

          if distance < 75:
               return True
          else:
               return False 

     def destroy(self):
          self.goto(2000, 2000)
          self.hideturtle()


levels = [""]


level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE           XXX",
"X  XXXXXXX   XXXXXX   XXX",
"X            XXXXXX   XXX",
"XXXXXXXXXX   XX S     XXX",
"XXXXXXXXXX   XXXXXX   XXX",
"X                XXXXXXXX",
"X    XXXXXXXXX   XXXXXXXX",
"X    XXXXXXXXX          X",
"X         S    E        X",
"X    XXXXXXXXXXXXXX     X",
"X    XXXXXXXXXXXXXX     X",
"X         XXXXXXXXX     X",
"XXXXX     XXXXX         X",
"XXXXX     XXXXX         X",
"XXXXX     XXXXX    XXXXXX",
"X         XXXXX  S XXXXXX",
"XS        XXXXXXXXXXXXXXX",
"XXXXX                XXXX",
"XXXXXX   E           XXXX",
"XXXXXXXXXXXXXXXXX    XXXX",
"XXXXXXXXXXXXXXXXX    XXXX",
"X S   XXXXXXXXXXX    XXXX",
"X                       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]


sparkles = []


enemies = []


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


                    if character == "E":
                         enemies.append(Enemy(screen_x, screen_y))


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


for enemy in enemies:
     turtle.ontimer(enemy.move, t=250)


while True:


     for sparkle in sparkles:
          if player.is_collision(sparkle):

               player.white += sparkle.white
               print ("Player White: {}".format(player.white))

               sparkle.destroy()

               sparkles.remove(sparkle)

     if not sparkles:
          print("🎉 All sparkles collected! Game Over!")
          break


     for enemy in enemies:
          if player.is_collision(enemy):
               print("Player dies!")

     wn.update()