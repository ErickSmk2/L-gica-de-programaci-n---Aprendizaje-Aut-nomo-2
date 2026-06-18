import tkinter as tk

class View:
    # Constructor to initialize the view
    def __init__(self, controller):
        self.controller = controller

        # Create main window
        self.window = tk.Tk()
        self.window.title("Adivina el número")
        self.window.geometry("300x300")

        # Create label 
        self.label = tk.Label(self.window, text="Piensa en un número del 1 al 100")
        self.label.pack(pady=10)

        self.number_label = tk.Label(self.window, text="", font=("Arial", 20))
        self.number_label.pack(pady=10)

        # Create buttons
        greater_button = tk.Button(self.window, text="Es mayor", command=self.greater)
        greater_button.pack(pady=5)

        lesser_button = tk.Button(self.window, text="Es menor", command=self.lesser)
        lesser_button.pack(pady=5)

        correct_button = tk.Button(self.window, text="Correcto", command=self.correct)
        correct_button.pack(pady=5)

    def show_number(self, numero):
        self.number_label.config(text=f"¿Es {numero}?")

    def greater(self):
        self.controller.response_user("mayor")

    def lesser(self):
        self.controller.response_user("menor")

    def correct(self):
        self.controller.response_user("correcto")

    def start(self):
        self.window.mainloop()