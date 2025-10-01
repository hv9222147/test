# file = open("python/demo.txt","w")
# file.write("hello world!\n")
# file.write("file handling in python ")
# file.close()

# file = open("python/demo.txt","r")
# content = file.read()
# print(content)
# file.close()




# try:
#     with open("python/demo.txt","r+") as file:
#         values = file.read().strip()  
#         if values:
#             print("previous values:", values)
        
      
#         v1 = input("Enter first no.: ")
#         v2 = input("Enter second no.: ")
#         print("The input values are:", v1, v2)
#         file.write(v1 + " " + v2) 

# except FileNotFoundError:
#     print("The file is not found. First create a new txt file.")







import heapq

# ==============================
# CONFIGURATION
# ==============================

ROWS = 10
COLS = 10

# Map symbols
EMPTY = "."
ROCK = "R"
TREE = "T"
WATER = "~"
MEDICAL_DEPOT = "H"
AMMO_DEPOT = "A"

# Characters
COMMANDER = "C"
WARRIOR = "W"
MEDIC = "M"
SUPPLY = "P"

# ==============================
# MAP CREATION
# ==============================
def create_map():
    grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    # Some obstacles
    grid[2][3] = ROCK
    grid[4][4] = TREE
    grid[6][2] = WATER
    grid[8][8] = ROCK

    # Depots
    grid[0][0] = MEDICAL_DEPOT
    grid[0][9] = AMMO_DEPOT

    return grid

# ==============================
# TEAM CLASS
# ==============================
class Character:
    def _init_(self, name, symbol, x, y, health=100, ammo=10):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.health = health
        self.ammo = ammo

    def position(self):
        return (self.x, self.y)

# ==============================
# A* PATHFINDING
# ==============================
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(grid, start, goal):
    (x1, y1) = start
    (x2, y2) = goal

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
            path.reverse()
            return path

        neighbors = [(current[0]+1, current[1]),
                     (current[0]-1, current[1]),
                     (current[0], current[1]+1),
                     (current[0], current[1]-1)]

        for nx, ny in neighbors:
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if grid[nx][ny] not in [ROCK, WATER]:  # cannot pass
                    tentative_g = g_score[current] + 1
                    if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                        came_from[(nx, ny)] = current
                        g_score[(nx, ny)] = tentative_g
                        f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)
                        heapq.heappush(open_set, (f_score[(nx, ny)], (nx, ny)))
    return []

# ==============================
# GAME LOGIC
# ==============================
def print_map(grid, team):
    temp = [row[:] for row in grid]
    for member in team:
        x, y = member.position()
        temp[x][y] = member.symbol
    for row in temp:
        print(" ".join(row))
    print("\n")

def move_character(grid, character, target):
    path = a_star(grid, character.position(), target)
    if path:
        for step in path:
            character.x, character.y = step
            print(f"{character.name} moved to {step}")
    else:
        print(f"{character.name} cannot reach {target}")

# ==============================
# MAIN
# ==============================
if __name__ == "_main_":
    grid = create_map()

    # Create team
    commander = Character("Commander", COMMANDER, 5, 1)
    warrior1 = Character("Warrior1", WARRIOR, 5, 2)
    warrior2 = Character("Warrior2", WARRIOR, 5, 3)
    medic = Character("Medic", MEDIC, 6, 1)
    supply = Character("Supply", SUPPLY, 6, 2)

    team = [commander, warrior1, warrior2, medic, supply]

    # Print initial map
    print("Initial Map:")
    print_map(grid, team)

    # Example moves
    move_character(grid, medic, (0, 0))   # Medic goes to medical depot
    move_character(grid, supply, (0, 9))  # Supply goes to ammo depot
    move_character(grid, warrior1, (8, 7)) # Warrior moves toward enemy

    print("\nFinal Map:")
    print_map(grid, team)
