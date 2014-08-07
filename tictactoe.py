from random import randint

board = [[" L "," L "," L "],[" L "," L "," L "],[" L "," L "," L "]]


# for x in range(0, 3):
#     board.append([" L "," L "," L "] )

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def check_range(row, col):
	if row in range(0,3) and col in range(0,3):
		return True
	else :
		return False

def check_isdigit(row,col):
	if row.isdigit() and col.isdigit():
		return True
	else : 
		return False

def check_done(player,board):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
            print player, "win."
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        print player, "win!!!"
        return True

    temp = 0
    for i in range(3):
    	for j in range(3):
    		if board[i][j] != ' L ' :
    			temp += 1

    print temp			
    if temp == 9:
	   print "Draw"
	   return True
    
    return False

def check_same(x,y):
	if board[x][y] == ' L ':
		return True
	else:
		return False


start = True
while start:

	player1 = ' X '
	player2 = ' O '

	print "Turn of 'X'"
	player1_row = raw_input("Guess Row:")
	player1_col = raw_input("Guess Col:")

	while (check_isdigit(player1_row,player1_col) == False):
		player1_row = (raw_input("Wrong Range. Guess Row:"))
		player1_col = (raw_input("Wrong Range. Guess Col:"))

	while ( check_range(int(player1_row),int(player1_col)) == False )or (check_same(int(player1_row),int(player1_col))==False):
		player1_row = (raw_input("Wrong Range. Guess Row:"))
		player1_col = (raw_input("Wrong Range. Guess Col:"))

	
	board[int(player1_row)][int(player1_col)] = player1
	print_board(board)
	done = check_done(player1,board)
	print "Turn of 'O'"
	player2_row = raw_input("Guess Row:")
	player2_col = raw_input("Guess Col:")

	while(check_isdigit(player1_row,player1_col) == False):
		player2_row = raw_input("Wrong Range. Guess Row:")
		player2_col = raw_input("Wrong Range. Guess Col:")		

	while (check_range(int(player2_row),int(player2_col)) == False) or (check_same(int(player2_row),int(player2_col)) ==False ):
		player2_row = raw_input("Wrong Range. Guess Row:")
		player2_col = raw_input("Wrong Range. Guess Col:")
	
	board[int(player2_row)][int(player2_col)] = player2
	print_board(board)

	

	done = check_done(player2,board)

	if done == True :
		start = False
	else :
		start = True
