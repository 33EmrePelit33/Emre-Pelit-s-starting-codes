# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:06:32 2022

@author: emrep
"""

from abc import ABC, abstractmethod

class People(ABC):
    def __init__(self,name,age,task,salary):
        self.name=name
        self.age=age
        self.task=task
        self.Salary=salary
    @abstractmethod
    def Mobility(self):
        return 4
    @abstractmethod
    def Voting_right(self):
        return 1        
class Manager(People):
    def __init__(self,name,age,task,salary):
        super().__init__(name,age,task,salary)
    def Mobility(self):
        return 4
    def Voting_right(self):
        return 1
class Lawyer1(People):
    def __init__(self,name,age,task,salary):
        super().__init__(name,age,task,salary)
    def Mobility(self):
        return 4
    def Voting_right(self):
        return 1
class Lawyer2(People):
    def __init__(self,name,age,task,salary):
        super().__init__(name,age,task,salary)
    def Mobility(self):
        return 4
    def Voting_right(self):
        return 1
selection=input("Select one of them 1);2);3)")
manager1=Manager("Jack",43,"signing",4300)
lawyer1=Lawyer1("Adam",35,"cleaner",2000)
lawyer2=Lawyer2("Helen",37,"accounter",3400)
if selection=='1':
    print(manager1.name)
    print(manager1.age)
    print(manager1.task)
    print(manager1.Salary)
    print(manager1.Mobility())
    print(manager1.Voting_right())
elif selection=='2':
    print(lawyer1.name)
    print(lawyer1.age)
    print(lawyer1.task)
    print(lawyer1.Salary)
    print(lawyer1.Mobility())
    print(lawyer1.Voting_right())
elif selection=='3':
    print(lawyer2.name)
    print(lawyer2.age)
    print(lawyer2.task)
    print(lawyer2.Salary)
    print(lawyer2.Mobility())
    print(lawyer2.Voting_right())    
else:
    print("I don't work at this bank.")

            

        