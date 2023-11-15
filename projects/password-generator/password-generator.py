# Process
# 1. import random module
# 2. import random string
# 3. collect user desired lenght
import random
import string

def pass_generate():
    password_length = int(input("How lengthy do you want your password to be?: "))
    characters = list(string.ascii_letters + string.digits + "_$-/!")
    random.shuffle(characters)

    generated_password = []

    for char in range(password_length):
        generated_password.append(random.choice(characters))

    random.shuffle(generated_password)
    generated_password = "".join(generated_password)    
    print(str(generated_password))


print("Do you want to generate your password?")

while True:

    decision = input("Please enter Yes / No: ").lower()


    if decision == "yes":
        pass_generate()
        print("Program ended succesfuly :)")

    elif decision == "no":
        print("Program ended succesfuly")
        break
    
    else:
        print("Options invalid")
        print("Please enter Yes / No")