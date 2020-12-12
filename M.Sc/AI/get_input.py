import numpy as np


def get_input():
    no_of_nodes = int(input("Enter no. of nodes for tree: "))
    print("Please enter the adjacent matrix for your tree...")

    adjacent_matrix = np.zeros((no_of_nodes, no_of_nodes), dtype=int)
    node_list = []

    for i in range(no_of_nodes):    # TODO: get node name from user
        while 1:
            node = input(f"Enter name for node{i+1}: ")
            if node not in node_list:
                node_list.append(node)
                break
            else:
                print("The node already exist...")

    print("\nPlease enter 0 for 'No' and 1 for 'Yes'...")
    for i in range(len(node_list)):  # TODO: get all connected graph from user(undirected)
        for j in range(len(node_list)):
            # ! remember a node cannot connect with itself
            if node_list[i] == node_list[j] or adjacent_matrix[i][j] == 1:
                continue

            if adjacent_matrix[j][i] == 1:  # ! we tried to get undirected graph
                # ! so if node1 connected with node2 the vice-versa also true
                adjacent_matrix[i][j] = 1
                continue

            while 1:
                check_connection = int(
                    input(f"Is node '{node_list[j]}' connected with '{node_list[i]}': "))

                if check_connection == 1 or check_connection == 0:
                    adjacent_matrix[i][j] = check_connection
                    adjacent_matrix[j][i] = check_connection
                    break
                else:
                    print("Wrong input....try again")

    return adjacent_matrix, node_list


if __name__ == "__main__":
    matrix = get_input()
    print(matrix)
