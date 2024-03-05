questions = {
    "Who is the president of the United States?": "Joe Biden",
    "What is the capital of France?": "Paris",
    "What is the largest mammal in the world?": "Blue whale", 
    "Who is the first president of India": "Dr. Rajendra Prasad"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + "\n")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + answer)

print("Quiz complete! You scored", score, "out of", len(questions))