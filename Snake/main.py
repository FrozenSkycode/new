from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def run_game():
    """Główna pętla gry."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Ustawienie nasłuchiwania klawiszy
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_active = True
    while game_active:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Kolizja z jedzeniem
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase()

        # Kolizja ze ścianą
        if (snake.head.xcor() > 295 or snake.head.xcor() < -295 or 
            snake.head.ycor() > 295 or snake.head.ycor() < -295):
            scoreboard.reset()
            snake.reset()

        # Kolizja z ogonem
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()

if __name__ == "__main__":
    run_game()
