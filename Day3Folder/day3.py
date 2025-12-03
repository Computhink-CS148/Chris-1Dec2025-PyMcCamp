# Write all your codes for Day 3 here.
# # COMMENT out the previous task before going on to the next task

import random

# print("hello from day3")

# ########################################################################
# # Task 1:
# name = input("What is your name? ")
# title = input("What is your title? ")
# # command = input("What is your command? ")
# # print(title + " " + name + " " + "commands his peasants to " + command + "." )
# ########################################################################
# # # Task 2:
# # name = input("What is your name? ")
# # num_pen = int(input("How many pens would you like to buy? "))
# # print(name + " bought " + str(num_pen) + ' pens')


# # ########################################################################
# #  Task 3:
# num1 = int(input("Give me a number: "))
# num2 = int(input("Give me another number: "))
# print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))

# # num1 = int(input("Give me a number: "))
# # num2 = int(input("Give me another number: "))
# print(str(num1) + " - " + str(num2) + " = " + str(num1-num2))

# # num1 = int(input("Give me a number: "))
# # num2 = int(input("Give me another number: "))
# print(str(num1) + " x " + str(num2) + " = " + str(num1*num2))

# # num1 = int(input("Give me a number: "))
# # num2 = int(input("Give me another number: "))
# print(str(num1) + " / " + str(num2) + " = " + str(num1/num2))

# # ########################################################################
# # Task 4:
# print("Each apple is $1")
# num = input("How many apples would you like to buy?")
# print("The cost is $" + str(num) + ".")

########################################################################
# Task 5:
# num_1 = int(input("Give me a number: "))
# num_2 = int(input("Give me another number: "))
# if num_1 > num_2:
#     print("The first number is greater than the second number.")
# elif num_1 < num_2:
#     print("The first number is less than the second number.")
# else:
#     print("Both numbers are the same.")

########################################################################
# Task 6:
# a = 3
# password = "12t727347863243yo5y372447437713"
# for count in range (100):
#     guess = input("What is the password? ")
#     if password == guess:
#             print("Access granted")
#     else:
#         print("Access denied")
#         a = a-1
#         if a == 0:
#             print("System has been locked out.")
            


########################################################################
# Task 7:

# for count in range (10):
#     random_number = random.randint(1,10000)
#     print(random_number)


#######qqqqqqqqqqqqqqqqqqqqq#################################################################
# Task 8:
def question():
    random_number1 = random.randint(1,50)
    random_number2 = random.randint(1,50)
    ans = int(input("What is " + str(random_number1) + " + " + str(random_number2) + "? "))
    if ans == random_number1 + random_number2:
        print("You are correct!")








    else:
        print("You are wrong!")
for count in range(20):
    question()

########################################################################
# Additional exercises: