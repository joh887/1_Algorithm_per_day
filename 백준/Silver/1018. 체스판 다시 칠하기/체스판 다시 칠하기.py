r, c = map(int,input().split())

board = []
change = []
for i in range(r):
    board.append(input())

for i in range(r - 7):
    for j in range(c - 7):
        start_W = 0
        start_B = 0
        for k in range(i, i + 8):
            for l in range(j, j +8):
                if((l + k) % 2 == 0):
                    if(board[k][l] != 'W'):
                        start_W += 1
                    if(board[k][l] != 'B'):
                        start_B += 1
                else:
                    if(board[k][l] != 'B'):
                        start_W += 1
                    if(board[k][l] != 'W'):
                        start_B += 1
        change.append(start_W)
        change.append(start_B)
            
print(min(change))