from Arduino import Arduino

board = Arduino() # plugged in via USB, serial com at rate 115200
board.pinMode(13, "OUTPUT")

while True:
	board.digitalWrite(13, "LOW")
	time.sleep(1)
	board.digitalWrite(13, "HIGH")
	time.sleep(1)