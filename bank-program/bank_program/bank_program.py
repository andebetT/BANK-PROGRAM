
balance=1000
def show_balance():
    print(f"your current balance is ${balance:.2f}")
def deposit():
    global balance
    amount = int(input("please enter your deposit amount"))
    if amount<0:
        return "please inter a valid amount"
    balance+=amount


def withdraw():
    global balance
    value=int(input("please enter your deposit value"))
    if value>balance:
        return f"please inter a number less than {balance}"
    balance=balance-value
is_running=True
while is_running:
    print("well come")
    print("1:show balance")
    print("2:deposit")
    print("3:withdraw")
    print("4:exit")
    choice=input("enter your choice")
    if choice=="1":
        show_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        print(f"your current balance is ${show_balance()}")
        print("thank you for coming")
        is_running=False
    else:
        print("please select a valid choice (1-4):")



