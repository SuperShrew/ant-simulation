class Ant:
    def __init__(self, type, coords):
        self.type = type
        self.has_food = False
        self.age = 0
        self.coords = coords
        if self.type == "worker":
            self.lifespan = 300
        elif self.type == "soldier":
            self.lifespan = 400
        elif self.type == "queen":
            self.lifespan = 9*10**9
            self.food_amount = 0
            self.next_ant = "worker"
    
    def tick(self, env):
        self.age += 1
        if self.type == "worker":
            