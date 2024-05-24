matrix = [

[2,5,7],
[7,8,5],
[6,9,0]


]

print(len(matrix))

final =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      final[j][i] = matrix[i][j]

for y in final:
   print(y)
