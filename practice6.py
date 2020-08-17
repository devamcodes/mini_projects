name = input("PLEASE ENTER YOUR NAME:")
me = "devam"
if me==name:
    print(f"Hello, {name.title()}")
    print ("YOU CAN RUN THE PROGRAM.")
    user = input("ENTER LOTTERY OR OPERATION:")
    for lottery in user:
        print("TRY YOUR LUCK HERE.")
    
else:
    print("SORRY YOU ARE NOT AUTHORISED.")
    
