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
            
        
def check_col(board, x, y):
    num = board[y][x]
    for i in range(9):
        if i != y:
            if board[i][x] == num:
                return False
    return True
      
def check_row(board, x, y):
    num = board[y][x]
    for i in range(9):
        if i != x:
            print board[y][i],
            if board[y][i] == num:
                return False
    return True     
    
def check_box(board, x, y):
    num_list = [[0,1,2],[3,4,5],[6,7,8]]
    num = board[y][x]
    print num
    for i in num_list:
        if x in i:
            row = i
        if y in i:
            col = i
    for i in row:
        for j in col:
            if not (i == x and j == y):
                if num == board[j][i]:
                    return False
    return True
            
    
    

board = [[0,4,0,6,3,9,0,5,0],\
         [0,0,0,0,0,0,0,0,0],\
         [0,9,3,0,0,0,2,6,0],\
         [0,0,9,3,0,1,4,0,0],\
         [0,0,8,0,0,0,7,0,0],\
         [2,0,0,0,4,0,0,0,8],\
         [0,2,0,9,0,4,0,3,0],\
         [0,0,4,0,0,0,9,0,0],\
         [9,0,0,2,0,3,0,0,5]]
         
test_case = [[1,3,5,7,2,4,6,8,9],\
             [2,0,0,0,0,0,0,0,0],\
             [3,0,0,0,0,0,0,0,0],\
             [4,0,0,0,0,0,0,0,0],\
             [5,0,0,0,0,0,0,0,0],\
             [6,0,0,0,0,0,0,0,0],\
             [7,0,0,0,0,0,1,2,3],\
             [8,0,0,0,0,0,4,5,6],\
             [9,0,0,0,0,0,7,8,9]]   
                   
#print check_row(test_case, 0, 0) 
print check_box(test_case, 6, 8)        
print_board(test_case)