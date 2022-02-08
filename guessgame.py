#"Author :- Manish Prakash Jadhav"
#"B.Tech Computer Science & Engineering At Daulatrao Aher College Of Engineering,Karad"
#"Dated:- 09-11-2021"

import random
import time
n=int(input("Enter Maximum Limit:- "))
print("Numbers Will Be Generate Between 1 to {} :".format(n))
generated_no=random.randint(1,n)
guess_no=0
while guess_no!=generated_no:
    guess_no=int(input("Enter Your Guess...:-"))
    if guess_no<generated_no:
        print("Guessing...")
        time.sleep(1)
        print("Entered Number Is Small")
        
    elif guess_no>generated_no:
        print("Guessing...")
        time.sleep(1)
        print("Entered Number Is Large")
        
    elif guess_no==generated_no:
        print("Guessing...")
        time.sleep(1)
        print("Congratulation..! You Have Guessed Correct No")

        
        
        
import random
# Create the 'num_guess()' function and pass  𝑛  as a parameter
def num_guess(n):
  # Ask the user to enter a number between 10 and 20 and store it in a variable 'user_guess'.
  user_guess=int(input("enter no between 10 and 20 :"))
  # If 'user_guess' is greater than  𝑛 , return 'You guessed high!' and 'n'.
  if user_guess>n:
    print("you have guess high!")
    return n

  # If 'user_guess' is lower than  𝑛 , return 'You guessed small!' and 'n'.
  elif user_guess<n:
    print("You guessed small!")
    return n

  # If 'user_guess' is equal to  𝑛 , return 'Correct Guess!' and 'n'.
  elif user_guess==n:
    print("Correct Guess!")
    return n


# Generate a random integer between 10 and 20 using randint() function and store it in a variable 'rand_num'
rand_num= random.randint(10,20)
# Call the function num_guess() and pass 'rand_num' as a parameter inside this function
num_guess(rand_num)
