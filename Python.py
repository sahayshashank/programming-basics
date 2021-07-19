"""
Created on Mon Jul 19 16:39:57 2021

@author: sahayshashank

Desc : Basic syntax in python from literally the most basic things
"""
from studentClass import Student

#variables
number = 11
string = "well strings"

#Lists = arrays
list1 = ["apples","oranges"]
list2 = list("apples")              #['a','p','p','l','e','s']
list1.append(7)
list1.extend([9, 11, 13])           #for multiple items
print(list1[1:4:2])                 #slicing
list3 = list1                       #same list due to = (list3 is like a pointer to list1)
list4 = list1.copy()                #to create a clone of list1
del list2[3]                        #deleting
list1.pop(3)                        #index can be specified or not
list2.sort()
list1.reverse()
print(list2.count("a"))
pow2 = [2 ** x for x in range(10)]

#Tuples - immutable lists
coords = (4,5)
##You can have a list of tuples

#Functions
def myFunc(param1):
    print(param1)
myFunc("wassa")

#Dictionaries - key,value pairs of data
dict1={
       'key1':"value1",
       'key2':2,
       '3':3
       }                            #I know this is weird
print(dict1["key2"]) 
print(dict1.get("key2")) 

#loops
for i in range(5):
    print(i)
for letter in list2:
    print(letter)
    
#Objects
stu1 = Student("Phil","AI",1789263)