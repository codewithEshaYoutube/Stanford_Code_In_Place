"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
'''
mars_constant =0.387
ask input user (weight on earth)
storing the answer from user
changing data type of answer str--->float
define formula     mars constant multiply with input
round off to 2 decimal points
show up the mars_weight
'''
def main():
 

# CONSTANT
    MARS_MULTIPLE=0.378

    #getting input from user and stored
    Earth_weight=input('Enter a weight on Earth:')
    # typecasting
    Earth_weight_float=float(Earth_weight)
    # defining formula
    Mars_weight= MARS_MULTIPLE * Earth_weight_float
    # round it off
    Mars_weight_rounded=round(Mars_weight,2)
    # show to user
    print("The equivalent weight on Mars: ", Mars_weight_rounded)


if __name__ == "__main__":
    main()
