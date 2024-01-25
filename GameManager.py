

class GameManager:

    def __init__(self):
        self.array_questions = None
        self.score = 0
        self.front_end = None

    def config_game(self, array_questions, front_end):
        self.array_questions = array_questions
        self.front_end = front_end

    def return_question(self, number):
        if len(self.array_questions) > number:
            return self.array_questions[number]
        else:
            return -1

    def update_score(self, number_question, anwser):
        if self.array_questions[number_question]["resposta_correta"].lower() == anwser.lower():
            self.score += 1
