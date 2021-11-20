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
