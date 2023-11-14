print("Enter your message :)")
input_data = input("> ")
emoji_data = {
    ":)" : "😂",
    ":(" : "😣"
}

input_split = input_data.split(' ')
new_message = ''

for word in input_split:
    new_message += emoji_data.get(word, word) + " "

print(new_message)