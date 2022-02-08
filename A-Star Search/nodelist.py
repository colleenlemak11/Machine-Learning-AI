'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: Implements and defines a List superclass with Queue and PriorityQueue subclasses.
'''

from node import * 

#
# Stack, Queue and PriorityQueue objects are used for the frontier nodes list, List is used for the explored nodes list
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
        if not self.empty():       
            return self._nodes.pop()

        return None

# PriorityQueue is a subclass of List

class PriorityQueue(List):
    def __swap(self, p, q):
        n = self._nodes[p]
        self._nodes[p] = self._nodes[q]
        self._nodes[q] = n

    def __shiftUp(self, parent, child):
        if self._nodes[child].heuristic < self._nodes[parent].heuristic:
            self.__swap(parent, child)

            if parent != 0:
                self.__shiftUp(int((parent - 1)/2), parent)

    def __shiftDown(self, parent):
        last_child = self.elements() - 1
        
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if left_child <= last_child:
            if right_child <= last_child:
                if self._nodes[left_child].heuristic < self._nodes[right_child].heuristic:
                    if self._nodes[parent].heuristic > self._nodes[left_child].heuristic:
                        self.__swap(parent, left_child)
                        self.__shiftDown(left_child)            
                else:
                    if self._nodes[parent].heuristic > self._nodes[right_child].heuristic:
                        self.__swap(parent, right_child)
                        self.__shiftDown(right_child)
            else:
                if self._nodes[parent].heuristic > self._nodes[left_child].heuristic:
                    self.__swap(parent, left_child) 
        
    def add(self, node): 
        super().add(node)
        
        p = self.elements() - 1
        
        self.__shiftUp(int((p - 1)/2), p)

    def remove(self):
        if not self.empty():
            root_node = self._nodes[0]
            last_node = self._nodes.pop()
            
            if not self.empty():
                self._nodes[0] = last_node
                self.__shiftDown(0)                

            return root_node
        
        return None
