# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 21:01:17 2023
@author: emrep
"""

# Soru: Başlangıçta 1 buğday var ve her geçen gün elimizdeki buğdayın 2 
# katını alırsak y gün sonra kaç buğdayımız olur?
y = int(input("Kaç gün?"))
z = int(input("İlk tohum adedi=?"))
x=3**(y-1)
print("Son durumdaki tohum adedi=",x)