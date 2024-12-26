import json
import random
import time
import os

def load_questions():
    # Load questions from a JSON file
    if not os.path.exists("questions.json"):
        print("Error: 'questions.json' file not found!")
        return {}

    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions

def save_high_score(player_name, score):
    # Save high scores to a file
    high_scores_file = "high_scores.json"
    if os.path.exists(high_scores_file):
        with open(high_scores_file, "r") as file:
            high_scores = json.load(file)
    else:
        high_scores = {}

    high_scores[player_name] = max(high_scores.get(player_name, 0), score)
    with open(high_scores_file, "w") as file:
        json.dump(high_scores, file, indent=4)

def display_leaderboard():
    # Display leaderboard
    high_scores_file = "high_scores.json"
    if not os.path.exists(high_scores_file):
        print("No high scores yet!")
        return

    with open(high_scores_file, "r") as file:
        high_scores = json.load(file)

    print("\nLeaderboard:")
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)
    for rank, (name, score) in enumerate(sorted_scores, 1):
        print(f"{rank}. {name}: {score}")
    print()

def play_quiz(player_name, category, questions):
    print(f"\nHello, {player_name}! You selected the category: {category}\n")
    print("Answer the questions within the time limit! Type 'exit' anytime to quit.\n")

    random.shuffle(questions)
    score = 0
    time_limit = 15  # seconds per question

    for index, question in enumerate(questions, 1):
        print(f"Question {index}/{len(questions)}: {question['question']}")
        for option in question["options"]:
            print(option)

        start_time = time.time()
        user_answer = input("\nYour answer: ").strip().upper()
        end_time = time.time()

        if user_answer == "EXIT":
            print("You chose to exit the quiz.")
            break

        if end_time - start_time > time_limit:
            print("Time's up! Moving to the next question.\n")
            continue

        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    print(f"\n{player_name}, your final score: {score}/{len(questions)}")
    save_high_score(player_name, score)

def quiz_bot():
    questions_by_category = load_questions()
    if not questions_by_category:
        return

    print("Welcome to the Advanced Quiz Bot!")

    while True:
        print("Select a category:")
        for idx, category in enumerate(questions_by_category.keys(), 1):
            print(f"{idx}. {category}")

        try:
            category_choice = int(input("Enter the category number: "))
            category = list(questions_by_category.keys())[category_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        player_name = input("Enter your name: ")
        questions = questions_by_category[category]
        play_quiz(player_name, category, questions)

        # Ask if another user wants to play
        another_user = input("\nWould another user like to play? (yes/no): ").strip().lower()
        if another_user != "yes":
            break

    display_leaderboard()
    print("Thank you for playing!")

if __name__ == "__main__":
    quiz_bot()