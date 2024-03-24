from turtle import Screen
from snake import Snakes
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
food = Food()
snake = Snakes()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.random_location()
        score.add_score()
        snake.extend()

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        score.game_over()
        game_over = True

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()
            game_over = True
            

screen.exitonclick()
