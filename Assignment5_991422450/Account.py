'''Defines a bank account its associated attributes and operation.
Fanxing Wang, Jan 5 2018'''
class Account(object):
    """The class defines a bank account,this account class has attribures: account holder's name, account number, annual interest rate, account initial balance
monthly deposited and withdrawal value. This account class can check user's input information and calculate the predicated monthly balance for the next 12 months
taking in consideration the monthly deposits and withdrawals as well as the interest."""
    def __init__(self):
        self.__name=input("Please enter the name of the account holder: ")
        self.__accountNumber=int(input("Please enter the account number;(100-1000): "))
        self.__interestRate=float(input("Please enter the annual interest rate percetange(>0): "))
        self.__initialBalance=float(input("Please enter the initial balance(>=0): "))
        self.__deposit=input("Please enter the monthly deposit(>100): ")
        self.__withdrawal=input("Please enter the monthly withdrawal(<"+self.__deposit+"): ")
        self.__deposit=float(self.__deposit)
        self.__withdrawal=float(self.__withdrawal)
    def checkAccountNumber(self):
        """Assume this bank only allow the account number from 100 to 1000"""
        while self.__accountNumber<100 or self.__accountNumber>1000:
            self.__accountNumber=int(input("Please enter the valid account number（100-1000）:"))

    def checkInterestRate(self):
        """the annual interest rate should greater than 0"""
        while self.__interestRate<=0:
            self.__interestRate=float(input("Please enter the valid annual interest rate percentage(should greater than 0)"))

    def checkInitialBalance(self):
        """Assume the initial balance of users must greater than or equal to 0"""
        while self.__initialBalance<0:
            self.__initialBalance=float(input("please enter the valid initial balance(the initial balance must greater than or equal to 0)"))

    def checkMonthlyDeposit(self):
        """Assume the deposited value need greater than 100"""
        while self.__deposit<=100:
            self.__deposit=float(input("Please enter the valid monthly deposit(the monthly deposit need greater than 100)"))

    def checkMonthlyWithdrawal(self):
        """Assume the monthly withdrawal should less than monthly deposit"""
        while self.__withdrawal>=self.__deposit:
            self.__withdrawal=float(input("Please enter the valid monthly withdrawal(the monthly withdrawal should less than monthly deposit)"))

    def calculate(self):
        """calculate the predicated monthly balance for the next 12 months taking in consideration the monthly deposits and withdrawals as well as the interest"""
        self.__balance=self.__initialBalance+self.__deposit-self.__withdrawal
        self.sumofBalance=0
        for i in range(1,13):
            print("Month ",i,":",sep="")
            print("          Balance:",self.__balance)
            self.sumofBalance=self.sumofBalance+self.__balance
            self.interest=self.sumofBalance*self.__interestRate*0.01/12
            print("         Interest:",self.interest,sep="")
            if i==12:
                break
            self.__balance=self.__balance+self.__deposit-self.__withdrawal
        print("End of Year Balance:",self.__balance+self.interest)
            
            


    def displayStatement(self):
        """Display the calculate information"""
        print("--------------------Programming Principles Bank Statement--------------------")
        print("Account Number:",self.__accountNumber,sep="")
        print("User Name:",self.__name,sep="")
        self.calculate()