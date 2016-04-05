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
    possible = {}
    for i in range(1,10):
        possible[i] = 0
        if check_all(board, x, y, i):
            possible[i] = i
    if board[y][x] != 0:
        possible[(board[y][x])] = 0
    return possible
        
def possibleEntries(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, 10):
        possibilityArray[x] = 0
    
    #For horizontal entries
    for y in range (0, 9):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    #For vertical entries
    for x in range (0, 9):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
    #For squares of three x three
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6
    for x in range (k, k + 3):
        for y in range (l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1          
    
    for x in range (1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray


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
    
    possiblities = {}
    
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
        
        # get all the possibilities for i,j
        possiblities = fill(board, j, i)

        
        # go through all the possibilities and call the the function
        # again and again
        for x in range (1, 10):
            if possiblities[x] != 0:
                board[i][j] = possiblities[x]
                #file.write(printFileBoard(board))
                solver(board)
        # backtrack
        board[i][j] = 0
    
        
    
solver(board)

        
