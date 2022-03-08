'''
Name: Colleen Lemak
Class: CSCI 4740
Professor: Jorge Martinez
Date: 22 February 2022
'''

class TicTacToe:
    def __init__(self):
        self.grid = [['_','_','_'],
                     ['_','_','_'],
                     ['_','_','_']]

        self.player_turn = 'X'

    def draw(self):
        print ("")
        
        for i in range(0, 3):
            for j in range(0, 3):
                print ("{}|".format(self.grid[i][j]), end="")
            print ("")
        print ("")
        
    def valid_coordinates(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.grid[px][py] != '_':
            return False
        else:
            return True

    def game_over(self):
        # horizontal win: X player wins when ['X', 'X', 'X'] in rows 0 to 2
        
        for i in range(0, 3):
            if (self.grid[i] == ['X', 'X', 'X']):
                return 'X'

        # horizontal win: O player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self.grid[i] == ['O', 'O', 'O']):
                return 'O'

        # vertical win: for i=0 to 2 grid positions [0][i], [1][i], and [2][i] are not '_' and have the same value
        
        for i in range(0, 3):
            if (self.grid[0][i] != '_' and self.grid[0][i] == self.grid[1][i] and self.grid[1][i] == self.grid[2][i]):
                return self.grid[0][i]

                
        # main diagonal win: grid positions [0][0], [1][1], and [2][2] have the same value
        
        if (self.grid[0][0] != '_' and self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2]):
            return self.grid[0][0]

        # second diagonal win: grid positions [0][2], [1][1], and [2][0] have the same value
        
        if (self.grid[0][2] != '_' and self.grid[0][2] == self.grid[1][1] and self.grid[0][2] == self.grid[2][0]):
            return self.grid[0][2]

        # if the grid is full is a forced draw
        
        for i in range(0, 3):
            for j in range(0, 3):
                # if there is an empty position '_', the game is not over
                
                if (self.grid[i][j] == '_'):
                    return None
        
        return '_'

    def play(self):
        while True:
            self.draw()
            
            winner = self.game_over()

            # if the game is over
            
            if winner != None:
                if winner == 'X':
                    print ("X player wins!")
                elif winner == 'O':
                    print ("O player wins!")
                elif winner == '_':
                    print ("The game ends with a forced draw!")
                
                return

            # if it is the X player turn
            
            if self.player_turn == 'X':
                while True:
                    print ("Player X enter coordinates x y: ", end="")

                    px, py = map(int, input().split())

                    if self.valid_coordinates(px, py):
                        self.grid[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print ("Coordinates are not valid! Play again")

            # if it is the O player turn
            
            else:
                while True:
                    print ("Player O enter coordinates x y: ", end="")

                    px, py = map(int, input().split())

                    if self.valid_coordinates(px, py):
                        self.grid[px][py] = 'O'
                        self.player_turn = 'X'
                        break
                    else:
                        print ("Coordinates are not valid! Play again")


if __name__ == "__main__":
    g = TicTacToe()
    g.play()