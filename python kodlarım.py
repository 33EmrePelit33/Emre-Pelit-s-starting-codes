# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:56:59 2022

@author: emrep
"""

#calculator project
class Calc(object):
    "Calculator"
     #init metodu
    def __init__(self,a,b):
        "initialize values"
        #attributes
        self.value1=a
        self.value2=b
    def add(self):
        "addition a+b=result -> return result"
        result=self.a + self.b
        return result
    def cikarma(self):
        "a-b=result -> return result"
        result=self.a - self.b
        return result
    def multiply(self):
        "return a*b"
        return self.a*self.b
    def tamsayi_bolme(self):
        "(int)a // (int)b = result <=> result must be an integer(2 tane bölme işaretinin yan yana gelmesiyle gösterilir."
        return self.a// self.b
    def divide(self):
        result = self.a/self.b
        return result 
print("Choose Add(1), Divide(2), Multiply(3),TamSayi_Bolme(4), Normal_Bolme(5)")
selection = input("Select one of them")

print("Give the first value")
v1=int(input("first value"))
print("Give the second value")
v2=int(input("Second value"))
c1 = Calc(v1,v2)
     
if selection=="1":
    Add_result=c1.Add()
    print("Add = {}". format(Add_result))
elif selection=="2":
    cikarma_result=c1.Divide()
    print("Cikan = {}". format(cikarma_result))
elif selection=="3":
    multiply_result=c1.multiply()
    print("Multiply = {}". format(multiply_result))        
elif selection=="4": 
    tamsayibolme_result=c1.tamsayi_bolme()
    print("Tam Sayi Bolme = {}". format(tamsayibolme_result))
elif selection==5:
    divide_result=c1.Divide()
    print("Divide = {}".format(divide_result))