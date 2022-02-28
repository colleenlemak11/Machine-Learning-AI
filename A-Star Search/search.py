'''
Name: Colleen Lemak
Course: CSCI 4740
Professor: Jorge Martinez Ladron de Guevara
File Description: Test file which runs our algorithms and functions of code.
'''

from graph import * 

# print the solution to the search problem
   
def print_solution(text, search):
    s = ""
    
    cost = 0

    while not search.path.empty():
        node = search.path.remove()
        
        s = s + node.vertex + "-"
        
        cost = cost + node.cost

    print (text + " " + s[:-1] + " with cost " + str(cost) + " after exploring " + str(search.explored_nodes) + " nodes")

		
if __name__ == '__main__':

    # Graph for uninformed search: BFS, DFS, UCS (page 62)
    
    g1 = Graph()

    # map from Metro to San Ignacio
    g1.set_vertex('A', [['B',18]])
    g1.set_vertex('B', [['C',18], ['D',18]])
    g1.set_vertex('C', [['E',72]])
    g1.set_vertex('D', [['H',270]])
    g1.set_vertex('E', [['F',126], ['H',126]])
    g1.set_vertex('H', [['I',234]])
    g1.set_vertex('F', [['I',18]]) # I is goal state
    g1.set_vertex('I', [])
    

    
    # g1.set_vertex('S', [['A',5], ['B',2], ['C',4]])
    # g1.set_vertex('A', [['D',9], ['E',4]])
    # g1.set_vertex('B', [['G',6]])
    # g1.set_vertex('C', [['F',2]])
    # g1.set_vertex('D', [['H',5]])
    # g1.set_vertex('E', [['G',6]])
    # g1.set_vertex('F', [['G',1]])
    # g1.set_vertex('G', [])
    # g1.set_vertex('H', [])

    print (g1)

    # print ("Uninformed search \n")
    # print_solution ("Breadth-first search", g1.bfs('A', 'I'))
    # print_solution ("Depth-first search  ", g1.dfs('A', 'I'))
    print_solution ("A* search f(n)=g(n) ", g1.astar('A', 'I', uniform_cost_search))
        
    # Graph for informed search: UCS, Greedy Best-first search, A* search (page 112)
   
    # g2 = Graph()

    # g2.set_vertex('S', [['A',1], ['B',5], ['C',8]], [8])
    # g2.set_vertex('A', [['D',3], ['E',7], ['G',9]], [8])
    # g2.set_vertex('B', [['G',4]], [4])
    # g2.set_vertex('C', [['G',5]], [3])
    # g2.set_vertex('D', [], [999])
    # g2.set_vertex('E', [], [999])
    # g2.set_vertex('G', [], [0])

    # print(g2)

    # print ("Informed search \n")
    # print_solution("A* search default f(n)   ", g2.astar('S', 'G'))
    # print_solution("A* search f(n)=g(n)+h(n) ", g2.astar('S', 'G', astar_search))
    # print_solution("A* search f(n)=g(n)      ", g2.astar('S', 'G', uniform_cost_search))
    # print_solution("A* search f(n)=h(n)      ", g2.astar('S', 'G', greedy_search))

    # # Graph in A* Applications (page 26)
    
    # g3 = Graph()

    # g3.set_vertex('A', [['B',6], ['F',3], ['G',5]], [8])
    # g3.set_vertex('B', [['A',6], ['C',3], ['D',2]], [8])
    # g3.set_vertex('C', [['B',3], ['D',1], ['E',5]], [5])
    # g3.set_vertex('D', [['B',2], ['C',1], ['E',8]], [7])
    # g3.set_vertex('E', [['C',5], ['D',8], ['I',5], ['J',5]], [3])
    # g3.set_vertex('F', [['A',3], ['G',1], ['H',7]], [6])
    # g3.set_vertex('G', [['A',5], ['F',1], ['I',3]], [5])
    # g3.set_vertex('H', [['F',7], ['I',2]], [3])
    # g3.set_vertex('I', [['E',5], ['G',3], ['H',2], ['J',3]], [1])
    # g3.set_vertex('J', [['E',5], ['I',3]], [0])

    # print (g3) 

    # print_solution ("A* search f(n)=g(n)      ", g3.astar('A', 'J', uniform_cost_search))
    # print_solution ("A* search f(n)=h(n)      ", g3.astar('A', 'J', greedy_search))
    # print_solution ("A* search f(n)=g(n)+h(n) ", g3.astar('A', 'J', astar_search))

    # print ("")
    
    # # Maze from A* search applications (page 12)
    
    # m1 = Graph()

    # m1.set_vertex('A', [['B',1]], [18])
    # m1.set_vertex('B', [['C',1]], [17])
    # m1.set_vertex('C', [['D',1]], [16])
    # m1.set_vertex('D', [['E',1]], [15])
    # m1.set_vertex('E', [['F',1]], [14])
    # m1.set_vertex('F', [['G',1]], [13])
    # m1.set_vertex('G', [['H',1]], [12])
    # m1.set_vertex('H', [['I',1]], [11])
    # m1.set_vertex('I', [['J',1]], [10])
    # m1.set_vertex('J', [['R1',1], ['L1',1]], [9])
    # m1.set_vertex('R1', [['R2',1]], [8])   
    # m1.set_vertex('R2', [['R3',1]], [7])
    # m1.set_vertex('R3', [['R4',1]], [6])     
    # m1.set_vertex('R4', [['R5',1]], [5])   
    # m1.set_vertex('R5', [['R6',1]], [6])
    # m1.set_vertex('R6', [['R7',1]], [7])     
    # m1.set_vertex('R7', [['R8',1]], [8])   
    # m1.set_vertex('R8', [['R9',1]], [9])
    # m1.set_vertex('R9', [['R10',1]], [10])     
    # m1.set_vertex('R10', [['R11',1]], [11])
    # m1.set_vertex('R11', [['R12',1]], [10])                 
    # m1.set_vertex('R12', [['R13',1]], [9])
    # m1.set_vertex('R13', [['R14',1]], [8])
    # m1.set_vertex('R14', [['R15',1]], [7])                 
    # m1.set_vertex('R15', [['R16',1]], [6])
    # m1.set_vertex('R16', [['R17',1]], [5])
    # m1.set_vertex('R17', [['R18',1]], [4])                 
    # m1.set_vertex('R18', [['R19',1]], [3])
    # m1.set_vertex('R19', [['R20',1]], [2])                 
    # m1.set_vertex('R20', [['S',1]], [1])
    # m1.set_vertex('J', [['L1',1]], [9])
    # m1.set_vertex('L1', [['L2',1]], [10])
    # m1.set_vertex('L2', [['L3',1]], [9])
    # m1.set_vertex('L3', [['L4',1]], [8])
    # m1.set_vertex('L4', [['L5',1]], [7])
    # m1.set_vertex('L5', [['L6',1]], [6])
    # m1.set_vertex('L6', [['L7',1]], [5])
    # m1.set_vertex('L7', [['L8',1]], [4])
    # m1.set_vertex('L8', [['L9',1]], [3])
    # m1.set_vertex('L9', [['L10',1]], [2])
    # m1.set_vertex('L10', [['S',1]], [1])
    # m1.set_vertex('S', [], [0])

    # print_solution ("A* search f(n)=g(n)+h(n) ", m1.astar('A', 'S'))
    # print_solution ("A* search f(n)=g(n)      ", m1.astar('A', 'S', uniform_cost_search))
    # print_solution ("A* search f(n)=h(n)      ", m1.astar('A', 'S', greedy_search))



