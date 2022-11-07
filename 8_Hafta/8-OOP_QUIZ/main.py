import Classes
import Question_List

quiz_list = Question_List.question_list

quiz = Classes.Quiz(quiz_list)
quiz.showQuestion()