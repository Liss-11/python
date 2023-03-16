import random

if __name__=='__main__':
    secret_num = random.randint(1, 99)
    answer = ""
    attempts = 0
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    while str(answer) != str(secret_num):
        attempts += 1
        try: input = raw_input
        except NameError: pass
        answer = input("\nWhat's your guess between 1 and 99?\n")
        try:
            int(answer)
            if int(answer) > secret_num:
                print("Too high!")
            elif int(answer) < secret_num:
                print("Too low!")
            else:
                if secret_num == 42:
                  print("The answer to the ultimate question of life, the universe and everything is 42.")
        except:
            if answer == "exit":
                exit(0) 
            else:
                print("That's not a number.")         
    print("Congratulations! You got it on your first try!" if attempts == 1 else "Congratulations, you've got it!\nYou won in "  + str(attempts) + " attempts!")
    exit(0)