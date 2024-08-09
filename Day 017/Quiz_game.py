from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Empty list
question_bank = []

# Looping through the question data
for q_data in question_data:
    new_q = Question(q_data["question"], q_data["correct_answer"])
    question_bank.append(new_q)

# Gets the questions from the question bank
quiz = QuizBrain(question_bank)

# Loops until we have reached the end of the question list
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{quiz.ques_num}")
