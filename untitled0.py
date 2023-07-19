# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 01:17:53 2022

@author: emrep
"""
class Employee(object):
    #init metodu
    def __init__(self,name,surname,rate_of_increase,amount):
        "Ilk değer atama"
        self.Name=name
        self.Surname=surname
        self.Rate_of_Increase=rate_of_increase
        self.Amount=amount
    def increase(self,rate_of_increase,amount):
        self.Rate_of_Increase=self.rate_of_increase
        self.Amount=self.amount*self.rate_of_increase
a2=Employee("Robin","Hood","2","1600")
a3=Employee("Elvis", "Priestley","3","2150")
print("Name2: ",a2.Name)
print("Name3: ",a3.Name)
print("Surname2: ",a2.Surname)
print("Surname3: ",a3.Surname)
print("Rate_of_Increase2= ",a2.Rate_of_Increase)
print("Rate_of_Increase3= ",a3.Rate_of_Increase)
print("Last amount2=  ",a2+a2*int(a2.Rate_of_Increase))
print("Last amount3= ",a3+a3*int(a3.Rate_of_Increase))