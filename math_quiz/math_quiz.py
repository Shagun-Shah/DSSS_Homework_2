import random

def get_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.

    Args:
        min_value (int): Minimum value of the range.
        max_value (int): Maximum value of the range.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Select a random mathematical operator from +, -, *.

    Returns:
        str: A random operator ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])

def calculate_answer(num1, num2, operator):
    """
    Calculate the answer based on the provided numbers and operator, and
    generate the corresponding math problem as a string.

    Args:
        num1 (int): The first number in the math problem.
        num2 (int): The second number in the math problem.
        operator (str): The operator for the math problem.

    Returns:
        tuple: A tuple containing:
            - str: A string representation of the math problem.
            - int: The calculated answer.
    """
    problem_statement = f"{num1} {operator} {num2}"
    
    # Corrected operations for each operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2
    
    return problem_statement, answer

def math_quiz():
    """
    Run the Math Quiz game where users are presented with simple math problems.
    They earn a point for each correct answer.
    """
    score = 0
    total_questions = 3  # Changed to an integer for valid loop iteration

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and an operator for the problem
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)  # Changed to integer range to avoid TypeError
        operator = get_random_operator()

        problem, correct_answer = calculate_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for user input
        try:
            user_answer = int(input("Your answer: "))
            
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        
        except ValueError:
            print("Invalid input. Please enter a numerical answer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()