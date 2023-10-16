str = "unirnavprtrrxtnzr"

#haveanicegeekgame
for s in str:
	print(chr(ord(s) - 13 if ord(s)-13 >= ord('a') else ord(s) - 13 + 26), end ='')

