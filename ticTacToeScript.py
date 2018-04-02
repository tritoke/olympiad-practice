global board
board = []
	
with open("output.txt", "w") as out:
	with open("input.txt", "r") as input:
		for line in input.readlines():
			tempList = []
			for char in line:
				if char != "\n":
					tempList.append(char)
			board.append(tempList)
	numPlayerWins = [0,0,0]
	for i in board: #this adds up victories on the rows
		a = len(set(i)) - 1
		numPlayerWins[a] += 1
	for i in range(3): #this adds up columns
		tempList = []
		for j in board:
			tempList.append(j[i])
		a = len(set(tempList)) - 1
		numPlayerWins[a] += 1
	diag = [board[0][0], board[1][1], board[2][2]] #this does one of the diagonals
	a = len(set(diag)) - 1
	numPlayerWins[a] += 1
	diag = [board[2][0], board[1][1], board[0][2]] #this does the other
	a = len(set(diag)) - 1
	numPlayerWins[a] += 1
	out.write(str(numPlayerWins[0]) + "\n" +  str(numPlayerWins[1]))
