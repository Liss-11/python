import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print("AssertionError: the number of arguments must be 1")
	exit()
if sys.argv[1].isnumeric():
	if int(sys.argv[1]) == 0:
		print("I'm Zero")
	elif int(sys.argv[1]) % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")
else:
	print("AssertionError: argument is not an integer")
	exit()

