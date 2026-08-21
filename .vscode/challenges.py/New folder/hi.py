board=[1,2,3,4,5,6,7,8,9]
print(board)
while True:
    p1=int(input("player choose X"))
    board[p1-1]="X"
    
    if (board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]):
    print("X wins!")
    break

    p2=int(input("player choose O"))
    board[p2-1]="O"
    print(board)

    if (board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]):
        print("O wins!")
        break
