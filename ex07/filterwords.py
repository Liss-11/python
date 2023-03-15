import sys
import string

if __name__=='__main__':
    if len(sys.argv) != 3:  
        print("ERROR, incorrect number of arguments!")
        print("You must enter one string and one positive number without decimals")
        exit(1)
    if sys.argv[1].isnumeric():
        print("ERROR, The first arguments must be a string")
        exit(1)
    try:
        int(sys.argv[2])
        transform = str.maketrans('', '', string.punctuation)
        all_words = (sys.argv[1].translate(transform)).split()
        words = [word for word in all_words if len(word) > int(sys.argv[2])]
        print(words)
    except:
        print("ERROR, The second argument must be a number [positive and without decimals]")
        exit(1)
    sys.exit()



    

