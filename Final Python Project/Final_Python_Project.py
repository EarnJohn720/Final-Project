import os, datetime
print(os.environ['USERPROFILE'])
user = (os.getenv('username'))
current_time = datetime.datetime.now()
format_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
print(format_time)

class Person:

    def __init__(self, name, address, phoneNum):
        self.__name = name
        self.__address = address
        self.__phoneNum = phoneNum
    
    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
       self.__address = address

    def setTelephone(self, phoneNum):
       self.__phoneNum = phoneNum

    def getName(self):
       return self.__name

    def getAddress(self):
       return self.__address

    def getTelephone(self):
       return self.__phoneNum


class Customer(Person):
    def __init__(self, name, address, phoneNum, custNum, MailList):
        super().__init__(name, address, phoneNum)
        self.__custNum = custNum
        self.__mailing = MailList

    def setCustomerNum(self, salary):
        self.__custNum = salary

    def setMailing(self, production):
       self.__mailing = production

    def getCustomerNum(self):
       return self.__custNum

    def getMailing(self):
       if self.__mailing == "Yes":
           return True
       if self.__mailing == "No":
           return False

def main():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phoneNum = input("Enter the phone number: ")
    custNum = input("Enter the customer number: ")
    mail = input("Does the customer wish to be on the mailing list?(Yes/No) ")
    people = Customer(name, address, phoneNum, custNum, mail)
    print("Customer information:")
    print("Name: ", people.getName())
    print("Address: ", people.getAddress())
    print("Phone Number: ", people.getTelephone())
    print("Customer Number: ", people.getCustomerNum())
    print("On Mailing List: ", people.getMailing())

    
main()
