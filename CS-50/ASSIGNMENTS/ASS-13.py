class Account:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number
    
    def debit(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("You have low balance...")

    def credit(self,amount):
        self.balance=self.balance+amount

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number
######################################################################################
class User:
    def __init__(self,name,address,email,account):
        self.accounts=[account]
        self.name=name
        self.address=address
        self.email=email

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email
    
    def get_accounts(self):
        return self.accounts
    
    def add_account(self,account):
        self.accounts.append(account)
###################################################################################
class Bank:
    def __init__(self,branch_name,branch_code):
        self.branch_name=branch_name
        self.branch_code=branch_code
        self.user=list()

    def get_branch_name(self):
        return self.branch_name

    def get_branch_code(self):
        return self.branch_code

    def get_users(self):
        return self.user

    def add_user(self,user):
        self.user=user
###################################################################################
def main():
    bank1=Bank('Halisahar', 202020)

    n=int(input("How many user you want to enter for your bank..."))
    users=list()

    for i in range(n):
        name=input("Enter the name of the user...")
        address=input("Enter the address of the user...")
        email=input("Enter the email of the user...")
        acc_no=743136+i
        balance=int(input("Enter the total deposit money..."))
        print()
        account=Account(balance,acc_no)
        user_details=User(name,address,email,account)
        users.append(user_details)

    bank1.add_user(users)
    user_list=bank1.get_users()
    
    for i in range(len(user_list)):
        print("User-name:",user_list[i].get_name())
        print("User-address:",user_list[i].get_address())
        print("User-email:",user_list[i].get_email())
        acc=user_list[i].get_accounts()
        for j in range(len(acc)):
            print("User-a/c:",acc[j].get_account_number())
            print("User-balance:",acc[j].get_balance())
        print()


main()