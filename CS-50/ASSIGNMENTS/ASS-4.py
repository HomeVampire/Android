r=int(input("Enter the number of row to be inserted: "))
c=int(input("Enter the number of column to be inserted: "))
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        element=int(input("Enter the Element: "))
        a.append(element)
    matrix.append(a)
print("ROW=",len(matrix))
print("COLOUMN=",len(matrix[0]))
print(matrix)