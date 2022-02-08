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

    g1.set_vertex('S', [['A',5], ['B',2], ['C',4]])
    g1.set_vertex('A', [['D',9], ['E',4]])
    g1.set_vertex('B', [['G',6]])
    g1.set_vertex('C', [['F',2]])
    g1.set_vertex('D', [['H',5]])
    g1.set_vertex('E', [['G',6]])
    g1.set_vertex('F', [['G',1]])
    g1.set_vertex('G', [])
    g1.set_vertex('H', [])

    print (g1)

    print ("Uninformed search \n")
    print_solution ("Breadth-first search", g1.bfs('S', 'G'))
    print_solution ("Depth-first search  ", g1.dfs('S', 'G'))
    print_solution ("A* search f(n)=g(n) ", g1.astar('S', 'G', uniform_cost_search))
        
    # Graph for informed search: UCS, Greedy Best-first search, A* search (page 112)
   
    g2 = Graph()

    g2.set_vertex('S', [['A',1], ['B',5], ['C',8]], [8])
    g2.set_vertex('A', [['D',3], ['E',7], ['G',9]], [8])
    g2.set_vertex('B', [['G',4]], [4])
    g2.set_vertex('C', [['G',5]], [3])
    g2.set_vertex('D', [], [999])
    g2.set_vertex('E', [], [999])
    g2.set_vertex('G', [], [0])

    print(g2)

    print ("Informed search \n")
    print_solution("A* search default f(n)   ", g2.astar('S', 'G'))
    print_solution("A* search f(n)=g(n)+h(n) ", g2.astar('S', 'G', astar_search))
    print_solution("A* search f(n)=g(n)      ", g2.astar('S', 'G', uniform_cost_search))
    print_solution("A* search f(n)=h(n)      ", g2.astar('S', 'G', greedy_search))

    # Graph in A* Applications (page 26)
    
    g3 = Graph()

    g3.set_vertex('A', [['B',6], ['F',3], ['G',5]], [8])
    g3.set_vertex('B', [['A',6], ['C',3], ['D',2]], [8])
    g3.set_vertex('C', [['B',3], ['D',1], ['E',5]], [5])
    g3.set_vertex('D', [['B',2], ['C',1], ['E',8]], [7])
    g3.set_vertex('E', [['C',5], ['D',8], ['I',5], ['J',5]], [3])
    g3.set_vertex('F', [['A',3], ['G',1], ['H',7]], [6])
    g3.set_vertex('G', [['A',5], ['F',1], ['I',3]], [5])
    g3.set_vertex('H', [['F',7], ['I',2]], [3])
    g3.set_vertex('I', [['E',5], ['G',3], ['H',2], ['J',3]], [1])
    g3.set_vertex('J', [['E',5], ['I',3]], [0])

    print (g3) 

    print_solution ("A* search f(n)=g(n)      ", g3.astar('A', 'J', uniform_cost_search))
    print_solution ("A* search f(n)=h(n)      ", g3.astar('A', 'J', greedy_search))
    print_solution ("A* search f(n)=g(n)+h(n) ", g3.astar('A', 'J', astar_search))

    print ("")
    
    # Maze from A* search applications (page 12)
    
    m1 = Graph()

    m1.set_vertex('A', [['B',1]], [18])
    m1.set_vertex('B', [['C',1]], [17])
    m1.set_vertex('C', [['D',1]], [16])
    m1.set_vertex('D', [['E',1]], [15])
    m1.set_vertex('E', [['F',1]], [14])
    m1.set_vertex('F', [['G',1]], [13])
    m1.set_vertex('G', [['H',1]], [12])
    m1.set_vertex('H', [['I',1]], [11])
    m1.set_vertex('I', [['J',1]], [10])
    m1.set_vertex('J', [['R1',1], ['L1',1]], [9])
    m1.set_vertex('R1', [['R2',1]], [8])   
    m1.set_vertex('R2', [['R3',1]], [7])
    m1.set_vertex('R3', [['R4',1]], [6])     
    m1.set_vertex('R4', [['R5',1]], [5])   
    m1.set_vertex('R5', [['R6',1]], [6])
    m1.set_vertex('R6', [['R7',1]], [7])     
    m1.set_vertex('R7', [['R8',1]], [8])   
    m1.set_vertex('R8', [['R9',1]], [9])
    m1.set_vertex('R9', [['R10',1]], [10])     
    m1.set_vertex('R10', [['R11',1]], [11])
    m1.set_vertex('R11', [['R12',1]], [10])                 
    m1.set_vertex('R12', [['R13',1]], [9])
    m1.set_vertex('R13', [['R14',1]], [8])
    m1.set_vertex('R14', [['R15',1]], [7])                 
    m1.set_vertex('R15', [['R16',1]], [6])
    m1.set_vertex('R16', [['R17',1]], [5])
    m1.set_vertex('R17', [['R18',1]], [4])                 
    m1.set_vertex('R18', [['R19',1]], [3])
    m1.set_vertex('R19', [['R20',1]], [2])                 
    m1.set_vertex('R20', [['S',1]], [1])
    m1.set_vertex('J', [['L1',1]], [9])
    m1.set_vertex('L1', [['L2',1]], [10])
    m1.set_vertex('L2', [['L3',1]], [9])
    m1.set_vertex('L3', [['L4',1]], [8])
    m1.set_vertex('L4', [['L5',1]], [7])
    m1.set_vertex('L5', [['L6',1]], [6])
    m1.set_vertex('L6', [['L7',1]], [5])
    m1.set_vertex('L7', [['L8',1]], [4])
    m1.set_vertex('L8', [['L9',1]], [3])
    m1.set_vertex('L9', [['L10',1]], [2])
    m1.set_vertex('L10', [['S',1]], [1])
    m1.set_vertex('S', [], [0])

    print_solution ("A* search f(n)=g(n)+h(n) ", m1.astar('A', 'S'))
    print_solution ("A* search f(n)=g(n)      ", m1.astar('A', 'S', uniform_cost_search))
    print_solution ("A* search f(n)=h(n)      ", m1.astar('A', 'S', greedy_search))



	
##    # Maze 2 used in the final exam?
##    
##    m2 = Graph() 
##
##    m2.set_vertex('A', [['B',1]], [18])
##    m2.set_vertex('B', [['C',1]], [17])
##    m2.set_vertex('C', [['D',1]], [16])
##    m2.set_vertex('D', [['E',1]], [15])
##    m2.set_vertex('E', [['F',1]], [14])
##    m2.set_vertex('F', [['L1',1], ['R1',1]], [13])
##    
##    m2.set_vertex('R1', [['R2',1]], [12])   
##    m2.set_vertex('R2', [['R3',1]], [11])
##    m2.set_vertex('R3', [['R4',1]], [10])     
##    m2.set_vertex('R4', [['R5',1]], [9])   
##    m2.set_vertex('R5', [['R6',1]], [8])
##    m2.set_vertex('R6', [['R7',1]], [7])     
##    m2.set_vertex('R7', [['R8',1]], [6])   
##    m2.set_vertex('R8', [['R9',1]], [5])
##    m2.set_vertex('R9', [['R10',1]], [6])     
##    m2.set_vertex('R10', [['R11',1]], [7])
##    m2.set_vertex('R11', [['R12',1]], [8])                 
##    m2.set_vertex('R12', [['R13',1]], [9])
##    m2.set_vertex('R13', [['R14',1]], [10])
##    m2.set_vertex('R14', [['R15',1]], [11])                 
##    m2.set_vertex('R15', [['R16',1]], [12])
##    m2.set_vertex('R16', [['R17',1]], [13])
##    m2.set_vertex('R17', [['R18',1]], [12])                 
##    m2.set_vertex('R18', [['R19',1]], [11])
##    m2.set_vertex('R19', [['R20',1]], [10])
##    m2.set_vertex('R20', [['R21',1]], [9])
##    m2.set_vertex('R21', [['R22',1]], [8])
##    m2.set_vertex('R22', [['R23',1]], [7])
##    m2.set_vertex('R23', [['R24',1]], [6])
##    m2.set_vertex('R24', [['R25',1]], [5])
##    m2.set_vertex('R25', [['R26',1]], [4])
##    m2.set_vertex('R26', [['R27',1]], [3])
##    m2.set_vertex('R27', [['R28',1]], [2])
##    m2.set_vertex('R28', [['S',1]], [1])
##
##    m2.set_vertex('L1', [['L2',1]], [14])
##    m2.set_vertex('L2', [['L3',1]], [15])
##    m2.set_vertex('L3', [['L4',1]], [14])
##    m2.set_vertex('L4', [['L5',1]], [13])
##    m2.set_vertex('L5', [['L6',1]], [12])
##    m2.set_vertex('L6', [['L7',1]], [11])
##    m2.set_vertex('L7', [['L8',1]], [10])
##    m2.set_vertex('L8', [['L9',1]], [9])
##    m2.set_vertex('L9', [['L10',1]], [8])
##    m2.set_vertex('L10', [['L11',1]], [7])
##    m2.set_vertex('L11', [['L12',1]], [6])
##    m2.set_vertex('L12', [['L13',1]], [5])
##    m2.set_vertex('L13', [['L14',1]], [4])
##    m2.set_vertex('L14', [['L15',1]], [3])
##    m2.set_vertex('L15', [['L16',1]], [2])
##    m2.set_vertex('L16', [['S',1]], [1])
##    
##    m2.set_vertex('S', [], [0])
##
##    print("\n")
##	
##    print_solution ("A* search f(n)=g(n)+h(n) ", m2.astar('A', 'S'))
##    print_solution ("A* search f(n)=g(n)      ", m2.astar('A', 'S', uniform_cost_search))
##    print_solution ("A* search f(n)=h(n)      ", m2.astar('A', 'S', greedy_search))
    

##    g4 = Graph()
##
##    g4.set_vertex('A', [['B',1]], [0])
##    g4.set_vertex('B', [['A',1], ['C',1]], [0])
##    g4.set_vertex('C', [['B',1], ['D',1], ['E',1]], [0])
##    g4.set_vertex('D', [['C',1], ['F',1]], [0])
##    g4.set_vertex('E', [['C',1], ['I',1]], [0])
##    g4.set_vertex('F', [['D',1], ['G',1]], [0])
##    g4.set_vertex('G', [['F',1], ['H',1], ['W',1]], [0])
##    g4.set_vertex('H', [['G',1], ], [0])
##    g4.set_vertex('I', [['E',1], ['J',1]], [0])
##    g4.set_vertex('J', [['I',1], ['K',1]], [0])
##    g4.set_vertex('K', [['J',1], ['L',1]], [0])
##    g4.set_vertex('L', [['K',1], ['M',1]], [0])
##    g4.set_vertex('M', [['L',1], ['N',1]], [0])
##    g4.set_vertex('N', [['M',1], ['O',1], ['Q',1]], [0])
##    g4.set_vertex('O', [['N',1], ['P',1]], [0])
##    g4.set_vertex('P', [['O',1]], [0])
##    g4.set_vertex('Q', [['N',1], ['R',1]], [0])
##    g4.set_vertex('R', [['Q',1], ['S',1]], [0])
##    g4.set_vertex('S', [['R',1], ['T',1]], [0])
##    g4.set_vertex('T', [['S',1], ['U',1]], [0])
##    g4.set_vertex('U', [['T',1]], [0])
##    g4.set_vertex('W', [['G',1], ['X',1]], [0])
##    g4.set_vertex('X', [['W',1]], [0])
##    g4.set_vertex('Y', [['W',1], ['Z',1]], [0])
##    g4.set_vertex('Z', [['Y',1]], [0])
##    
##    print(g4)
##
##    print_solution ("A* search f(n)=g(n)+h(n) ", g4.astar('A', 'U'))
##
##    
##    g5 = Graph()
##
##    g5.set_vertex('A', [['B',2], ['E',3]], [11])
##    g5.set_vertex('B', [['A',2], ['C',1], ['F',9]], [6])
##    g5.set_vertex('C', [['B',1]], [20])
##    g5.set_vertex('D', [['E',6], ['F',1]], [1])
##    g5.set_vertex('E', [['A',3], ['D',6]], [7])
##    g5.set_vertex('F', [['B',9], ['D',1]], [0])
##    
##    print(g5)
##
##    print_solution ("A* search f(n)=g(n)+h(n) ", g5.astar('A', 'F'))

