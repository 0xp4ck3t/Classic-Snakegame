from turtle import Turtle

move_distance = 20


class Snakes:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[len(self.segment) - 1]

    def create_snake(self):
        x = 0
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(x, 0)
            self.segment.append(snake)
            x -= 20

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):

        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
            self.segment[i].showturtle()

        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
