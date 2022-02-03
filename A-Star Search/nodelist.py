'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: Implements and defines a List superclass with Queue and PriorityQueue subclasses.
'''

from node import * 

#
# Stack, Queue and PriorityQueue objects are as the frontier nodes list, List is used for the explored nodes list
#

# List (superclass)

class List:
    def __init__(self): 
        self._nodes = []

    def empty(self): 
        return len(self._nodes) == 0

    def add(self, node): 
        self._nodes.append(node)

    def remove(self):
        if not self.empty():
            return self._nodes.pop(0)

        return None

    def get(self, vertex):
        for node in self._nodes:
            if node.vertex == vertex:
                return node

        return None
        
    def contains(self, vertex):
        for node in self._nodes:
            if node.vertex == vertex:
                return True

        return False

    def elements(self):
        return len(self._nodes)

    def __str__(self):
        s = "{"
        
        for node in self._nodes:
            s = s + "[" + str(node) + "],"

        s = s[:-1] + "}"

        return s

# Queue is a subclass of List
        
class Queue(List):
    pass

# Stack is a subclass of List
    
class Stack(List): 
    def remove(self):
        # removes the last element of the list
        pass
        # if not self.empty():
        #     return self.nodes.pop(-1)

        # return None

# PriorityQueue is a subclass of List

class PriorityQueue(List):
    def __swap(self, p, q):
        # swaps the value of nodes at positions p and q
        pass

    def __shiftUp(self, parent, child):
        # swaps the child and the parent node while the parent's heuristic is greater that the child's heuristic
        pass

    def __shiftDown(self, parent):
        # swaps the parent with minimum of its left and right child
        pass
        
    def add(self, node): 
        # adds a new node 
        pass

    def remove(self):
        # removes the node with the minimum key (heuristic)
        pass