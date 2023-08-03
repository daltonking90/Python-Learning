from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=900, height=700) # default is that middle of screen is 0, 0
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")


game_running = True
while game_running:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.increase_size()

    # wall collision
    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        game_running = False
        score.game_over()

    # tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            score.game_over()


screen.exitonclick()
