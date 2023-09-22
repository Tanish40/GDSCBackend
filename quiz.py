from question_data import question_data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def check_answer(self, user_answer):
        current_question = self.questions[self.current_question_index - 1]
        if user_answer.lower() == current_question.answer.lower():
            self.score += 2
        else:
            self.score -= 1

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def run_quiz(self):
        while self.do_questions_remain():
            current_question = self.next_question()
            if current_question:
                print(current_question.text)
                user_answer = input("True or False? ").strip()
                self.check_answer(user_answer)

        print(f"Your final score: {self.score}")

if __name__ == "__main__":
    quiz = Quiz([Question(q["text"], q["answer"]) for q in question_data])
    quiz.run_quiz()















