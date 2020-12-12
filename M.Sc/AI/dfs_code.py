import get_input
import numpy as np


# # ! Test dataset
# adjacent_matrix = [[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
# node_list = ['a', 'b', 'c', 'd']

adjacent_matrix, node_list = get_input.get_input()
stack = []
visited_node = []

while 1:
    start_node = input("\nEnter your starting node: ")
    end_node = input("Enter your end node: ")
    # ! remember startnode and end node must match with node names
    if start_node not in node_list and end_node not in node_list:
        print("Wrong input try again...")
    else:
        break

# TODO: PUSH the starting node into stack
stack.append(node_list.index(start_node))

while len(stack) > 0:
    top_element = stack.pop()   # TODO: POP top element from STACK
    if top_element not in visited_node:  # TODO: if the node is visited then we ignore it
        visited_node.append(top_element)

        # TODO: PUSH all nodes into STACK if it is not visited
        for i in range(len(node_list)):
            if adjacent_matrix[top_element][i] == 1 and i not in visited_node:
                stack.append(i)

        if node_list[top_element] == end_node:
            print("We found the end node....")
            print("*** Our visited nodes are ***")

            # TODO: print the output in Style
            for i in visited_node:
                print(f"| ({node_list[i]})", end=" ")
            print("|")
            break
