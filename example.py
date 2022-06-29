import board

myboard = board.ExpansionBoard()

while True:
	data = myboard.ser.read()
	if data != None:
		print(data)