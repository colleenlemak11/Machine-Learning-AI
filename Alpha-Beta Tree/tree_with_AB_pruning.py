'''
Name: Colleen Lemak
Class: CSCI 4740
Professor: Jorge Martinez
Date: 22 February 2022
'''

import math

PLUS_INFINITE  = +1000
MINUS_INFINITE = -1000

def minimax(depth, node, maximize, scores, tree_depth, alpha, beta, verbose=False):        
    # when a leaf is reached, it returns the score (the depth of the leaves is equal to tree_depth)
    
    if depth == tree_depth:
        if verbose:
            print ("Evaluating score ", scores[node])
            
        return (scores[node])
        
    else:
        # if the node is not a leaf, minimize or maximize the score of its children
        
        if maximize:           
            best_value = MINUS_INFINITE

            for child in [0, 1]:
                child_value = minimax(depth + 1, node * 2 + child, False, scores, tree_depth, alpha, beta, verbose)

                # updates best_value with max(best_value, child_value)
            
                best_value = max(best_value, child_value)

                # updates alpha with max(alpha, best_value)
            
                alpha = max(alpha, best_value)

                # if beta <= alpha, the search ends and returns the best value found
            
                if beta <= alpha:
                    break
                
            return best_value

        else:
            best_value = PLUS_INFINITE
            
            for child in [0, 1]:
                child_value = minimax(depth + 1, node * 2 + child, True, scores, tree_depth, alpha, beta, verbose)

                # updates best_value with min(best_value, child_value)

                best_value = min(best_value, child_value)

                # updates beta with min(beta, best_value)
            
                beta = min(beta, best_value)

                # if beta <= alpha, the search ends and returns the best value found
                
                if beta <= alpha:
                    break
                
            return best_value


if __name__ == '__main__':

    # the search tree is modeled using a perfect binary tree having 2, 4, 8, 16, 32 leaves 
    # the value of each leaf is the score of the game, these values are stored in a list
    
    scores = [2, 4, 5, 10, 1, 3, 1, 0]

    # the tree depth is log2(total leaves)
    
    tree_depth = math.log(len(scores), 2)

    # minimax with Alpha-Beta pruning

    print ("\nMinimax with Alpha-Beta pruning\n")
    
    print("The optimal value for a Max player is", minimax(0, 0, True, scores, tree_depth, MINUS_INFINITE, PLUS_INFINITE))
    print("The optimal value for a Min player is", minimax(0, 0, False, scores, tree_depth, MINUS_INFINITE, PLUS_INFINITE))

    # minimax with Alpha-Beta pruning showing the leaves evaluated during the search

    print ("\nMinimax showing the leaves evaluated during the search\n")

    print("The optimal value for a Max player is", minimax(0, 0, True, scores, tree_depth, MINUS_INFINITE, PLUS_INFINITE, True))
    print("The optimal value for a Min player is", minimax(0, 0, False, scores, tree_depth, MINUS_INFINITE, PLUS_INFINITE, True))