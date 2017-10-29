"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  """


  no = problem.getStartState()
  if (problem.isGoalState(no)):
    return []
  
  pilha = util.Stack()
  pilha.push((no, []))
  
  explorados = []
  
  while not pilha.isEmpty():
    (no, caminho) = pilha.pop()
    
    if problem.isGoalState(no):
        return caminho
    
    explorados.append(no)
    for filho in problem.getSuccessors(no):
        if (filho[0] not in explorados):
            pilha.push((filho[0], caminho + [filho[1]]))

  return []

def breadthFirstSearch(problem):

    no = problem.getStartState()
    if (problem.isGoalState(no)):
        return []

    fila = util.Queue()
    fila.push((no, []))

    explorados = []

    while not fila.isEmpty():
        (no, caminho) = fila.pop()

        if problem.isGoalState(no):
            return caminho

        explorados.append(no)
        for filho in problem.getSuccessors(no):
            if (filho[0] not in explorados):
                fila.push((filho[0], caminho + [filho[1]]))

    return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"

  no = (problem.getStartState(), (), 0)
  fila = util.PriorityQueue()
  fila.push(no,  0)
  visitados = []

  while not fila.isEmpty():
      node, acoes, custo = fila.pop()

      if problem.isGoalState(node):
          return acoes

      visitados.append(node)

      for filho in problem.getSuccessors(node):
          pos, direcao, passo = filho
          if not pos in visitados:
              fila.push((pos, acoes + (direcao,), custo + passo), custo + passo)
  return []



def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"

  fila = util.PriorityQueue()
  visitados = []
  fila.push((problem.getStartState(), ()), heuristic(problem.getStartState(), problem))
  while not fila.isEmpty():
      atual, acoes = fila.pop()
      if atual in visitados: continue
      visitados = visitados + [atual]
      if problem.isGoalState(atual):
          return acoes
      for filho, direcao, custo in problem.getSuccessors(atual):
          if not filho in visitados:
              novaAcoes = acoes + (direcao, )
              fila.push((filho, novaAcoes),
                          problem.getCostOfActions(novaAcoes) + heuristic(filho, problem))


  return []


    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


