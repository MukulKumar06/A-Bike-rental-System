# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:21:09 2022

@author: Lenovo
"""

class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total bike",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter The postive value or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total Price",q*500)
            print("Total Bike",self.stock)
            

while True:
    obj=bikeShop(100)
    uc=int(input('''
1 Display stocks
2 Rent a Bike
3 Exit
                 '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Qty:---"))
        obj.rentForBike(n)
    else:
        break
        