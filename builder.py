class House:
    def __init__(self, walls = 4) -> None:
        self.floor = True
        self.roof = True
        self.walls = walls
    
    def windows(self, num_windows = 2):
        self.windows = num_windows
        return self
    
    def build_pool(self):
        self.pool = True
        return self
    
    def build_garden(self):
        self.build_garden = True
        return self
    
    def display(self):
        print(self.__dict__)
    
    def __repr__(self) -> str:
        return f"{__class__} ({[key for key in self.__dict__]})"


normal_house = House().windows()
villa_house = House().windows().build_garden().build_pool()
normal_house.display()
villa_house.display()

print(normal_house)
