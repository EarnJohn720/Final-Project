class Character:
    #Initializer
    def __init__(self, name, age, race, alignment, stats):
        self.__name = name
        self.__age = age
        self.__race = race
        self.__align = alignment
        self.__stats = stats

    def __init__(self, name, age, race, race_des, alignment, stats):
        self.__name = name
        self.__age = age
        self.__race = race
        self.__des = race_des
        self.__align = alignment
        self.__stats = stats
    #Setter
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
       self.__age = age

    def setRace(self, race):
       self.__race = race

    def setAlign(self, alignment):
       self.__align = alignment

    def setStats(self, Stats):
       self.__stats = Stats

    def setDescipt(self, description):
        self.__des = description

    #Getter
    def getName(self):
       return self.__name

    def getAge(self):
       return self.__age

    def getRace(self):
       return self.__race

    def getAlign(self):
       return self.__align

    def getStats(self):
        for x, y in self.__stats.items():
            print(f"{x}: {y}")

    def getDescript(self):
        return self.__des

    def returnStats(self):
        return self.__stats
        #print()
       #return self.__stats

    #def __str__(self):

    #   return 0

#class Person:

#    def __init__(self, name, address, phoneNum):
#        self.__name = name
#        self.__address = address
#        self.__phoneNum = phoneNum
    
#    def setName(self, name):
#        self.__name = name

#    def setAddress(self, address):
#       self.__address = address

#    def setTelephone(self, phoneNum):
#       self.__phoneNum = phoneNum

#    def getName(self):
#       return self.__name

#    def getAddress(self):
#       return self.__address

#    def getTelephone(self):
#       return self.__phoneNum


#class Customer(Person):
#    def __init__(self, name, address, phoneNum, custNum, MailList):
#        super().__init__(name, address, phoneNum)
#        self.__custNum = custNum
#        self.__mailing = MailList

#    def setCustomerNum(self, salary):
#        self.__custNum = salary

#    def setMailing(self, production):
#       self.__mailing = production

#    def getCustomerNum(self):
#       return self.__custNum

#    def getMailing(self):
#       if self.__mailing == "Yes":
#           return True
#       if self.__mailing == "No":
#           return False

