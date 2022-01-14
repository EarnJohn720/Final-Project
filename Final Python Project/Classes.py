class Character:
    def __init__(self, name, address, phoneNum):
        self.__name = name
        self.__age = address
        self.__race = phoneNum


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

