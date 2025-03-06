class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.player_score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):\n")
        self.check_answer(player_answer, current_question.answer)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            print("You got it correct!")
            self.player_score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.player_score}/{self.question_number}\n")
        