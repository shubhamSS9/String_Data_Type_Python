# print("Hello World") #"Hello World is a string"
# from numpy.lib.function_base import append

# a = "shubham shinde"   #Assigning string to a variable
# print(a)

# # multiline string

# b = """Thank you for giving this apportunity to introduce myself,
# Hello maam my name is shubham krishna shinde.I honed the skills like 
# Python, django,javascript and python libraries like NumPy, Pandas and sciPy etc., I hold a bachlors degree 
# from Pune university in Bachlors of Engineering in mechanical department"""
# print(b)

# String are arrays

# a = ("shubham")
# print(a[0:7])

# Looping through string

# a = "shubham"
# for i in a:
#     print(i, end=" ")

# String Length

# a = "shubham "
# print(len(a))

# check string

# a = "My name is shubham krishna shinde"
# if ("suraj" or "shubham") in a:
#     print("shubham is present in the string")
# else:
# #     print("Not present in the string")

# a = "shubham is my real name"
# # if "my" not in a:
# #     print("Yes")
# # else:
# #     print("No")

# print("shubham" not in a)



# a="Hello World"
# print(a[2:7])
# print(len(a))
# print(a[0:11])
# print(a[0:11:2])
# print(a[0:])
# print(a[:-1])




# Modify string

# a = "shubham shinde"
# print(a.upper())
# print(a.lower())
# print(a.isupper())
# print(a.islower())
# print(a.strip())

# print(a.replace("a", "R"))

# print(a.split(" "))




# String concatination

# a = "shubham"
# b = "shinde"
# c = a +" "+ b
# print(c.upper())

# string formating

# age = 26
# b="shubham"
# a = "My name is {} and I'm {}"
# print(a.format(b, age))

# b = "I'm {} years old"
# print(b.format(age))

# age = 26
# name = "shubham"
# gender = "male"

# a= "I'm a male, My name is shubham and I'm 26"

# print("I'm a {}, My name is {} and I'm {}.".format(gender, name, age))
# print("Gender: {}\nname: {}\nage: {}".format("male", "shubham", 26))

# Escape character
 
# a = "We are the so-called\f'Vikings' from the north." 
# print(a)

# String Methods

# a = "Intro: my nAme is shubham shinde"
# print(a.casefold())
# print(a.capitalize())
# print(a.center(50))



# Write a Python program to calculate the length of a string.

# a = "I'm from Pune City!"
# print(len(a))


# def str_len(sent):
#     count = 0
#     for i in sent:
#         count = count + 1
#     return count
        
# print(str_len("shubham"))



# def change_char(str1):
#     char = str1[0]
#     str1 = str1.replace(char, "$")
#     str1=char+str1[1:]
#     return str1

# print(change_char("shubhsm"))


# def Swap_str(a, b):
    
#     new_a=b[:2]+a[2:]
#     new_b=a[:2]+b[2:]
#     return new_a+" "+new_b
    
# print(Swap_str('abc','xyz'))


# def change_end(word):
#     length=len(word)
#     if length > 3:
#         if word[-3:] == "ing":
#             word = word + "ly"
#         else:
#             word = word + "ing"
#     else:
#         return "Enter the word which has at least 3 character" 
#     return word   
# input_word = input("Enter the word: ")
# result = change_end(input_word)
# print(result)


# def change_last(a):
#     if a[14:] == "not that poor!":
#         a = a.replace(a[14:], "good !")
#         return a
#     else:
#         return a


# input_sent=input("Enter the sentence: ")
# result=change_last(input_sent)
# print(result)    


# def longest_word(word_1, word_2, word_3):
#     a = len(word_1)
#     b = len(word_2)
#     c = len(word_3)

#     if (a > b):
#         return "Logest word is: ", word_1, " and their length is: ", a
        
#     elif (b > c):
#         return "Logest word is: ", word_2, " and their length is: ", b
#     else:
#         return "Logest word is: ", word_3, " and their length is: ", c
        
# print(longest_word("shubham ","krishna","shinde"))

# a = "Python"
# print(a[:5]+ a[6:])



# x=str(20)
# y=int("1")
# z=float("20")
# print(x)

# String

# msg = "Hello"
# a = msg[0]
# print(a)
# print(msg[2])
# print(msg[-4])

# msg = "rafting"
# print(msg[1])

# string properties

# s = "Hello"
# # s[0] = "M"
# s = "Bye"
# print(s)

# replicate
# s= "shubham"
# print(50*s)

# print('z' in msg)

# built in function

# a = "shubhz"
# print(len(a))
# print(max(a))
# print(min(a))

# string method

# a = "shubham"
# b=98
# print(type(a))
# print(id(a))
# print(id(b))

# import random
# num=random.randint(1,25)
# a = "shubham"
# a.upper()
# print(num)

# name = "Shubham krishna shinde"
# print(name.isalpha())
# print(name.isdigit())
# print(name.isalnum())
# print(name.islower())
# print(name.isupper())
# print(name.startswith("S"))
# print(name.endswith("e"))

# name = "shubham"
# print(name.replace("s", "x"))

# name = "shubham"
# print(name[2:4])
# print(name[2:7])
# print(name[0])

# concatination

# name = "shinde"
# name1 = " shubham"

# fullName = name + name1
# print(fullName)

# student1 = "shubham"
# id1 = 58
# div1 = "A"
# age1 = 26

# student2 = "akshay"
# id2 = 67
# div2 = "B"
# age2 = 27

# print(div1)
# print(age2)


# def Student(name, age, rollNum):
#     return name, age, rollNum


# # print(Student("shubham", 26, 58))
# print(Student("Akshay", 27,65))
        
# a = 23
# b = 54
# A=76
# print(a)

# a = b = "shubham"
# print(a,b)

# for i in range(1, 11):
#     print(i)



# a=7
# surface_area=6*(a**2)
# volume=a**3

# print(surface_area, volume)




# Indexing

# name = "shubham"
# # print(name[-2:])
# # print(name.replace("h", "x"))
# # print("_".join(name))
# print(name.upper())
# print(name.lower())
# print(name.islower())
# print(name.isupper())

# s1 = "shubham"
# s2 = "shinde"
# s3="shubham"

# print(s1 == s2)
# print(s1 == s3)
# print(s1 != s3)
# print(s1 > s2)
# print(s3 > s2)
# print(s2 > s3)

# name = "shubham"
# print(name)

# str1 = "I'm currently learling \'PYTHON\'."
# str2 = r"I'm currently learling 'PYTHON'."

# print(str1)
# print(str2)

# # MultilineLine String

# str3 = "Hello My name is shubham shinde,...I'm currently working in WEB HUB TECHNOLOGY...\
# as a PYTHON DEVELOPER"
# print(str3)

# str4 = """I gained deep knowlegde in Python libraries...
# like pyndas, numpy etc"""
# print(str4)

# str5 = ("I completed my bachlor's degree"
# " from pune university")
# print(str5)

# print(name * 5)

# str6 = "Hello"
# print(str6 + str1)

# print(len(str4))
# print(min(name))
# print(max(name))

# given = "Bamboozled"

# print(given[0:2])
# print(given[8:])
# print(given[-2:])
# print(given[2:])
# print(given[:6])
# print(given[::-1])
# print(given[::])
# print(given[::2])
# print(given[::3])
# print(given[::4])
# print(given + "Hype!")
# print(given[:6] + "Monger!")
# print(given[-0])

# s1 = "NitiAayog"
# s2 = "And Quiet Flows The Don"
# s3 = "1234567890"
# s4 = "Make $1000 a day"

# print(s1)
# print(s2)
# print(s3)
# print(s4)

# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())
# print(s4.isalpha())
# print("......."
# "......")
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s4.isalnum())


# print("_______________")
# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())
# print(s4.isdigit())

# print("_______________")

# print(s1.isupper())
# print(s2.isupper())
# print(s3.isupper())
# print(s4.isupper())

# print("**************")
# print(s1.islower())
# print(s2.islower())
# print(s3.islower())
# print(s4.islower())

# print("_*_*_*_*_*_*_*__*_*_*_*__*_*_*_*_*")

# print(s2.startswith("and"))
# print(s2.endswith("Don"))

# s1 = "Bring It On"
# s2 = " Flanked by spaces on either side "
# s3 = "C:\\Users\\Kanetkar\\Documents"

# print(s1.upper())
# print(s1.lower())
# print(s1.capitalize())
# print(s1.title())
# print(s1.swapcase())
# print(s1.find("I"))
# print(s1.find("On"))
# print(s1.replace("It", "Him"))


# print("________________")
# print(s2.lstrip())
# print(s2.rstrip())

# print("_________________")
# print(s3.split("\\"))
# print(s3.partition("\\"))



# s = "The Terrible Tiger Tore The Towel
# count = 0
# for i in s:
#    if i == "T":
#     count = count + 1
    
# print(count)

# s = "The Terrible Tiger Tore The Towel
# print(s.count("T"))
# print(s.replace("T", "t"))
# print(len(s))







# s = "The Terrible Tiger Tore The Towel"


# pos = s.find("T", 0)
# print(pos, s[pos])

# pos = s.find("T", pos + 1)
# print(pos)


# pos = s.find("T", pos + 1)
# print(pos)

# pos = s.find("T", pos + 1)
# print(pos)

# pos = s.find("T", pos + 1)
# print(pos)

# pos = s.find("T", pos + 1)
# print(pos)

# pos = s.find("T", pos + 1)
# print(pos)

# str1 = "Light travels faster than sound. This is why some people appear bright until you hear them speack"
# print(len(str1))
# print(str1.replace("Light", "LIGHT").replace( "sound", "SOUND"))

# str1 = "Visit ykanetkar.com for online courses in programming"
# # str2 = str1.title()
# # str3 = str2.split(" ")
# # str4 = str3[1].capitalize()
# # str5 = str1[0:5]
# # str6=" "
# # str7 = str1[7:19].capitalize
# # str8=" "
# # str9 = str1[20:]

# # newstr=str5+str6+str7+str8+str9
# # print(newstr)

# # str = str1.index("y", "m")
# # print(str)

# print(str1.title())

# x = 8
# y = 8.0

# print(x is y)

# x = 0
# while x < 20:
#     x = x + 3
#     print(x)
# print(x)


# atm=["cash_widraw","balance_check","pin_change"]
# for i in atm:
#     if i=="cash_widraw":
#         print("Enter The Amount")
#     elif i=="balance_check":
#         print("Enter The Pin")
#     elif i=="pin_change":
#         print("Enter OTP")   
#     else:
#         print("*****INVALID PIN*****")


# m="Keep yourself warm"
# print(m[-1:3])

# name = "shubham"
# print(name[3])
# print(name[3:])
# print(name[::-1])
# print(name[::2])

# name1 = "shubham"
# name2 = "shinde"
# fullname=name1+name2
# print(fullname)

# print(type(name1))
# print(name1.upper())
# print(name1.isupper())
# print(name1.islower())

# per = int(input("Enter percentage: "))

# if per >= 60:
#     print("First Division")
# elif per >= 50:
#     print("Second division")
# elif per >= 40:
#     print("Third Division")
# else:
#     print("Fail")

# age = int(input("Enter your age: "))
# # age=6
# if age >= 18:
#     print("Eligible for voting")
# else:
#     print("Not Eligible")

# num = int(input("enter the number: "))

# if num % 2 == 0:
#     print("EVEN")
    
# else:
#     print("ODD")

# if num % 2 != 0:
#     print("ODD")
    
# else:
#     print("Even")


# year=int(input("Enter year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year")
    
# else:
#     print("Not Leap year")

# n = 1
# while n <= 10:
#     print(n)
#     n=n+1

# n = 1
# sum=0
# while n < 10+1:
#     sum=2*n
#     print(sum)
#     n = n + 1

# sum=0
# for i in range(1, 10+1):
#     sum = 2 * i
#     print(sum)

# name = {"shubham", "shinde"}
# name[0] = "k"
# print(name)
