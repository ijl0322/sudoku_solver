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
                            
def fill(board, x, y, num):
    if board[y][x] != 0:
        return board
    for i in range(1,10):
        if i != num and check_all(board, x, y, i):
            board[y][x] = i
            return board


board = [[0,4,0,6,3,9,0,5,0],\
         [0,0,0,0,0,0,0,0,0],\
         [0,9,3,0,0,0,2,6,0],\
         [0,0,9,3,0,1,4,0,0],\
         [0,0,8,0,0,0,7,0,0],\
         [2,0,0,0,4,0,0,0,8],\
         [0,2,0,9,0,4,0,3,0],\
         [0,0,4,0,0,0,9,0,0],\
         [9,0,0,2,0,3,0,0,5]]
         

solution = board[:]                   
#print_board(board)

def main():
    solution = board[:]  
    x = 0
    y = 0

    while x < 8 or y < 8 :
        print x, y
        result = fill(solution, x, y, solution[y][x])
        if result == None:
            if x <= 8 and x > 0:
                x -= 1
            elif x == 0 and y > 0:
                x = 8
                y -= 1  
    
        #go forward

        else:
            solution = result     
            if x < 8:
                x += 1
            elif x == 8 and y < 8:
                x = 0
                y += 1

        print_board(solution)         

    
    
main()

