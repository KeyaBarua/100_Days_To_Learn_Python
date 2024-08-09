class QuizBrain:
    def __init__(self, ques_list):
        self.ques_num = 0
        self.ques_list = ques_list
        self.score = 0

    def still_has_questions(self):
        """Checks if there are more questions"""
        return self.ques_num < len(self.ques_list)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong! The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.ques_num}\n")

    def next_question(self):
        """Gets the current question number and gets the question at that position"""
        current_question = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_answer = input(f"Q.{self.ques_num}: {current_question.text} (True/ False)?: ")
        self.check_answer(user_answer, current_question.answer)

