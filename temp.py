# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:30:27 2023

@author: emrep
"""
#Rent a vehicle project
import datetime

# Parent Class
class VehicleRent:
    def __init__(self,stock):
        self.stock=stock
        self.now=0
    def display_stock(self,stock):
        """
        Display stock
        """
        print("{} vehicle(s) available to rent".format(self.stock))
        return self.stock
    def RentHourly(self,n):
        """
        Rent hourly
        """
        if n<=0:
            print("Number should be positive.")
            return None
        elif(0<n<=self.stock):
            self.now=datetime.datetime.now()
            print("Rented {} vehicle(s) as hourly from {}.".format(n,self.now))
            self.stock-=n
            return self.now
        else:
            print("You didn't choose a proper selection,we have {} available vehicle(s) to rent".format(self.stock))
            return None
            
    def RentDaily(self,n):
        """
        Rent daily
        """
        if n<=0:
            print("Number should be positive.")
            return None
        if(0<n<=self.stock):
            self.now=datetime.datetime.now()
            print("Rented {} vehicle(s) as daily from {}.".format(n,self.now))
            self.stock-=n
            return self.now
        else:
            print("You didn't choose a proper selection,we have {} available vehicle(s) to rent".format(self.stock))
            return None
    def ReturnVehicle(self,request,brand):
        """
        Return a bill
        """
        car_h_price=100
        car_d_price=car_h_price*9/10*24
        bicycle_h_price=25
        bicycle_d_price=bicycle_h_price*8/10*24
        rentalTime, rentalBasis, numOfVehicles = request
        bill=0
        
        if brand=="cars":
            if rentalTime and rentalBasis and numOfVehicles:
                self.stock+=numOfVehicles
                now= datetime.datetime.now()
                rentalPeriod= now-rentalTime
                if rentalBasis==1: #hourly
                    bill+=car_h_price*numOfVehicles*rentalPeriod.seconds/3600
                elif rentalBasis==2: #daily
                    bill=car_d_price*numOfVehicles*rentalPeriod.seconds/86400
                    
                if(4<numOfVehicles):
                    print("You have extra %15 discount.")
                    bill*=0.85
                
                print("Thank you for returning the car.")
                print("Your price is $ {}".format(bill))
                return bill
        if brand=="bikes":
            if rentalTime and rentalBasis and numOfVehicles:
                self.stock+=numOfVehicles
                now= datetime.datetime.now()
                rentalPeriod= now-rentalTime
                if rentalBasis==1: #hourly
                    bill+=bicycle_h_price*numOfVehicles*rentalPeriod.seconds/3600
                elif rentalBasis==2: #daily
                    bill+=bicycle_d_price*numOfVehicles*rentalPeriod.seconds/86400
                    
                if(9<numOfVehicles):
                    print("You have extra %15 discount.")
                    bill*=0.85
                
                print("Thank you for returning the bike.")
                print("Your price is $ {}".format(bill))
                return bill
#Child Class 1
class CarRent(VehicleRent):
    global discount_rate
    discount_rate=10
    def __init__(self,stock):
        super().__init__(stock)
    def discount(self,b):
        """
            discount
        """
        bill=b-(b*discount_rate)/100
        return bill
#Child Class 2
class BicycleRent(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)
        
#customer
class Customer(object):
        
    bikes=0
    rentalBasis_b=0
    rentalTime_b=0
            
    cars=0
    rentalBasis_c=0
    rentalTime_c=0
        
    def RequestVehicle(self,brand,stock):
        """
        Take a Request Bike or Car from Customer
        """
        if brand=="bikes":
            bikes=input("How many bikes do you want to rent?\n")
            try:  
                bikes=int(bikes)
            except ValueError:
                print("Number should be number.")
                return -1
            if bikes<1:
                print("Number should be positive.")
                return None
            if 1<=bikes<=BicycleRent(stock).stock:
                self.bikes=bikes
                return self.bikes
            else:
                print("We haven't got bikes as such as your request.")
                return None
        if brand=="cars":
            cars= input("How many cars would you rent?\n")
            try: 
                cars= int(cars)
            except ValueError:
                print("Number should be Number.")
                return -1
            if cars<1:
                print("Number should be positive.")
            elif 1<=cars<=CarRent(stock).stock:
                self.cars=cars
                return self.cars
            else:
                print("We haven't got cars as such as your request.")
                return None
    def ReturnVehicle(self,brand):
        """
            Return Bikes or Cars
        """
        if brand=="bikes":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
        if brand=="cars":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0