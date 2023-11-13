def add(input_1, input_2):
    result = input_1 + input_2
    print(f"${str(input_1)} + ${str(input_2)} = ${str(result)}") 


def sub(input_1, input_2):
     result = input_1 - input_2
     print(f"{str(input_1)} - {str(input_2)} = {str(result)}") 

def mul(input_1, input_2):
     result = input_1 * input_2
     print(f"{str(input_1)} * {str(input_2)} = {str(result)}") 


def div(input_1, input_2):
     result = input_1 / input_2
     print(f"{str(input_1)} / {str(input_2)} = {str(result)}")


prompts = """
A - Addition
S - Substraction
M - Multiplication
D - Division
E - Exit!
"""

print(prompts)


while True:
    calc_prompt= input("> ").upper()
    if calc_prompt == "A":
        calc_input_1 = int(input('Enter input one '))
        calc_input_2 = int(input("Enter input two "))
        add(calc_input_1, calc_input_2)
    elif calc_prompt == "S":
        calc_input_1 = int(input('Enter input one '))
        calc_input_2 = int(input("Enter input two "))
        sub(calc_input_1,calc_input_2)
    elif calc_prompt == "M":
         calc_input_1 = int(input("Enter input one "))
         calc_input_2 = int(input("Enter input two "))
         mul(calc_input_1, calc_input_2)
    elif calc_prompt == "D":
         calc_input_1 = int(input("Enter input one "))
         calc_input_2 = int(input("Enter input two "))
         div(calc_input_1, calc_input_2)
    elif calc_prompt == "E":
         print("Progam successfully ended :) ")
         break
    elif not calc_prompt ==  "A" or not calc_prompt == "S" or calc_prompt == "D" or not calc_prompt == "M" or not calc_prompt == "E":
         print("Prompt not recognized :(!")
         print(prompts)
         print(f"Please enter new prompt! \n {prompts}")



   
        
        
     