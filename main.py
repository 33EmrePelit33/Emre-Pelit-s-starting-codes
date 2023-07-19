# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:27:08 2023

@author: emrep
"""
from temp import Customer,CarRent,BicycleRent
bike=BicycleRent(20)
car=CarRent(10)
customer=Customer()

main_menu=True

while True:
    if main_menu:
        print("""
        *****Vehicle Rental Shop*****
        A.Bike Menu
        B.Car Menu
        Q.Exit
        """)
    main_menu=False
    choice=input("Enter your choice")
    if choice=="A" or choice=="a":
        print("""
              ***Bike Menu***
              1.Display available bikes
              2.Request a bike for hourly basis $25
              3.Request a bike for daily basis $480 
              4.Return a bicycle
              5.Back to main menu
              6.Exit""")
        selection=input("What would you like to do?")
        try:
            selection=int(selection)
        except ValueError:
            print("Selection should be 1 to 6 number.")
            continue
        if selection==1:
            bike.display_stock(bike.stock)
            choice="A"
        if selection==2:
            customer.rentalTime_b = bike.RentHourly(customer.RequestVehicle("bikes",bike.stock))
            customer.rentalBasis_b = 1
            main_menu=True
        if selection==3:
            customer.rentalTime_b = bike.RentDaily(customer.RequestVehicle("bikes",bike.stock))
            customer.rentalBasis_b = 2
            main_menu=True
        if selection==4:
            customer.bill = bike.ReturnVehicle(customer.ReturnVehicle("bikes"),"bikes")
            customer.rentalTime_b, customer.rentalBasis_b, customer.bikes = 0,0,0
            main_menu=True
        if selection==5:
            main_menu=True
        if selection==6:
            break
        else:
            "It isn't a proper selection. Try again later."
    
    if choice=="B" or choice=="b":
        print("""
              ***Car Menu***
              1.Display available cars
              2.Request a car for hourly basis $25 or €20 or £15
              3.Request a car for daily basis $480 or €384 or £288
              4.Return a car
              5.Back to main menu
              6.Exit""")
        selection=input("What would you like to do?")
        try:
            selection=int(selection)
        except ValueError:
            print("Selection should be 1 to 6 number.")
            continue
        if selection==1:
            car.display_stock(car.stock)
            choice="B"
        if selection==2:
            customer.rentalTime_c = car.RentHourly(customer.RequestVehicle("cars",car.stock))
            customer.rentalBasis_c = 1
            choice="B"
        if selection==3:
            customer.rentalTime_c = car.RentDaily(customer.RequestVehicle("cars",car.stock))
            customer.rentalBasis_c = 2
            choice="B"
        if selection==4:
            customer.bill = car.ReturnVehicle(customer.ReturnVehicle("cars"),"cars")
            customer.rentalTime_c,customer.rentalBasis_c,customer.cars = 0,0,0
            main_menu=True
        if selection==5:
            main_menu=True
        if selection==6:
            break
        else:
            "It isn't a proper selection. Try again later."
    if choice=="Q" or choice=="q":
        print("You haven't choosen a proper choice. Try again later.")
        break
    else:
        "Your shopping is stopped by our Vehicle Rental Shop."
        continue
    print("-----------------")