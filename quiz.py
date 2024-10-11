questions=[
    {
        "prompt":"What is the capital of Senegal?",
        "options": ["A. Kinshasa", "B. Beirut", "C. Dakar", "D. Lagos"],
        "answer": "C"
    },
    {
        "prompt":"What is the largest organ in the human body?",
        "options": ["A. Skin", "B. Liver", "C. Kidney", "D. Tongue"],
        "answer": "A"
    },
    {
        "prompt":"Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Oscar Wilde", "D. Wole Soyinka"],
        "answer": "A"
    },
    {
        "prompt":"What is the chemical symbol for gold?",
        "options": ["A. Gd", "B. Ag", "C. Fe", "D. Au"],
        "answer": "D"
    },
    {
        "prompt":"Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Pluto", "D. Jupiter"],
        "answer": "B"
    },
    {
        "prompt":"Where did sushi originate?",
        "options": ["A. Japan", "B. China", "C. Italy", "D. Nigeria"],
        "answer": "A"
    },
    {
        "prompt":"In what year did the Titanic sink?",
        "options": ["A. 2024", "B. 1996", "C. 1905", "D. 1912"],
        "answer": "D"
    },
    {
         "prompt":"Which element is not found in water?",
         "options": ["A. Carbon", "B. Hydrogen", "C. Oxygen"],
         "answer": "A"
    },
    {
        "prompt":"Which country is home to the Great Barrier Reef?",
        "options": ["A. Kenya", "B. Ireland", "C. Australia", "D. India"],
        "answer": "C"
    },
    {
        "prompt":"What is the rarest and most expensive spice in the world by weight?",
        "options": ["A. Saffron", "B. Vanilla", "C. Cinnamon", "D. Orchid nutmeg"],
        "answer": "A"
    }
]

def run_quiz(questions):
    total_questions=len(questions)
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=input("Enter your answer (A, B, C, or D)")
        if answer==question["answer"].casefold():
            print("Correct! You're so smart.\n")
            score+=1
        else:
            print("You got that wrong!. The correct answer was {0} \n".format(question["answer"]))
        misses=total_questions-score

    print(f"you got {score} questions right and {misses} questions wrong")


run_quiz(questions)
