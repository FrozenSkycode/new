from turtle import Turtle

class Scoreboard(Turtle):
    """Klasa odpowiedzialna za wyświetlanie wyniku gry."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def load_high_score(self):
        """Ładuje najlepszy wynik z pliku, obsługując potencjalne błędy."""
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def display_score(self):
        """Odświeża wyświetlany wynik."""
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", 
                   align="center", font=("Arial", 12, "normal"))

    def increase(self):
        """Zwiększa wynik o 1 i aktualizuje wyświetlanie."""
        self.score += 1
        self.display_score()

    def reset(self):
        """Resetuje wynik oraz zapisuje nowy rekord, jeśli został pobity."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display_score()
