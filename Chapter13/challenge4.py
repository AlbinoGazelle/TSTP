class Horse():
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

class Rider():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

horsey = Horse("Kentucky", "Brown")
nathan = Rider("Nathan", "280")

print(horsey.breed)