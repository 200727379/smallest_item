#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#Date: 29 April 2021
"""
Write a Python program to get the smallest number from a list
"""

my_list = [100,25,750, 48, 478, 30, 24]

smallest = 9999999

for x in my_list:
    if smallest > x:
        smallest = x
        
print("The smallest number in the list is: ", smallest)