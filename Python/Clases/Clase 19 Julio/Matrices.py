matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz)

for i in matriz:
    print(i)
print("=============================================")   
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
print("=============================================")   
for i in range(len(matriz)):
    for j in matriz[i]:
        print(j)
print("=============================================")        
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print(" ")       