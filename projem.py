# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:41:32 2023

@author: emrep
"""
#%% Object Orianted Programming
#%%
# class and constructure
class Lawyer: #class
    def __init__(self,name,surname,degree): #constructure
        self.name=name
        self.surname=surname
        self.email=name+surname+"@asd.com"
        self.degree=degree
        self.salary=3000*pow(degree+1,2)
    def giveSalary(self):
        return self.salary
    def giveEmail(self):
        return self.email
l1=Lawyer("Jack","Daniels",0) 
l2=Lawyer("John","Adams",1)
l3=Lawyer("Sandra","McDommy",2)   
print("Salary1=",l1.giveSalary())
print("Email3=",l3.giveEmail())
#%%
# class variable
class Student: 
    oran=0.95 # class variable
    sayaç=0 # sınıf mevcudu
    def __init__(self,name,surname,degree,grade):
        self.grade=grade
        self.name=name
        self.surname=surname
        self.email=name+surname+"@asd.com"
        self.degree=degree
        self.number=degree*100+len(name)*len(surname)
        Student.sayaç+=1
    def dicrease_grade(self):
        self.grade*=self.oran
        print(self.grade)
    def giveNameSurname(self):
        return self.name+"\n"+self.surname
#    def giveEmail(self):
#       return self.email
s1=Student("Emre","Pelit",3,75)
print("s1'in ilk notu=",s1.grade)
print("s1'in son notu=",s1.dicrease_grade())
print("Sınıf mevcudu=",Student.sayaç)
s2=Student("Esra","Esma",4,83)
print("s2'nin ilk notu=",s2.grade)
print("s2'nin son notu=",s2.dicrease_grade())
print("Sınıf mevcudu=",Student.sayaç)
print("s1'in numarası=",s1.number)
print("s2'nin numarası=",s2.number)
print("s1'in emaili:",s1.email)
print("s2'nin emaili:",s2.email)
s3=Student("Elif","Ayşe",3,83)
print("Sınıf mevcudu=",Student.sayaç)
s4=Student("Merve","Özbay",1,87)            
print("Sınıf mevcudu=",Student.sayaç)
s5=Student("Ekin","Uzun",2,78)
print("Sınıf mevcudu=",Student.sayaç)
# class example            
liste=[s1,s2,s3,s4,s5]
print(liste) 
print(liste[0])
print(liste[0].degree)
print(liste[0].grade)
print(liste[1].giveNameSurname())
print(liste[2].grade) 
print(liste[3].dicrease_grade())
print(liste[4].email)
max_grade=liste[0].grade
min_grade=liste[0].grade
for each in liste:
    while each.grade>max_grade:
        max_grade=each.grade
        print("En başarılı öğrenci:",each.giveNameSurname(),"\nOnun numarası=",each.number,"\nOnun emaili:",each.email)
for each in liste:
    while each.grade<min_grade:
        min_grade=each.grade
print("Minimum not=",min_grade,"\nMaximum not=",max_grade)
#%% Programming errors
# syntax error
print(9)
#print 9
int(3.14159+1.789)
#int 3.14159+1.789
i=0
while(i<10):
    print(i)
    i+=1
#%% exceptions
# runtime error
# Python derleyicisi öncelikle syntax hatası arar eğer yoksa diğer hatalara bakar.
a=10
b="23"
c="bugün hava çok güzel."
liste=[1,2,4,7]
print(sum(liste))
#print(a+b)
print(str(a)+b)
print(a+len(b))
print(b+c)
#print(c+liste)
print(c+str(liste))
zero=0
k=15
# if(zero==0):
#     e=0
# else:
#     e=k/zero
try:
    e=k/zero
except ZeroDivisionError:
    e=0
print(e)
# index error
l1=[1,3,5,7,9]
# print(l1[5])
print(l1[4])
# module not found error
#import numpyy
# file not found error
#import pandas as pd
#pd.read_csv("asd")
# type error
#2+"12"
# value error
#int("123sad") 
try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done")
#%%

        





















