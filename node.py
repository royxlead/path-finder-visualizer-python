ROWS = 20 
COLS = 20 

class Node:
    def __init__(self, x, y, walkable=True):
        self.x = x  
        self.y = y  
        self.walkable = walkable  
        self.color = (255, 255, 255)  
        self.f_score = float('inf')  
        self.g_score = float('inf')  
        self.h_score = float('inf')  
        self.previous = None  
        self.is_start = False 
        self.is_end = False  

    def set_start(self):
        
        self.is_start = True
        self.color = (0, 0, 255) 

    def set_end(self):
        
        self.is_end = True
        self.color = (255, 165, 0)  

    def __repr__(self):
        return f"Node({self.x}, {self.y})"

    def __lt__(self, other):
        return self.f_score < other.f_score  