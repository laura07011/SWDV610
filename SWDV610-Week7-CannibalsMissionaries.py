class SearchSolution:
    def __init__(self, problem, search_method):
        self.problem_name = str(problem)
        self.search_method = search_method
        self.path = []
        self.nodes_visited = 0

    def __str__(self):
        string = "----\n"
        string += "{:s}\n"
        string += "attempted with search method {:s}\n"

        if len(self.path) > 0:

            string += "number of nodes visited: {:d}\n"
            string += "solution length: {:d}\n"
            string += "path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                self.nodes_visited, len(self.path), str(self.path))
        else:
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(self.problem_name, self.search_method, self.nodes_visited)

        return string

from collections import deque

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object
    
    def __init__(self, state, parent=None):
        self.state=state
        self.parent= None
        
# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions
    
    def bfs_search(search_problem):
        initial_state = State(3,3,0)
        if initial_state.is_goal():
            return initial_state
        frontier = list()
        explored = set()
        frontier.append(initial_state)
        while frontier:
            state = frontier.pop(0)
            if state.is_goal():
                return state
            explored.add(state)
            children = successors(state)
            for child in children:
                if (child not in explored) or (child not in frontier):
                    frontier.append(child)
        return None
    
# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
    def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    
    # if no node object given, create a new search from starting state

        if node == None:
            node = SearchNode(search_problem.start_state)
            solution = SearchSolution(search_problem, "DFS")


class CannibalProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        # you might want to add other things to the problem,
        #  like the total number of missionaries (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        self.state=state
        
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string

## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((5, 5, 1))
    #print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)


#from CannibalProblem import CannibalProblem
#from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
problem331 = CannibalProblem((3, 3, 1))
problem541 = CannibalProblem((5, 4, 1))
problem551 = CannibalProblem((5, 5, 1))

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))
