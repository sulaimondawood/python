quiz ={
    "question 1": {
        "question" : "What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question 2":{
        "question" : "What is the name of Nigeria's President?",
        "answer": "Bola Ahmed Tinubu"
       
    },
    "question 3": {
        "question": "What level is Dawood currently in?",
        "answer": 200
    },
    "question 4": {
        "question":  "Where is University of  Ilorin located?",
        "answer": "Ilorin"
    }
}

score =0
for key, value in quiz.items():
    print(key, ": " + value.get("question"))
    answer = input("Enter your answer ").lower()

    if(str(value.get("answer")).lower() == answer ):
        score+=1
        print("Your score is " + str(score) + '\n')

    else:
        print("Wrong! :(")
        print("Your new score is " + str(score))
        print("The right answer is " + value["answer"] + "\n")
 

total_score = f"Your total score is {score} / {len(quiz.items())}"
print(total_score)
your_percentage = f"Your percentage is {(score / len(quiz.items())) * 100}%"
print(your_percentage)