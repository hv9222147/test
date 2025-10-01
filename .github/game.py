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
def heuristic(a,b):
    return abs(a[0]-y[0])+ abs(a[1]-y[1])

def a_star(grid,start,goal):
    (x1,y1) = start
    (x2,y2) = goal




def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  
        
        x, y = current
        for nx, ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:  
                tentative_g = g_score[current] + 1
                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = tentative_g
                    f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (f_score[(nx, ny)], (nx, ny)))
    return []