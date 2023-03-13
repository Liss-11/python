import sys
import logging

logger = logging.getLogger()
if len(sys.argv) == 1:
	logger.error("You must enter at least one argument")
	exit()
word = sys.argv[1]
for x in sys.argv[2:]:
	word += (" " + x)
word = word[::-1]
print(word.swapcase())