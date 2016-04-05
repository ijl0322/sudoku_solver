def print_board(board):
    print "+-------+-------+-------+"    
    for i in range(9):
        string = "| "
        for j in range(9):
            if board[i][j] == 0:
                string += ". "
            else:
                string += str(board[i][j]) + " "
            if j in [2,5,8]:
                string += "| "
        print string
        if i in [2,5,8]:
            print "+-------+-------+-------+"
            
        
        
    
    

board = [[0,4,0,6,3,9,0,5,0],\
         [0,0,0,0,0,0,0,0,0],\
         [0,9,3,0,0,0,2,6,0],\
         [0,0,9,3,0,1,4,0,0],\
         [0,0,8,0,0,0,7,0,0],\
         [2,0,0,0,4,0,0,0,8],\
         [0,2,0,9,0,4,0,3,0],\
         [0,0,4,0,0,0,9,0,0],\
         [9,0,0,2,0,3,0,0,5]]
         
print_board(board)