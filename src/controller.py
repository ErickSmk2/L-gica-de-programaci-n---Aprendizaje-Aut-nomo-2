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
        self.model.increase_tried(candidate)
        self.view.show_number(candidate)
        self.view.show_tried(self.model.tried)

    # Function to handle user responses and update the game state
    def process_response(self, response, candidate):
        
        if response == "mayor":
            self.model.min = candidate +  1
        elif response == "menor":
            self.model.max = candidate - 1
    
    def response_user(self, response):
        candidate = self.model.calculate_candidate()

        if response == "correcto":

            history_text = ", ".join(map(str,self.model.history))

            messagebox.showinfo("Resultado",f"Adiviné en {self.model.tried} intentos\nHistorial: {history_text}")

            return
    
        self.process_response(response, candidate)

        #Update game state
        self.update_game()

    #Restar game function
    def restart_game(self):
        self.model.reset_game()
        self.update_game()
