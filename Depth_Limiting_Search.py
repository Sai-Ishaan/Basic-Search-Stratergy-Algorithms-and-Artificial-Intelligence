#Depth Limited with constant Depth value
from collections import deque
import matplotlib.pyplot as plt

class Problem:
    def __init__(self, grid, initial, goal):
        self.grid = grid
        self.initial_state = initial
        self.goal_state = goal
     
    def is_goal(self, state):
        return state == self.goal_state
    def expand(self, state):
        movements = [(0,-1),(0,1),(1,0),(-1,0)]
        valid = []
        for move in movements:
            new_x = state[0] + move[0]
            new_y = state[1]+move[1]
            if 0<=new_x<len(self.grid) and 0<=new_y<len(self.grid[0]) and self.grid[new_x][new_y] == 0:
                valid.append((new_x, new_y))
        return valid        
     
def dls(problem, depth_limit):
        return recursive_dls(problem.initial_state, problem, depth_limit)
def recursive_dls(node, problem, depth_limit):
        if problem.is_goal(node):
            return [node]
        elif depth_limit == 0:
            return "cutoff"
        else:
            for child in problem.expand(node):
                res = recursive_dls(child, problem, depth_limit-1)
                if res == "cutoff":
                    continue
                elif res != "failure":
                    return [node] + res
            return "failure"
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
initial_position = (0,0)
goal_position = (4,4)

problem = Problem(grid, initial_position, goal_position)

depth = 9
path = dls(problem, depth)

if path == "failure":
    print("No path found")
elif path  == "cutoff":
    print("Search cut off in between")
else:
    print("Path found:",path)           

