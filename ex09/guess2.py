import random
import string


#if __name__=='__main__':
#    secret_num = str(random.randint(1, 99))
 #   answer = -1
 #   print(secret_num)
 #   attempts = 0
 #   print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
 #   answer = input("\nWhat's your guess between 1 and 99?\n")
 #   print(answer)


secret_num = str(random.randint(1, 99))
print(secret_num)
attempts = 0
print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
answer = raw_input("\nWhat's your guess between 1 and 99?\n")
print(answer) 
exit(0)  
  
    