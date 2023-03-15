import sys
import random
import string

if __name__=='__main__':
    secret_num = random.randint(1, 99)
    answer = -1
    print(secret_num)
    attempts = 0
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    #answer = input("\nWhat's your guess between 1 and 99?\n")
    while answer != str(secret_num):
        attempts += 1
        answer = raw_input("\nWhat's your guess between 1 and 99?\n")
        print(answer)
        if answer == 'exit':
            print("Goodbye!")
            exit(0)
        if not isinstance(answer, int):
            print("That's not a number.")
            if answer == "exit":
                print("IS a exit")
            answer = -1
            break
        answer = int(answer)
        if answer > secret_num:
            print("Too high!")
        elif answer < secret_num:
            print("Too low!")
        else:
            if secret_num == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")            
    print("Congratulations! You got it on your first try!" if attempts == 1 else "Congratulations, you've got it!\nYou won in"  + attempts + "attempts!")
    exit(0)

    
           
            


    #si el numero es 42 - poner la cita
    #contar los intentos
    #felicitacion si acierta a la primera
    #indicar si ha dicho mas alto o mas bajo