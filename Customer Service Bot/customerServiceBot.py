import time
from returningCustomer import *
from newCustomer import *


def bot():
    print(
        "Hello Welcome to the [Company Name] support site! Are you a returning customer or new customer?")
    print("[1] Returning Customer \n[2] New Customer")
    responseBot = input(
        "Please enter the number corresponding to your choice: ")

    if responseBot == "1":
        returningCustomer()

    elif responseBot == "2":
        newCustomer()

    else:
        # loops back to the beginning of function if incorrect input
        time.sleep(1)
        print("Sorry, that number is not an option")
        time.sleep(1)
        print("Let's try that again")
        time.sleep(2)
        bot()


bot()


# Consider PyQt for GUI, Otherwise Tkinter seems like best choice
