
import math

def print_perfect_binary_tree(scores, cur_depth, node_idx, tree_depth):
    if cur_depth == tree_depth:
        print(scores[node_idx], end=", ")
    else:
        left_child = 2 * node_idx + 0
        right_child = 2 * node_idx + 1
        
        print_perfect_binary_tree(scores, cur_depth + 1, left_child, tree_depth)
        print_perfect_binary_tree(scores, cur_depth + 1, right_child, tree_depth)

# when a leaf is reached, it returns the score (the depth of the leaves is equal to tree_depth)
def minimax(depth, node, maximize, scores, tree_depth):
    if depth == tree_depth:
        print("Evaluating score ", scores[node])
        return (scores[node])
    else:
        # if not a leaf, min or max the score
        left_child = node * 2 + 0
        right_child = node * 2 + 1
        
        if(maximize):
            return max(minimax(depth + 1, left_child, False, scores, tree_depth), minimax(depth + 1, right_child, False, scores, tree_depth))
        else:
            return min(minimax(depth + 1, left_child, False, scores, tree_depth), minimax(depth + 1, right_child, False, scores, tree_depth))
        


if __name__ == '__main__':
    scores = [2, 4, 5, 10, 1, 3, 1, 0]
    tree_depth = math.log(len(scores), 2)
    
    # print_perfect_binary_tree(scores, 0, 0, 3)
    
    print("The optimal value for a Max player is ", minimax(0, 0, True, scores, tree_depth))
    print("The optimal value for a Min player is ", minimax(0, 0, False, scores, tree_depth))
