
from Question import Question
question_file=open("questions.txt","r")
Ques_prompt=question_file.readlines()
questions_easy=[
    Question(Ques_prompt[0], "a"),
    Question(Ques_prompt[1] , "d"),
    Question(Ques_prompt[2], "b"),
    Question(Ques_prompt[3], "d"),
    Question(Ques_prompt[4], "a")
]
questions_medium=[
    Question(Ques_prompt[7], "d"),
    Question(Ques_prompt[8] , "a"),
    Question(Ques_prompt[9], "c"),
    Question(Ques_prompt[10], "c"),
    Question(Ques_prompt[11], "a")
]
questions_hard=[
    Question(Ques_prompt[14], "c"),
    Question(Ques_prompt[15] , "c"),
    Question(Ques_prompt[16], "c"),
    Question(Ques_prompt[17], "a"),
    Question(Ques_prompt[18], "d")
]
def exam(questions_easy):
    marks=0
    for question in questions_easy:
        answer = input(question.prompt)
        if answer == question.answer:
            marks+=1
    if marks==1 or marks==0:
     print("you are  poor in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
    elif marks==2:
        print("you are bad in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
    elif marks==3:
        print("you are good in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
    elif marks==4:
        print("you are strong in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
    elif marks==5:
        print("you are very strong in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
i=int(input("select any level 1.easy 2.medium 3.hard"))
if i==1:
  exam(questions_easy)
elif i==2:
    def exam(questions_medium):
        marks = 0
        for question in questions_medium:
            answer = input(question.prompt)
            if answer == question.answer:
                marks += 1
        if marks == 1 or marks == 0:
            print("you are  poor in general knowledge you got " + str(marks) + "/" + str(len(questions_easy)) + " correct")
        elif marks == 2:
            print("you are bad in general knowledge you got " + str(marks) + "/" + str(len(questions_medium)) + " correct")
        elif marks == 3:
            print("you are good in general knowledge you got " + str(marks) + "/" + str(len(questions_medium)) + " correct")
        elif marks == 4:
            print("you are strong in general knowledge you got " + str(marks) + "/" + str(len(questions_medium)) + " correct")
        elif marks == 5:
            print("you are very strong in general knowledge you got " + str(marks) + "/" + str(len(questions_medium)) + " correct")
    exam(questions_medium)
elif i==3:
    def exam(questions_hard):
        marks = 0
        for question in questions_hard:
            answer = input(question.prompt)
            if answer == question.answer:
                marks += 1
        if marks == 1 or marks == 0:
            print("you are  poor in general knowledge you got " + str(marks) + "/" + str(len(questions_hard)) + " correct")
        elif marks == 2:
            print(
                "you are bad in general knowledge you got " + str(marks) + "/" + str(len(questions_hard)) + " correct")
        elif marks == 3:
            print(
                "you are good in general knowledge you got " + str(marks) + "/" + str(len(questions_hard)) + " correct")
        elif marks == 4:
            print("you are strong in general knowledge you got " + str(marks) + "/" + str(len(questions_hard)) + " correct")
        elif marks == 5:
            print("you are very strong in general knowledge you got " + str(marks) + "/" + str(len(questions_hard)) + " correct")
    exam(questions_hard)

