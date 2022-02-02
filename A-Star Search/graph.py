'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: This file uses search functions to graph the results.
'''

from nodelist import * 
from searchpath import *

# A* search uses three cost functions
#
# Uniform cost search      f(n) = g(n)
# Greedy Best-first search f(n) = h(n)
# A* search                f(n) = g(n) + h(n)

def uniform_cost_search(g, h):
    return g

def greedy_search(g, h):
    return h

def astar_search(g, h):
    return g + h


#
# Weighted Graph based on a dictionary (key, value), each vertex (key) has a list of edges (value),
# where each edge is represented with a list containing the vertex and the cost
# the heuristic function is used by Greedy Best-first search and A* search
# 
# graph = { vertex-1: [[vertex-1-1, cost-1-1], [vertex-1-2, cost-1-2] ... [vertex-1-m, cost-1-m]],
#           vertex-2: [[vertex-2-1, cost-2-1], [vertex-2-2, cost-2-2] ... [vertex-2-m, cost-2-m]],
#           ...
#           vertex-n: [[vertex-n-1, cost-n-1], [vertex-n-2, cost-n-2] ... [vertex-n-m, cost-n-m]] }
#
# heuristic  = { vertex-1: [heuristic-1],
#                vertex-2: [heuristic-2],
#                ...
#                vertex-n: [heuristic-n] }
#

class Graph:
    def __init__(self, graph=None, heuristic=None):
        self._graph = {} if graph is None else graph
        self._heuristic = {} if heuristic is None else heuristic

    def set_vertex(self, vertex, edges=None, heuristic=None):
        if vertex not in self._graph:
            self._graph[vertex] = [] if edges is None else edges
            self._heuristic[vertex] = [0] if heuristic is None else heuristic

    def __str__(self):
        graph = "\n{"
        
        for vertex in self._graph:
            graph = graph + "\n'" + vertex + "': " + str(self._graph[vertex]) + ", "

        graph = graph[:-2] + "\n}"

        vertices = "{"
        
        for vertex in self._heuristic:
            vertices = vertices + "'" + vertex + "':" + str(self._heuristic[vertex]) + ", "

        vertices = vertices[:-2] + "}\n"
            
        return graph + "\n" + vertices if len(vertices) > 1 else graph

    # search algorithms: Breadth-first search (BFS), Depth-first search (DFS), A* search

    def bfs(self, initial, goal):
        # bfs

    def dfs(self, initial, goal):
        # dfs

    def astar(self, initial, goal, heuristic=astar_search):      
        # a* search