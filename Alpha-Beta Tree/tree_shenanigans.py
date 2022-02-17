
import math

def print_perfect_binary_tree(scores, cur_depth, node_idx, tree_depth):
    if cur_depth == tree_depth:
        print(scores[node_idx], end=", ")
    else:
        left_child = 2 * node_idx + 0
        right_child = 2 * node_idx + 1
        
        print_perfect_binary_tree(scores, cur_depth + 1, left_child, tree_depth)
        print_perfect_binary_tree(scores, cur_depth + 1, right_child, tree_depth)

if __name__ == '__main__':
    scores = [2, 4, 5, 10, 1, 3, 1, 0]
    tree_depth = math.log(len(scores), 2)
    
    print_perfect_binary_tree(scores, 0, 0, 3)