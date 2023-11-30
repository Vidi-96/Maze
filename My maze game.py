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
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XX
"X 
"XXXXX
"X   X
"X   X
"X   X
"X
"X
"X
"X
"X
"X
"X
"X
"X
"X
"XX
"X
"X
"X
"X
"X
"X
"X
"X
