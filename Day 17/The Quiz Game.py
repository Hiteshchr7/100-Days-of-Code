from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questions_bank = []
for ques in question_data :
    questions_bank.append(Question(ques["text"],ques["answer"]))

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Final Score:  {quiz.score}/{quiz.question_number}")