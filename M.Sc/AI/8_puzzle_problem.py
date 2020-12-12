import numpy as np
import math

print("This is your goal state:")
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, ' ']])
print(goal_state)

input_state = [''] * (3**2)
input_state = np.array(input_state)
input_state.shape = (3, 3)
# print(input_state)
print("Now, Enter your elements from top-left:\nEnter space to let a cell empty...")
for i in range(3):
    for j in range(3):
        while 1:
            element = input(f"Enter element for point({i}, {j}): ")
            if element in goal_state and element not in input_state:
                input_state[i][j] = element
                break
            else:
                print("Given data already exist or not matched with output data...")

print("Your input state is:\n", input_state)

misplaced_tiles = 0
manhatten_distance = 0
for i in range(3):
    for j in range(3):
        if goal_state[i][j] != input_state[i][j]:
            misplaced_tiles += 1
            for x1 in range(3):
                for x2 in range(3):
                    if goal_state[i][j] == input_state[x1][x2]:
                        manhatten_distance += math.ceil(
                            math.sqrt((x1-i)**2 + (x2-j)**2))

print("No. of misplaced tiles(h1): ", misplaced_tiles)
print("Manhatten Distance(h2): ", manhatten_distance)
