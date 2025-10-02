class QuizApp:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of india?",
                "options": ["A. Berlin", "B. Madrid", "C. delhi", "D. Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. J.K. Rowling"],
                "answer": "C"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz App!\n")
        for i, q in enumerate(self.questions, start=1):
            print(f"Q{i}: {q['question']}")
            for option in q["options"]:
                print(option)
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")



quiz = QuizApp()
quiz.start_quiz()
