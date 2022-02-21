
def try_me():
    food_input = input("Do you like Pizza? y/n  " )
    if food_input.lower() == "y":
        print ("You are almost Italian! Mamma mia!!")
    drink_input = input("What is your go-to drink? ")
    choose= input(f'Would you rather drink {drink_input} forever or eat Pizza forever?:')
    print(choose +  " is on its way!")

    return food_input , drink_input, choose
try_me()
