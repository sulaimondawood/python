words_dictionary = {
    "name": "Name is what is used to describe a person",
    "first name": "It is the name given by one's parent",
    "school": "A standart place for learning purpose only",
    "head":"It's is the upper part of the body",
    "daddy" : "Another name for father",
    "pops" : "Synonymous to father"
}

def find_words_meaning():
    word = input('Enter your word: ').lower()
    while True:
        if word == '':
            print("No word entered")
            print("Program terminated!")
            break
    
        if word in words_dictionary:
            print(word, " - " + words_dictionary.get(word, "Word not found:( "))
            word = input("Enter new word: ")

        else:
            print("No word found in the  dictionary")
            print("Program terminated!")
            break

find_words_meaning()