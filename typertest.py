
# Typing Test Project #

import time
import random
import datetime

sentences = [           # List of sentences that will be used in the typing test
    "Have you heard about the chocolate record player? It sounds pretty sweet.",
    "Don't trust trees, they're a bit shady.",
    "The quick brown fox jumps over the lazy dog.",
    "The weather forecast is predicting thunderstorms.",
    "The Netflix show called Suits has interesting characters.",
    "You are currently typing the following letters to form a sentence.",
]

top_scores = []          # Empty list to store top scores achieved in the typing test

# Define a function to check if a date string is in a valid format (day/month/year)
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d/%m/%y')  # Try to parse the date string using the specified format
        return True
    except ValueError:
        return False

# Main function for the typing test
def typing_test(sentences):
    print("////////////////////////////// \n")  
    print("Welcome to the Typing Tester! \n")   
    print("////////////////////////////// \n")

    while True:
        choice = input("Enter 'start' to begin the typing test, 'scores' to view top scores, or 'exit' to quit: ")

        if choice.lower() == 'start':
            break  # Exit the loop and start the typing test
        elif choice.lower() == 'scores':
            if not top_scores:
                print("No top scores available yet.")
            else:
                print("Top scores: ")
                sorted_scores = sorted(top_scores, key=lambda x: x[0], reverse=True)
                for score, name, date, wpm in sorted_scores:
                    print(f"Score: {score}, User: {name}, Date: {date}, Overall WPM: {wpm:.2f}")
        elif choice.lower() == 'exit':
            print("Goodbye!")  # Exit 
            return
        else:
            if choice:
                print("Invalid input. Please enter 'start' to begin, 'scores' to view top scores, or 'exit'.")

    user_name = input("Enter your name: ")  # Username 

    while True:
        date = input("Enter today's date (d/m/y), for example - 1/10/23: ")
        if is_valid_date(date):
            day, month, year = map(int, date.split('/'))  # Parse the day, month, and year from the date string
            break
        else:
            print("Invalid date format or out-of-range date. Please enter a valid date in d/m/y format.")

    random.shuffle(sentences)  # Shuffle the order of sentences to make the test more interesting

    print("\n//////////////////////////////////////////////////////////// \n")
    print("Quick guide: Copy the following sentences accurately to score a point!")
    print("\n//////////////////////////////////////////////////////////// \n")

    # Initialize the typing test
    print("Get ready to type!")
    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)

    print("////////////////////////////// \n")
    print("Type now! \n")
    print("////////////////////////////// \n")

    time_start = time.time()  # Record the start time of the test

    user_score = 0              # Initialize the user's score
    overall_word_count = 0      # Initialize the overall word count
    overall_time = 0            # Initialize the overall time
    sentence_wpm = []           # Initialize a list to store sentence-level WPM scores

    for sentence in sentences:  # Loop through the shuffled sentences
        print(sentence)
        typed_sentence = input()  # Get the user's typed input for the current sentence

        sentence_time = time.time() - time_start  # Calculate the time taken to type the sentence

        if typed_sentence == sentence:  # Check if the typed input matches the original sentence
            words = sentence.split()  # Split the sentence into words
            word_count = len(words)    # Count the number of words in the sentence
            overall_word_count += word_count
            overall_time += sentence_time

            wpm = (word_count / sentence_time) * 60.0  # Calculate the words per minute (WPM) for the current sentence
            sentence_wpm.append(wpm)

            print(f"Correct! Well done. WPM for this sentence: {wpm:.3f}")
        else:
            sentence_time += 4  # Penalty time for incorrect input
            print("Oh no, you typed it wrong!")

        time_start += sentence_time  # Update the start time for the next sentence
        user_score += 1  # Increment the user's score

    # Calculate the overall WPM and average sentence WPM
    overall_wpm = (overall_word_count / overall_time) * 60.0
    average_sentence_wpm = sum(sentence_wpm) / len(sentence_wpm)

    # Output overall and average sentence WPM
    print("\n//////////////////////////////////////////////////////////// \n")
    print(f"You typed a score of {user_score} in {overall_time:.2f} seconds! Your Overall WPM is {overall_wpm:.3f}")
    print(f"Average Sentence WPM: {average_sentence_wpm:.3f}")
    print("\n//////////////////////////////////////////////////////////// \n")

    # Add user_score to top_scores list
    top_scores.append((user_score, user_name, f"{day}/{month}/{year}", overall_wpm))

    while True:
        choice = input("Do you want to play again (type 'play'), view top scores again (type 'scores'), or exit (type 'exit')? ")
        if choice.lower() == 'play':
            typing_test(sentences)
        elif choice.lower() == 'scores':
            if not top_scores:
                print("No top scores available yet.")
            else:
                print("Top scores: ")
                sorted_scores = sorted(top_scores, key=lambda x: x[0], reverse=True)
                for score, name, date, wpm in sorted_scores:
                    print(f"Score: {score}, User: {name}, Date: {date}, Overall WPM: {wpm:.2f}")
        elif choice.lower() == 'exit':
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please enter 'play', 'scores', or 'exit.")

# Main program
typing_test(sentences)