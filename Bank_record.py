import random

class Database:
    def __init__(self,ac,phone_no,name,dob):
        self.phone_no=phone_no
        self.name=name
        self.dob=dob
        self.account_no=ac
        self.account_balance=0
        self.next=None
class BankNetwork:
    #Header files
    def __init__(self):
        self.head=None
        self.account=[]
    # Create account
    def create(self,ac,phone_no,name,dob):
        if self.head is None:
            data=Database(ac,phone_no,name,dob)
            self.head=data
            self.account.append(ac)
        else:
            new_account=Database(ac,phone_no,name,dob)
            data=self.head
            while data.next is not None:
                data=data.next
            data.next=new_account
            self.account.append(ac)
    #Display accounts
    def account_counts(self):
        data=self.head
        count=1
        if data.head is None:
            return 0
        else:
            while data.next is not None:
                count+=1
                data=data.next
        return count
    #show customer list
    def show_customers(self):
        data=self.head
        if self.head is not None:
            i=0
            for i in range(self.account_counts()):
                print(f"{i+1}\t{data.name}\t{data.account_no}\t{data.account_balance}\t{data.phone_no}")
                data=data.next
            return True
        else:
            return False
    def customer_info(self,ac=None,phone_no=None):
        print(self.account_counts())
        if ac is not None:
            data = self.head
            if ac in self.account:
                for i in range(self.account_counts()):
                    if data.account_no==ac:
                        return data
                    data=data.next
                else:
                    return False
            else:
                return False
        elif phone_no is not None:
            data = self.head
            for i in range(self.account_counts()):
                if data.phone_no==phone_no:
                    return [data.name,data.account_no]
                data=data.next
            else:
                return False
        else:
            return False
    #Transfer amount
    def transfer(self,amount,c_ac,r_ac):
        c_data = self.customer_info(c_ac)
        r_data = self.customer_info(r_ac)
        if c_ac in self.account and r_ac in self.account and c_data.account_balance>amount:
            print(f"Sender : {c_data.name} \t Receiver : {r_data.name}")
            input("press any key to continue ... ")
            c_data.account_balance-=amount
            r_data.account_balance+=amount
            print("Transfer Completed")
    #Deposit amount
    def deposit(self,ac,amount):
        if ac in self.account:
            data=self.customer_info(ac)
            input(f"\n{data.name} confirm the Transaction\nclick a key to confirm ...")

            data.account_balance=data.account_balance+amount
            return True
        else:
            return "-ac"
    #withdraw amount from linkage
    def withdraw(self,ac,amount):
        if ac in self.account:
            data=self.customer_info(ac)
            input(f"\n{data.name} confirm the Transaction\nclick a key to confirm ...")
            if data.account_balance>amount:
                data.account_balance=data.account_balance-amount
                return True
            else:
                return "-l"
        else:
            return "-ac"
    def check_balance(self,ac):
        bal=self.customer_info(ac)
        if bal:
            return bal.account_balance
        else:
            return False
    #Remove account from linkage
    def remove_account(self,ac):
        data=self.head
        if ac in self.account and self.head is not None:
            if data.account_no==ac:
                self.head=data.next
            else:
                while data.next.account_no!=ac:
                    data=data.next
                a_ac=data.next.next
                data.next=a_ac
            return True
        else:
            return "-ac"
    def input_(self,ac=False):
        if ac:
            ac=input("Enter account_no : ")
            return ac
        else:
            name = input("Enter your name : ")
            dob = input("Enter date of birth(YYYY-MM-DD) : ")
            phone_no = ("+91 " + input("Enter Your phone No : ")).rstrip()
            return name,dob,phone_no




if __name__=="__main__":
    bank=BankNetwork()
    while True:
        print("\nBank Operation :\n\n1- Create Account\n2- Account Balance\n3- Withdraw\n4- Deposit\n5- Remove Account\n6- Info \n7- Quit")
        ch=input("Enter the choice : ")
        choice=["1","2","3","4","5","6","7"]
        if ch in choice:
            if ch ==choice[0]:
                name,dob,phone_no=bank.input_()

                if name and dob and len(phone_no)==14:
                    while True:
                        account_no="920425"+str(random.randint(100000,9999999))
                        if account_no not in bank.account:
                            bank.create(ac=account_no,phone_no=phone_no,name=name,dob=dob)
                            break
                        continue
                print("Account Created Successfully !!",name,f"\nAccount no : {account_no}")
                input()
            elif ch==choice[1]:
                ac=bank.input_(True)
                bal=bank.check_balance(ac)
                if bal:
                    print("Your Balance : ",bal)
                    input()
                else:
                    print("Something wrong with a Input\n Try again\n")
                input()
            elif ch == choice[2]:
                ac=bank.input_(True)
                amount=input("Enter the amount : ")
                m=bank.withdraw(ac,int(amount))
                if m=="-l":
                    print("Not Sufficient Amount")
                elif m=="-ac":
                    print("Account Not Found")
                else:
                    print(f"Account : {ac}\namount : {amount}\nAmount Transfer Completed")
                input()
            elif ch == choice[3]:
                ac = bank.input_(True)
                amount = input("Enter the amount : ")
                m = bank.deposit(ac,int(amount))
                if m == "-ac":
                    print("Account Not Found")
                else:
                    print(f"Account : {ac}\nAmount : {amount}\nAmount Transfer Completed")
                input()
            elif ch == choice[4]:
                ac=bank.input_(True)
                ban=bank.remove_account(ac)
                if ban=="-ac":
                    print("Account Not Found")
                elif ban:
                    print("The Account Removed")
                input()
            elif ch==choice[5]:
                m=bank.show_customers()
                if m:
                    pass
                else:
                    print("No Record Found")
                input()
            else:
                print("Existing ...")
                input()
                break







