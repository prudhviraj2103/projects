print("=-_-"*10)

customerNames = ['mouse','keyboard','cpu','ups']
customerPins = ['1024','2048','3434','1234']
customerBalances = [10000,20000,30000,40000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 2
i = 0


#this below use to repeat the statement contineously
while True:
    #os system
    print("<.>"*15)
    print("-_-_-_-WELECOME TO SWISS BANK-_-_-_-")
    print("<.>"*15)
    print("1. open a new account <<----")
    print('2. withdraw money <<----')
    print("3. deposit money <<----")
    print("4. check customers & Balance <<----")
    print("5. Exit/Quit  <<----")
    print("*"*20)
    choiceNumber = input("select your option from above menu: ")
    if choiceNumber == "1":
        print('option 1 is selected by you')
        NOC = eval(input('number of custmers'))
        i = i + NOC
        
        if i>5:
            print("/n")
            print('customer registration reached maximum')
            i = i-NOC
        else:
            while counter_1 <= i:
                name = input("enter your full name :")
                customerNames.append(name)
                pin = str(input('enter your pin:'))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input('enter a valid amount for create your account:'))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])    
                print("pin=", end=" ")
                print(customerPins[counter_2])
                print("balance=", end=" ")
                print(customerBalances[counter_2])
                print("-/Rs")
                counter_1 = counter_1+1
                counter_2 = counter_2+1
                print("\nyour name is added")
                print("your pin is created")
                print("your balance is added")
                print("---your new account created----")
                print("\n")
                print("your name is available in customer list")
                print(customerNames)
                print("\n")
                print("please rember your pin and username")
                print(".........................................")
        mainmenu = input("please enter any key to go back to mainmenu")
    elif choiceNumber == "2":
        j = 0
        print("option 2 is selected by you")
        while j < 1:
            k = -1
            name = input("please enter your name : ")
            pin = input("please enter your pin: ")
            while k < len(customerNames) - 1:
                k = k+1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j+1
                        print("your current balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("input your withdraw amount:"))
                        if withdrawal > balance:
                            deposition = eval(input("please deposit higher value balance above mentioned"))
                            balance = balance + deposition
                            print("your current balance:", end=" ")
                            print(customerBalances[k], end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----withdraw successful----")
                            customerBalances[k] = balance
                            print("your new balance:",balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----withdraw successful----")
                            customerBalances[k] = balance
                            print("your new balance:",balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("your name or pin or incorrect")
                break
        mainmenu = input("please enter any key to go back to mainmenu")
    elif choiceNumber == "3":
        print("option 3 is selected by you")
        n = 0 
        while n < 1:
            k = -1
            name = input("please enter username")
            pin = input("please enter your pin")
            while k < len(customerNames) -1:
                k = k+1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n+1
                        print("your current balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        deposition = eval(input("please deposit higher value balance above mentioned"))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("deposition successful")
                        print("youe new balance:", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("your name and pin does not match")
                break            
        mainmenu = input("please enter any key to go back to mainmenu")
    elif choiceNumber == "4":
        print("option 4 is selected by you")
        k = 0
        print("customet name and balance list ; ")
        print("\n")
        while k <= len(customerNames[k]):
            print("->.customet =,", customerNames[k])
            print("->.balance =", customerBalances[k], end=" ")
            print("-/Rs")          
            print("\n")
            k = k+1
        mainmenu = input("please enter any key to go back to mainmenu")
    elif choiceNumber == "5":
        print("option 5 is selected by you")
        print("thank you for using our bank")
        print("\n")
        print("come again")
        print("bye bye")
        break
    else:
        print("invaild option")
        print("please try again")
        mainmenu = input("please enter any key to go back to mainmenu")
