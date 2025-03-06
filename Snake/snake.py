from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0
}

class Snake:
    """Klasa reprezentująca węża."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Tworzy początkowe segmenty węża."""
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Dodaje nowy segment węża na podanej pozycji."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        """Resetuje węża do stanu początkowego."""
        for segment in self.segments:
            segment.goto(1000, 1000)  # Przeniesienie poza ekran
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Dodaje segment do ogona węża."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Porusza wężem."""
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Zmienia kierunek ruchu węża na góra."""
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        """Zmienia kierunek ruchu węża na dół."""
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        """Zmienia kierunek ruchu węża na lewo."""
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        """Zmienia kierunek ruchu węża na prawo."""
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])
