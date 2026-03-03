# Smart Study Planner :--

# Main file (control layer) :-

"""
Smart Study Planner (Rule-Based)

This is a console-based productivity and study analysis system.
It uses rule-based (heuristic) logic to analyze study patterns,
generate insights, and calculate a productivity score.

NOTE:
- This project uses rule-based intelligence, NOT machine learning.
- All decisions are based on predefined logical rules.
- Designed to be explainable, interpretable, and beginner-friendly.
"""

# Used to timestamp each study session (date & time tracking)
from datetime import datetime

from tracker import study_sessions, add_session, view_summary 
from analytics import evaluate_day

def show_menu() :
    """Displays the main menu options to the user."""

    print("====== Smart Study Planner ======")
    print("1. Add Study Session")
    print("2. View Study Summary")
    print("3. Evaluate Day")
    print("4. Exit")


def main() :
    """
    Main control loop of the application.
    Continuously runs until the user chooses to exit.
    """

    while True :
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1" :
            add_session()
        elif choice == "2" :
            view_summary()
        elif choice == "3" :
            evaluate_day()
        # elif choice == "4" :
        #     productivity_score()
        elif choice == "4" :
            print("Thank You! Bye. Keep studying smart 📚")
            break
        else :
            print("Invalid choice. Try again!\n")


# Entry point of the program
if __name__ == "__main__" :
    main()
    
