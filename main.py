from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# determining the screen size
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# tracer method to turn animation off
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting colliding with food
    if snake.head.distance(food) < 15:
        # increasing score when collides with food
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.reset()
        snake.reset()

    # slicing out the body of snake
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
