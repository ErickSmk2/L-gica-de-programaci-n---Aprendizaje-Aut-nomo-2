class Model:

    # Construc to initialize the game state
    def __init__(self):
        self.min = 1
        self.max = 100
        self.tried = 0

    # Function to calculate the next candidate number based on the current min and max
    def calculate_candidate(self):
        return (self.min + self.max) // 2

    # Function to increase the number of tries
    def increase_tried(self):
        self.tried += 1