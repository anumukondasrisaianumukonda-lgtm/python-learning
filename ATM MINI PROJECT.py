account_balance = 100000
valid_card = "B"
valid_password = 6688
print("ATM APPLICATION")
card = input("insert the card").strip()
if card!= valid_card:
    print("invalid card")
else:
    print("welcome lakshmi")
    password = int(input("enter the password"))
    if password!= valid_password:
        print("incorrect password")
    else:
        print("options -> 1.balance enquiry")
        print("options -> 2.withdraw")
        option = int(input("choose option(1 or 2"))
        if option == 1:
            print("account balance is ->",account_balance)
        elif option == 2:
            amount = int(input("amount ->"))
            account_balance = account_balance - amount
            print("remaining account balance is ->",account_balance)
        else:
            print("invalid option")
