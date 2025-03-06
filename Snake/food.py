from turtle import Turtle
import random

class Food(Turtle):
    """Klasa reprezentująca jedzenie w grze."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Losowo przenosi jedzenie na ekranie."""
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)
