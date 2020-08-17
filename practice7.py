"""
Project:Use of all the functions learned(if,for,while,zip,enumerate,import,range,
comprehension,lambda.)
Author:Devam A

Discreption:
    *How does import function works for programs in different folders

"""
user_input = input("PLEASE ENTER YOUR NAME:")
print(f"Hello, {user_input.title()}")
if user_input == "devam":
    num1 = int(input("ENTER ANY NUMBER:"))
    num2 = int(input("ENTER ANY NUMBER:"))
    from converter\set_to_list import set_generator
    addition = print(lambda num1,num2:num1 + num2)
    subtration = print(lambda num1,num2:num1 - num2)
    division = print(lambda num1,num2:num1/num2)
else:
    print("SORRY YOU ARE NOT AUTHORISED")
input("THANK YOU PROGRAM COMPLETED!!")
