'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: SearchPath objects are used to return the solution of a search problem 

When searching, we need to store a node's...
1. vertex
2. cost
3. parent
4. heuristic g(n), h(n), g(n) + h(n)
'''

# Node objects store data used when exploring nodes

class Node:
    def __init__(self, vertex, parent=None, cost=0, heuristic=0):
        self.vertex = vertex
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __str__(self):
        return "'" + self.vertex + "'" if self.parent == None else "'" + self.vertex + "','" + self.parent + "',cost=" + str(self.cost) + ",heuristic=" + str(self.heuristic)