matrix=[]
m=int(input('enter number of rows, m = '))
n=int(input('enter number of columns, n = '))

for i in range(m):
    matrix.append([])
    for j in range(n):
        elem=input('enter element: ')
        matrix[i].append(elem)

#print matrix
for i in range(m):
    for j in range(n):
        print (matrix[i][j]),
    print ('\n')

#generate transpose
transpose=[]
for j in range(n):
    transpose.append([])
    for i in range (m):
        ent=matrix[i][j]
        transpose[j].append(ent)

#print transpose
for i in range (n):
    for j in range (m):
        print (transpose[i][j]),
    print ('\n')


