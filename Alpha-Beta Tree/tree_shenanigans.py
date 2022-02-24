'''
Name: Colleen Lemak
Class: CSCI 4740
Professor: Jorge Martinez
Date: 17 February 2022
'''

import math

def minimax(depth, node, maximize, scores, tree_depth, verbose=False):        
    # when a leaf is reached, it returns the score (the depth of the leaves is equal to tree_depth)
    
    if depth == tree_depth:
        if verbose:
            print ("Evaluating score ", scores[node])
            
        return (scores[node])
        
    else:
        # if the node is not a leaf, minimize or maximize the score of its children

        left_child = node * 2 + 0
        right_child = node * 2 + 1
        
        if maximize:
            # returns the max score of its children
                        
            return max(minimax(depth + 1, left_child, False, scores, tree_depth, verbose), minimax(depth + 1, right_child, False, scores, tree_depth, verbose))
     
        else:
            # returns the min score of its children

            return min(minimax(depth + 1, left_child, True, scores, tree_depth, verbose), minimax(depth + 1, right_child, True, scores, tree_depth, verbose)) 


if __name__ == '__main__':

    # the search tree is modeled using a perfect binary tree having 2, 4, 8, 16, 32 leaves 
    # the value of each leaf is the score of the game, these values are stored in a list
    
    scores = [2, 4, 5, 10, 1, 3, 1, 0]

    # the tree depth is log2(total leaves)
    
    tree_depth = math.log(len(scores), 2)

    # minimax

    print ("\nMinimax \n")

    print ("The optimal value for a Max player is", minimax(0, 0, True, scores, tree_depth))
    print ("The optimal value for a Min player is", minimax(0, 0, False, scores, tree_depth))

    # minimax showing the leaves evaluated during the search

    print ("\nMinimax showing the leaves evaluated during the search\n")

    print ("The optimal value for a Max player is", minimax(0, 0, True, scores, tree_depth, True))
    print ("The optimal value for a Min player is", minimax(0, 0, False, scores, tree_depth, True))