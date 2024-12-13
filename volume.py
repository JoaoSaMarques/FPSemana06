class Volume:
    
    formulas = {
        "Prism": lambda a, b, c : a * b * c,
        "Cylinder": lambda r, h : 3.14 * r**2 * h
    }
    
    def __init__(self):
        pass
    
    def calc(self, name, *param):
        return self.formulas.get(name)(*param)
    
volume = Volume()

print("Volume: ", volume.calc("Prism", 3, 2, 2))