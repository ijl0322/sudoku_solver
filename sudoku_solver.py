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
            
def is_full(board):
    for x in range(0, 9):
        for y in range (0, 9):
            if board[y][x] == 0:
                return False
    return True            
        
def check_col(board, x, y, num):
    #print "\nchecking col......"
    for i in range(9):
        if i != y:
            #print board[i][x],
            if board[i][x] == num:
                return False
    return True
      
def check_row(board, x, y, num):
    #print "\nchecking row......"
    for i in range(9):
        if i != x:
            #print board[y][i],
            if board[y][i] == num:
                return False
    return True     
    
def check_box(board, x, y, num):
    #print "\nchecking box......"
    num_list = [[0,1,2],[3,4,5],[6,7,8]]

    for i in num_list:
        if x in i:
            row = i
        if y in i:
            col = i
    for i in row:
        for j in col:
            if not (i == x and j == y):
                #print board[j][i],
                if num == board[j][i]:
                    return False
    return True
            
def check_all(board, x, y, num):
    if check_row(board, x, y, num) and check_col(board, x, y, num) and check_box(board, x, y, num):
        return True
    return False                    
                            
def fill(board, x, y):
    possible = []
    for i in range(1,10):
        if check_all(board, x, y, i):
            possible.append(i)
    if board[y][x] != 0:
        possible.remove(board[y][x])
    return possible
        
board = [[0,4,0,6,3,9,0,5,0],\
         [0,0,0,0,0,0,0,0,0],\
         [0,9,3,0,0,0,2,6,0],\
         [0,0,9,3,0,1,4,0,0],\
         [0,0,8,0,0,0,7,0,0],\
         [2,0,0,0,4,0,0,0,8],\
         [0,2,0,9,0,4,0,3,0],\
         [0,0,4,0,0,0,9,0,0],\
         [9,0,0,2,0,3,0,0,5]]
         

        
#print_board(board)

def solver(board):
    i = 0
    j = 0
    
    possiblities = []
    
    # if board is full, there is no need to solve it any further
    if is_full(board):
        print("Board Solved Successfully!")
        print_board(board)
        return
    else:
        # find the first vacant spot
        for x in range (0, 9):
            for y in range (0, 9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
    possible = fill(board, j, i)
    if possible != []:
        for num in possible:
            board[i][j] = num
            solver(board)
            
    board[i][j] = 0

    
        
    
solver(board)

#print fill(board,1,0)        
