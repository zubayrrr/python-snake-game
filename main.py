from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food

    if snake.head.distance(food) < 15:
        print("nom nom")
        food.refresh()
        snake.extend()
        scoreboard.current_score()

    # Collision with wall

    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game = False
        scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()
