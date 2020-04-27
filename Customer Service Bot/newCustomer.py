#Path for new customers

def newCustomer():
    print("Not an issue! From here we can either sign you up for a new account, you can schedule a home visit, or we can connect you directly with a live representative! Do you want to \n[1] Create a new account \n[2] Schedule a home visit \n[3] Get connected to a live representative")
    responseNew = input("Enter the number corresponding to your choice")
    if responseNew == "1":
        newAccount()
    elif responseNew == "2":
        scheduleVisit()
    elif responseNew == "3":
        liveRep()
    else:
        time.sleep(1)
        print("Sorry, that number is not an option")
        time.sleep(1)
        print("Let's try that again in:")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        newCustomer()

def newAccount():
    print("Awesome, I'm glad to see you're climbing aboard our ship, you won't be dissapointed!")
    #Prompt Login Window

def scheduleVisit():
    print("")
