import time

from helpers import (load_map, show_map) 
from astart import shortest_path

start_time = time.clock()
map_40 = load_map('map-40.pickle')
MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])    
]

def test(shortest_path_function):
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
        
"""Can uncomment this line test too"""
#test(shortest_path)

start, goal = 8, 24
path = shortest_path(map_40, start, goal)
show_map(map_40, start, goal, path)
print (path)
print (time.clock() - start_time)
