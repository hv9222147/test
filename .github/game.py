rows = 10
cols = 10

empty = ""
tree =  "T"
rock = "R"
water = "~"
medical_depot = "H" 
ammo_depot = "A"

commandor = "C"
worrier = "W"
medic = "M"
supply = "P"




class create_map():
    grid = [[empty for _ in range(cols)] for _ in range(rows)]
    grid[2][3] = rock
    grid[4][5] = tree
    grid[6][2] = water
    grid[8][8] = rock


    grid[0][0] = medical_depot
    grid[0][9] = ammo_depot



class character:
    def _init_(self,name,symbol,x,y,ammo=10,health=100):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.ammo = ammo
        self.health = health
        
    def position(self):
        return(self.x,self.y)


