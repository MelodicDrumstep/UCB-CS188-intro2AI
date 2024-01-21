# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    is_visited = []
    class Stack_Node:
        def __init__(self, state, path = []):
            self.state = state
            self.path = path
            
    Stack = [Stack_Node(problem.getStartState())]        
    while len(Stack) > 0:
        current_node = Stack.pop()
        if problem.isGoalState(current_node.state):
            return current_node.path
        if current_node.state not in is_visited:
            is_visited.append(current_node.state)
            for next_location in problem.getSuccessors(current_node.state):
                if next_location[0] not in is_visited:
                    next_path = current_node.path + [next_location[1]]
                    Stack.append(Stack_Node(next_location[0], next_path))
    return []
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    is_visited = []
    class Queue_Node:
        def __init__(self, state, path = []):
            self.state = state
            self.path = path
            
    Queue = [Queue_Node(problem.getStartState())]

    # print(is_visited)
    # for s in Queue:
    #     print(s.path)
        
    while len(Queue) > 0:
        current_node = Queue.pop(0)
        #print("current location is: ", current_node.state)
        #print("current path is: ", current_node.path)
        if problem.isGoalState(current_node.state):
            return current_node.path
        if current_node.state not in is_visited:
            is_visited.append(current_node.state)
            for next_location in problem.getSuccessors(current_node.state):
                if next_location[0] not in is_visited:
                    next_path = current_node.path + [next_location[1]]
                    #print("inside the loop, current path is", current_node)
                    Queue.append(Queue_Node(next_location[0], next_path))
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    is_visited = []
    class PQueue_Node:
        def __init__(self, state, path = [], priority = 0):
            self.state = state
            self.path = path       
            self.priority = priority     
    
    PQueue = util.PriorityQueue()
    PQueue.push(PQueue_Node(problem.getStartState()), 0)

    while not PQueue.isEmpty():
        current_node = PQueue.pop()
        #print("current location is: ", current_node.state)
        #print("current path is: ", current_node.path)
        if problem.isGoalState(current_node.state):
            return current_node.path
        if current_node.state not in is_visited:
            is_visited.append(current_node.state)
            for next_location in problem.getSuccessors(current_node.state):
                if next_location[0] not in is_visited:
                    next_path = current_node.path + [next_location[1]]
                    #print("inside the loop, current path is", current_node)
                    PQueue.push(PQueue_Node(next_location[0], next_path, current_node.priority + next_location[2]), current_node.priority + next_location[2])
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    is_visited = []
    class PQueue_Node:
        def __init__(self, state, path = [], priority = 0):
            self.state = state
            self.path = path       
            self.priority = priority     
    
    PQueue = util.PriorityQueue()
    PQueue.push(PQueue_Node(problem.getStartState()), 0)

    while not PQueue.isEmpty():
        current_node = PQueue.pop()
        if problem.isGoalState(current_node.state):
            return current_node.path
        if current_node.state not in is_visited:
            is_visited.append(current_node.state)
            for next_location in problem.getSuccessors(current_node.state):
                if next_location[0] not in is_visited:
                    next_path = current_node.path + [next_location[1]]
                    #print("inside the loop, current path is", current_node)
                    priority = current_node.priority + next_location[2] + heuristic(next_location[0], problem)
                    PQueue.push(PQueue_Node(next_location[0], next_path, current_node.priority + next_location[2]), priority)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
