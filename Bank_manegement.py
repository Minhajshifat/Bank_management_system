class Bank:
    accounts = []
    total_balance = 0
    total_loan = 0
    loan_status = True
    adminid = "admin"
    adminpass = "admin"

    def create_account(self, User):
        Bank.accounts.append(User)
        print("You have sucessfully created a account! ")
        print("Holder's account id is ", user.id)

    def delete_user(self, userid):
        for acount in Bank.accounts:
            if acount.id == userid:
                Bank.accounts.remove(acount)
                print("successfully deleted!")
                return
        print("user not found!")

    def available_balance(self):
        print("Your Bank Balance is : ", Bank.total_balance)
        return Bank.total_balance

    def change_loan_status(self, cng):
        if cng == "o" or cng == "O":
            Bank.loan_status = True
            print(" Loan system is On")
        elif cng == "f" or cng == "F":
            Bank.loan_status = False
            print(" loan system is  OFF")
        else:
            print("Wrong instruction!!!")

    def t_loan(self):
        print(Bank.total_loan)
        return Bank.total_loan

    def show_all_account(self):
        for acount in Bank.accounts:
            print()
            print("Account Holder's Name: ", acount.name, "\nHolder's id: ", acount.id)
            print(
                "Holder email: ", acount.email, " \nHolder's Address : ", acount.address
            )
            print(
                "Account'type:",
                acount.type,
                "\nAccount Id: ",
                acount.id,
                "\nUser balance is :",
                acount.balance,
            )
            print()


class User:
    users = 0

    def __init__(self, name, email, address, type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        if self.type == "s" or self.type == "S":
            self.type = "saving"

        elif self.type == "c" or self.type == "C":
            self.type == "cuurent"
        self.balance = 0
        self.loan = 0
        self.loanc = 0
        self.history = []
        User.users += 1
        self.id = User.users + 120

    def user_balance(self):
        print("your balance is :", self.balance)

    def create_account(self):
        Bank.accounts.append(self)
        print()
        print("You have sucessfully created a account!")
        print("Your account id is : ", self.id)
        print("Don't share this id with anyone\nplease remember this account id")
        print()

    def disposit(self, amount):
        if amount > 0:
            self.balance += amount
            Bank.total_balance += amount
            print("you sucessfully diposit ", amount)
            h1 = ("diposit", amount)
            self.history.append(h1)

    def withdraw(self, amount):
        if amount > 0:
            if amount < Bank.total_balance:
                if amount <= self.balance:
                    self.balance -= amount
                    Bank.total_balance -= amount
                    print("you successfully withdrawed", amount)
                    h2 = ("withdraw", amount)
                    self.history.append(h2)
                else:
                    print("Withdrawal amount exceeded!!!")
            else:
                print("The bank is bankrupt")
        else:
            print("Please enter valid amount")

    def take_loan(self, amount):
        if amount > 0:
            if self.loanc < 2:
                if amount < Bank.total_balance and Bank.loan_status == True:
                    Bank.total_balance -= amount
                    self.loan += amount
                    Bank.total_loan += amount
                    self.loanc += 1
                    print()
                    print("you successfully take loan ", amount)
                    h3 = ("take loan", amount)
                    self.history.append(h3)
                else:
                    print("You cannot  take loan !")
            else:
                print("you already reach your limit you cannot take loan !")
                print()

    def send_money(self, amount, reciverid):
        for account in Bank.accounts:
            if account.id == reciverid:
                if amount > 0 and amount < self.balance:
                    self.balance -= amount
                    account.balance += amount
                    print("you successfully send", amount)
                    h4 = ("send money", amount)
                    self.history.append(h4)
                    break
                else:
                    print("you don't have enough money")
                    break
            else:
                print("Account does not exist!!!")

    def transation_history(self):
        for stroy in self.history:
            print(stroy)


Banglabank = Bank()
currentuser = None
while True:
    if currentuser == None:
        print("   *** Well come ***  ")
        print("press a for admin log in")
        print("press u for user log in")
        print("press r for register account")
        b = input()
        if b == "a":
            id = input("enter admin id : \n")  # admin
            password = input("Enter your password : \n")  # admin
            if id == Bank.adminid and password == Bank.adminpass:
                currentuser = Banglabank
            else:
                print("You entered wrong id or password")
        elif b == "u":
            print("Enter your account Number :")
            a = int(input())
            for account in Bank.accounts:
                if account.id == a:
                    currentuser = account
                    break
        elif b == "r":
            n = input("Enter user name  : ")
            e = input("Enter email : ")
            ad = input("Enter address : ")
            t = input("Enter type of account : ")
            if t == "s" or t == "c":
                user = User(n, e, ad, t)
                user.create_account()
                currentuser = user
            else:
                print("you entered wrong type of account")
                currentuser = None
    elif currentuser == Banglabank:
        print("press 1 create an user account")
        print("press 2 delete any user account")
        print("press 3 see all user accounts list")
        print("press 4 check the total available balance of the bank")
        print("press 5 check the total loan amount")
        print("press 6 on or off the loan feature of the bank")
        print("press 7 for logout")
        p = int(input())
        if p == 1:
            n = input("Enter user name :\n ")
            e = input("Enter email :\n ")
            ad = input("Enter address :\n")
            t = input("Enter type of account :\n")
            if t == "s" or t == "c":
                user = User(n, e, ad, t)
                Banglabank.create_account(user)
            else:
                print("you entered wrong type of account")
                currentuser = Banglabank
        elif p == 2:
            i = int(input("enter user id \n"))
            Banglabank.delete_user(i)
        elif p == 3:
            Banglabank.show_all_account()
        elif p == 4:
            Banglabank.available_balance()
        elif p == 5:
            Banglabank.t_loan()
        elif p == 6:
            ter = input("Enter o for on or f for off :\n")
            Banglabank.change_loan_status(ter)
        else:
            currentuser = None

    else:
        print("press 1 withdraw")
        print("press 2 diposit")
        print("press 3 check avaiable balance")
        print("press 4 check transaction history")
        print("press 5 take loan")
        print("press 6 transefer money")
        print("press 7 for logout")
        ac = int(input())
        if ac == 1:
            amount = int(input("Enter the amount :\n"))
            currentuser.withdraw(amount)
        elif ac == 2:
            amount = int(input("Enter the amount :\n"))
            currentuser.disposit(amount)
        elif ac == 3:
            currentuser.user_balance()
        elif ac == 4:
            currentuser.transation_history()
        elif ac == 5:
            amount = int(input("Enter the amount :\n"))
            currentuser.take_loan(amount)
        elif ac == 6:
            amount = int(input("Enter the amount :\n"))
            id = int(input("Enter the reciver id : \n"))
            currentuser.send_money(amount, id)
        elif ac == 7:
            currentuser = None
