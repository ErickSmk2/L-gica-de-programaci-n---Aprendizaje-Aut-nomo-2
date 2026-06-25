import tkinter as tk

class View:
    # Constructor to initialize the view
    def __init__(self, controller):
        self.controller = controller

        # Create main window
        self.window = tk.Tk()
        self.window.title("Adivina el número")
        self.window.geometry("300x350")

        # Title label
        self.label = tk.Label(self.window, text="Piensa en un número del 1 al 100")
        self.label.pack(pady=10)

        # Number display
        self.number_label = tk.Label(self.window, text="", font=("Arial", 20))
        self.number_label.pack(pady=10)

        # Attempt counter
        self.intentos_label = tk.Label(self.window, text="Intentos: 0")
        self.intentos_label.pack(pady=5)

        # Buttons
        tk.Button(self.window, text="Es mayor", command=self.greater).pack(pady=5)
        tk.Button(self.window, text="Es menor", command=self.lesser).pack(pady=5)
        tk.Button(self.window, text="Correcto", command=self.correct).pack(pady=5)

        # Restart button
        tk.Button(self.window, text="Reiniciar", command=self.restart).pack(pady=10)

    # Show number
    def show_number(self, numero):
        self.number_label.config(text=f"¿Es {numero}?")

    # Show attempts
    def show_tried(self, tried):
        self.intentos_label.config(text=f"Intentos: {tried}")

    def greater(self):
        self.controller.response_user("mayor")

    def lesser(self):
        self.controller.response_user("menor")

    def correct(self):
        self.controller.response_user("correcto")

    # Restart function
    def restart(self):
        self.controller.restart_game()

    def start(self):
        self.window.mainloop()