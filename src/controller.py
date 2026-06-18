from model import Model
from view import View
from tkinter import messagebox

class Controller:
    def __init__(self):
        self.model = Model()
        self.view  = View(self)

        # Initialize the game by showing the first candidate
        self.update_game()

    # Function to update the game state and show the next candidate
    def update_game(self):
        candidate = self.model.calculate_candidate()
        self.model.increase_tried()
        self.view.show_number(candidate)

    # Function to handle user responses and update the game state
    def response_user(self, response):
        candidate  = self.model.calculate_candidate()

        if response == "correcto":
            messagebox.showinfo(
                "Resultado",
                f"Adiviné en {self.model.tried} intentos"
            )
            self.view.window.destroy()

        elif response == "mayor":
            self.model.min = candidate + 1

        elif response == "menor":
            self.model.max = candidate - 1

        # Update the game state and show the next candidate
        self.update_game()