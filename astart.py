from priorityqueue import PriorityQueue
from helpers import create_node, heuristic_sld, steps_cost 
            
def shortest_path(map,start,goal):
    node = a_star_graph_search(map,start,goal)
    return path(node)    

def a_star_graph_search(map,start,goal):   
    
    """ Frontier and explored must be either a hash or tree for fast 
    membership testing
    
    In this implementation node doesn't need to be hashable because it is 
    not used in membership testing, a dic is used to associate keys and values.
    it may be better to create a Node class"""
    
    node = create_node(start, map, goal)
    if goal == start:
        node["path"].append(start)
        return node
    
    frontier = PriorityQueue()
    frontier.append(node)
    explored = set()
    
    while frontier:
        node = frontier.pop()
        state = node["state"]
        if goal == state:
            return node
        explored.add(state) 
        for action in map.roads[state]: 
            """child_node is not created here to not be called if in explored"""
            if action not in explored and action not in frontier:
                child_node = create_node(action, map, goal, node)
                frontier.append(child_node)
            elif action in frontier:
                child_node = create_node(action, map, goal, node)
                """frontier[child_node] = node with same state as child_node"""
                if child_node['f'] < frontier[child_node]['f']:
                    del frontier[frontier[child_node]]
                    frontier.append(child_node)            
    return None           

def path(node):
        path = []
        while node:
            path.insert(0, node['state'])
            node = node['parent']
        return path
