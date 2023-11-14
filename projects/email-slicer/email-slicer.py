def slice_email(condition):
    if slice_question == condition:
        slice_input = input('Enter your email :) ')
        split_input = slice_input.split("@")
        (username, domain) = split_input
        (url, extension) = domain.split(".")
        print("Username - " + username)
        print("Domain - " + domain)
        

while True:
    print("Enter Yes or No")
    slice_question = input("Do you want to slice your mail? ").capitalize()
    if slice_question == "Yes":
        slice_email(slice_question)

    elif slice_question == "No":
        print("Oops, seems you don't wanna slice your email :(")
        print("Run the program again")
        break

    else :
        print("Incorrect response")

