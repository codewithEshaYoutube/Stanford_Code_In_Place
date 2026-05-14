import random
"""
step 1 comp random num hidden
        hint number
step 2 input from user
step 3 decide by if else statements wrong or right
step 4 adding score or not
step 5 repeating loop 5 times



"""

NUM_ROUNDS=5
def main():
    score=0
    print("Welcome to the High-Low Game!")
    for i in range(NUM_ROUNDS):
        print(f"round {i+1}")
        #step1 
        hidden_num=random.randint(1,100)
        hint_num=random.randint(1,100)
        print(f"Your number is {hint_num} ")
        #step 2
        choice=input("Do you think number is lower or higher from computer's number")
        #step 3
        """
        hint_num >= hidden number =user= higher     correct 
        hint_num<=hidden number =user =lower correct

        hint_num >= hidden number =user=lower     in correct 
        hint_num<=hidden number =user =higher  incorrect

        """
        higher_and_correct=choice== "higher" and hint_num > hidden_num
        lower_and_correct=choice=="lower" and hint_num< hidden_num
        if lower_and_correct or higher_and_correct:
            print(f"Yeah you are right the computer number was {hidden_num}")
            score+=1
        else:
            print(f"aww Its incorrect you should try again correct computer number was {hidden_num}")
        print(f"the score is {score}")
        print("")
    print("Thanks for playing")





if __name__ == "__main__":
    main()
