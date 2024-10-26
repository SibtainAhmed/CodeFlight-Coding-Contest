x = 8
y = 4

desks = 0

matrix = [['.']*y for _ in range(x)]


nextRStart = x
nextCStart = y

for i in range(0,x,2):
    if i+2 == x:
        nextRStart = i
        break
    for j in range(0,y,3):
        if j+3 == y: 
            nextCStart = j

            break
        if y-j >= 2:
            desks += 1
            for k in range(2):
                matrix[i][j+k] = 'X'
            


for i in range(x):
    print(matrix[i])
print(nextRStart, nextCStart)

for j in range(0,nextCStart,2):
    # if i+2 == x:break
    for i in range(nextRStart,x,3):
        # if j+3 == y: break
        if x-i >= 2:
            desks += 1
            for k in range(2):
                matrix[k+i][j] = 'A'
            


for i in range(x):
    print(matrix[i])

print(nextRStart, nextCStart)




for j in range(nextCStart, y,2):
    # if i+2 == x:break
    for i in range(0,x,3):
        if i+3 == x: 
            break
        # if y-j >= 2:
        desks += 1
        for k in range(2):
            matrix[k+i][j] = 'B'
            


for i in range(x):
    print(matrix[i])

print(nextRStart, nextCStart)




for i in range(nextRStart-1, x,2):
    # if i+2 == x:break
    for j in range(nextCStart+1,y,3):
        # if i+3 == x: 
        #     break
        # if y-j >= 2:
        desks += 1
        for k in range(2):
            matrix[i][j+k] = 'C'
            


for i in range(x):
    print(matrix[i])

print(nextRStart, nextCStart)

print('desks: ', desks)