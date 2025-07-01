def run_mock_test(questions):
    """
    Runs a simple mock test with multiple-choice questions.

    Args:
        questions: A list of dictionaries, where each dictionary represents a question.
                   Each question dictionary should have the following keys:
                       - "question": The question text.
                       - "options": A list of answer options.
                       - "correct_answer": The index of the correct answer in the options list (0-based).

    Returns:
        The score (number of correct answers).
    """

    score = 0
    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i+1}: {question_data['question']}")

        for j, option in enumerate(question_data['options']):
            print(f"{j+1}. {option}")

        while True:
            try:
                user_answer = int(input("Enter the number of your answer: ")) - 1  # Adjust for 0-based indexing
                if 0 <= user_answer < len(question_data['options']):
                    break  # Valid input, exit the loop
                else:
                    print("Invalid input. Please enter a number between 1 and", len(question_data['options']))
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_answer == question_data['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question_data['correct_answer'] + 1}.") # Show 1-based index

    print(f"\n--- Test Results ---")
    print(f"You scored {score} out of {len(questions)}.")
    return score


# Example Usage:
if __name__ == "__main__":
    test_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": 2
        },
        {
            "question": "What is the value of pi (approximately)?",
            "options": ["3.14", "2.71", "1.61", "4.20"],
            "correct_answer": 0
        },
        {
            "question": "Which programming language is this code written in?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "correct_answer": 1
        }
    ]

    run_mock_test(test_questions)
