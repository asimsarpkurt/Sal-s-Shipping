# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:34:58 2021
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
Sal’s Shippers has several different options for a customer to ship their package:
Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
@author: Sarp
"""
weight=1.5
#Ground Shipping
if weight<=2:
  cost_ground=weight*1.50+20
elif weight>2 and weight<=6:
  cost_ground=weight*3.00+20
elif weight>6 and weight<=10:
  cost_ground=weight*4.00+20
elif weight>10:
  cost_ground=weight*4.75+20
print('Ground Shipping Cost:',cost_ground)
#Ground Shipping Premium
cost_premium=125
print('Ground Shipping Premium:',cost_premium)
#Drone Shipping
if weight<=2:
  cost_drone=weight*4.50 
elif weight>2 and weight<=6:
  cost_drone=weight*9.00
elif weight>6 and weight<=10:
  cost_drone=weight*12.00
elif weight>10:
    cost_drone=weight*14.25
print('Drone Shipping Cost:',cost_drone)