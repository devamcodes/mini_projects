name = "Devam"
user_input = input("PLEASE ENTER YOUR NAME:")

if user_input==name:
    print("WELLCOME DEVAM ")
    
    
    lottery = int(input("PLEASE ENTER YOUR LUCKY NUMBER:"))
    number = [3,4,13,23,5,56,66,98,85]
    if lottery in number:
         print("YOU HAVE WON THE LOTTERY!!!")
    else:
         print("BETTER LUCK NEXT TIME!")

else:
    print("YOU ARE UNAUTHORIESED SORRY.")

input("THE PROGRAM COMPLETED!!")

