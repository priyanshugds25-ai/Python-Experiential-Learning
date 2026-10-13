# Online Quiz Management System

quizzes = {}


def create_quiz():
    quiz_name = input("Enter quiz name: ")
    quizzes[quiz_name] = []

    n = int(input("Enter number of questions: "))

    for i in range(n):
        print("\nQuestion", i + 1)
        question = input("Enter question: ")
        option1 = input("Enter option A: ")
        option2 = input("Enter option B: ")
        option3 = input("Enter option C: ")
        option4 = input("Enter option D: ")
        answer = input("Enter correct answer (A/B/C/D): ").upper()

        quizzes[quiz_name].append({
            "question": question,
            "options": [option1, option2, option3, option4],
            "answer": answer
        })

    print("\nQuiz created successfully!")


def view_questions():
    if not quizzes:
        print("No quizzes available.")
        return

    for quiz_name, questions in quizzes.items():
        print("\nQuiz:", quiz_name)

        for i, q in enumerate(questions, 1):
            print("\nQ", i, q["question"])
            print("A.", q["options"][0])
            print("B.", q["options"][1])
            print("C.", q["options"][2])
            print("D.", q["options"][3])


def attempt_quiz():
    if not quizzes:
        print("No quizzes available.")
        return

    print("\nAvailable Quizzes:")
    for name in quizzes:
        print("-", name)

    quiz_name = input("Enter quiz name: ")

    if quiz_name not in quizzes:
        print("Quiz not found.")
        return

    student_name = input("Enter student name: ")
    score = 0
    questions = quizzes[quiz_name]

    for i, q in enumerate(questions, 1):
        print("\nQ", i, q["question"])
        print("A.", q["options"][0])
        print("B.", q["options"][1])
        print("C.", q["options"][2])
        print("D.", q["options"][3])

        answer = input("Enter your answer: ").upper()

        if answer == q["answer"]:
            score += 1

    total = len(questions)
    percentage = (score / total) * 100

    print("\n----- Performance Report -----")
    print("Student Name:", student_name)
    print("Quiz Name:", quiz_name)
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Score:", score, "/", total)
    print("Percentage:", percentage, "%")


def admin_menu():
    while True:
        print("\n----- Admin Menu -----")
        print("1. Create Quiz")
        print("2. Add/View Questions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_quiz()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n===== Online Quiz Management System =====")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()

        elif choice == "2":
            attempt_quiz()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()