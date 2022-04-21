import random

class CityMap():
    def __init__(self, height, width, houses, max_services):
        self._max_services = max_services
        self._height = height
        self._width = width
        
        self._houses = set()

        for house in houses:
            self._houses.add((house[0], house[1]))
            
        self._services = set()
        
    def __is_a_house(self, row, col):
        return (row, col) in self._houses

    def __is_a_service(self, row, col):
        return (row, col) in self._services

    def __available_positions(self):
        # returns all the available cells in the grid

        positions = set()
        
        for row in range(self._height):           
            for col in range(self._width):
                positions.add((row, col))

        # removes the positions of houses and services
        
        for house in self._houses:
            positions.remove(house)
            
        for service in self._services:
            positions.remove(service)
            
        return positions

    def __get_cost(self, services):
        # calculates the sum of distances from houses to nearest public service
        
        cost = 0
        
        for house in self._houses:
            cost += min(
                abs(house[0] - service[0]) + abs(house[1] - service[1])
                for service in services
            )
            
        return cost

    def __get_neighbors(self, row, col):
        # returns neighbors not containing a house or a public service
        
        candidates = [ (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1) ]
        neighbors = []
        
        for r, c in candidates:
            if (r, c) in self._houses or (r, c) in self._services:
                continue
            if 0 <= r < self._height and 0 <= c < self._width:
                neighbors.append((r, c))
                
        return neighbors

    def hill_climb(self, maximum=100, verbose=False):      
        count = 0

        # initializes the locations of the services randomly
        
        # self._services = set()
         
        # for i in range(self._max_services):
        #     self._services.add(random.choice(list(self.__available_positions())))
            
        # continues until the maximum number of iterations
        
        while count < maximum:
            count += 1
            best_neighbors = []
            best_neighbor_cost = None

            # analyzes the services to reallocate
            
            for service in self._services:
                # analyzes the neighbors of a public service (pharmacy, school, police station, ...)
                
                for replacement in self.__get_neighbors(*service):
                    # generates a neighboring set of services
                    
                    neighbor = self._services.copy()
                    neighbor.remove(service)
                    neighbor.add(replacement)

                    # check if the neighbor is the best so far
                    
                    cost = self.__get_cost(neighbor)
                    
                    if best_neighbor_cost is None or cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # end when the best neighbor is not better than the current state
            
            if best_neighbor_cost >= self.__get_cost(self._services):
                return self._services
            else:
                # moves to a highest-valued neighbor

                if verbose:
                    print ("Better neighbor found with cost ", best_neighbor_cost)
                    
                self._services = random.choice(best_neighbors)

    def random_restart(self, maximum, verbose=False):

        # best_services is a set with the location of the services
        # best_cost is the best_cost so far

        best_services = set()
        
        # repeats hill-climbing a fixed number of times
        
        # for i in range(maximum):
        #
        #    call hill_climb()
        #
        #    if the new cost is lower than the best cost
        #       update best cost and best_services
        #
        #       if verbose
        #          show the new best cost found
        #
        
        return best_services
    
    def print_map(self, services):
        print ("\nCity Map \n")
        
        for i in range(self._height):
            for j in range(self._width):
                if self.__is_a_house(i, j):
                    print ("H", end="")
                elif (i, j) in services:
                    print ("*", end="")
                else:
                    print ("_", end="")

            print (" ")
            
        print ("\nCost is ", self.__get_cost(services), " Services locations ", services, "\n")
           

if __name__=="__main__":
    
    # creates a new city map with houses and services

    city = CityMap(height=5, width=9, houses=[(0,2), (1,8), (3,0), (4, 3)], max_services=2)

    print ("__H______") 
    print ("________H") 
    print ("_________") 
    print ("H________") 
    print ("___H_____")
    
    # runs hill climbing to find the locations of the public services

    print ("\nHill climbing")

    locations = city.hill_climb(verbose=True)

    city.print_map(locations)

    # hill climbing with random restart
    
    print ("Hill climbing with random restart")
    
    locations = city.random_restart(10, verbose=True)

    # city.print_map(locations)