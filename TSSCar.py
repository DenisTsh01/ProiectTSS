import unittest

#ruta pe care o ia masina va fi primita de catre aceasta sub forma de lista cu date precum "L R"
#masina se afla pe o matrice de n x n dimensiuni si 
class Car:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
    
    def go(self, instructions):
        for instruction in list(instructions):
            self.execute(instruction)
    
    def execute(self, instruction,n=8):
        # n dimensiunea matricii 
        if instruction == "R":
            if self.facing == "N":
                self.facing = "E"
                return 
        
           
            if self.facing == "E":
                self.facing = "S"
                return 
            
            if self.facing == "S":
                self.facing = "W"
                return 
            
            self.facing = "N"
            return 
        
        elif instruction == "L":
            if self.facing == "N":
                self.facing = "W"
                return 
        
            
            if self.facing == "E":
                self.facing = "N"
                return 
       
            if self.facing == "S":
                self.facing = "E"
                return 
            
            self.facing = "S"
            return 

        elif instruction == "M":
            if self.facing == "N":
                self.y += 1
            elif self.facing == "E":
                self.x += 1
            elif self.facing == "S":
                self.y -= 1
            elif self.facing == "W":
                self.x -= 1
        
                # Verificăm dacă mașina a ieșit din matrice
            if self.x < 0:
                self.x = 0
            elif self.x >= n:
                self.x = n - 1
            if self.y < 0:
                self.y = 0
            elif self.y >= n:
                self.y = n - 1