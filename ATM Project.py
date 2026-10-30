balance=10000
print('1.check balance')
print('2.deposit')
print('3.withdraw')
print('4.exit')
def check_balance():
    print('available balance is ',balance)

def deposit():
    global balance
    amount=int(input('enter your deposit money:'))
    if amount<=0:
        print('invalid')
    else:
        balance+=amount
        print('amount deposited successfully')
        check_balance()

def withdraw():
    global balance
    Amount=int(input("enter your withdraw amount:"))
    if Amount<=0:
        print('invalid amount')
    elif Amount>balance:
        print('insufficient amount in your account') 
    else:
        balance-=Amount
        print('amount withdrawn successfully')
        check_balance()

def show_menu():
    print('1.check balance')
    print('2.deposit')
    print('3.withdraw')
    print('4.exit')

while True:
    show_menu()
    option=int(input('select one option from 1 to 4:'))
    if option==1:
        check_balance()
    elif option==2:
        deposit()
    elif option==3:
        withdraw()
    elif option==4:
        print('exit')
        break 
    else:
        print('ivalid choice')              