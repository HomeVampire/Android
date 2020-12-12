def saddle_point(matrix, r, c):
    minimum=min(matrix[r])
    for i in range(c):
        if minimum == matrix[r][i]:
            column=i
    maximum=0
    row=r
    for i in range(c):
        if maximum <= matrix[i][column]:
            maximum=matrix[i][column]
            row=i
    if matrix[r][column]==matrix[row][column]:
        return matrix[r][column]
    else:
         return -1


def main():
    r=int(input("Enter the number of row & column to be inserted: "))
    c=r
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
    flag=0
    for i in range(r):
        saddle_points=saddle_point(matrix, i, c)
        if saddle_points != -1:
            print("SADDLE POINT=",saddle_points)
            flag=1
    if flag==0:
        print("NO SADDLE POINT")        


main()