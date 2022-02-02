'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: SearchPath objects are used to return the solution of a search problem.
'''

class SearchPath:
    def __init__(self, path, explored_nodes):
        self._path = path
        self._explored_nodes = explored_nodes

    @property
    def path(self):
        return self._path

    @property
    def explored_nodes(self):
        return self._explored_nodes