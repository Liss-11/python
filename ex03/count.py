import sys
import string

def get_characters(param):
	upper = 0
	lower = 0
	punctuation = 0
	space = 0
	total = 0
	for x in param:
		if x.isupper():
			upper += 1
		if x.islower():
			lower += 1
		if x == ' ':
			space += 1
		if x in string.punctuation:
			punctuation += 1
	total = len(param)
	print("The text contains " + str(total) + ", total")
	print("- " + str(upper) + " upper letter(s)")
	print("- " + str(lower) + " lower letter(s)")
	print("- " + str(punctuation) + " punctuation mark(s)")
	print("- "+ str(space) + " space(s)")

def analizer(param):
	try:
		int(param)
		print("AssertionError: argument is not a string")
	except:
		get_characters(param)

def text_analyzer(*args):
	if not args or args[0] == None:
		resp = ""
		while resp == "":
			resp = input("What is the text to analyze?")
		analizer(resp)
	else:
		if len(args) == 1:
			analizer(args[0])
		else:
			print("AssertionError: You have to pass 1 argument")
			exit()


if __name__ == '__main__':
	if len(sys.argv) > 2:
		print("AssertionError: You have to pass 1 argument")
		exit()
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()

