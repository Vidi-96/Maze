import turtle
w = turtle.screen()
w.bgcolor("black")
w.title("The Maze of Sorrows")
w.setup(700,700)

class barrier(tutle.Turtle):
    def_init_(self):
        turtle.Turtle._init_(self)
        self.shape("square")
        self.color("white")
        self.barrierup()
        self.speed(0)

levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX"
"X  X                 X  X"
"X  XXXXXXXX  XXXXX   X  X"
"X         X  X   X   X  X"
"XXXXXXXX  X  X   X   X  X"
"X      X  X  X   X   X  X"
"XXXXX  X  X  X   X   X  X"
"X   X  X  X  X   X   X  X" 
"X   X            X   X  X"
"X         XXXXXXXX   X  X"
"XXXXXXXXXXX             X"
"X              XXXXXXXXXX"
"XXX  XXXXXXXXXXX        X"
"X        X  X           X"
"XXXXXX   X  XXXXXXXXX   X"
"X    X   X              X"
"X        XXXXXXXXXX  XXXX"
"XX  XX               XXXX"
"XX  XX   XXXXXXXXXX  XXXX"         
"XX  XX       XXXXXX  XXXX"
"XX  XXXXXXX  XXXXXX  XXXX"
"XXXXXXXXXXX  XX      XXXX"
"XXX          XX      XXXX"
"XXX  XXXXXXXXXX      XXXX"
"XXX  XX              XXXX"
"XXX  XXXXXXXXXXXXXXXXXXXX"

