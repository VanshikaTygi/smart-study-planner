# Smart Study Planner :--

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

# Stores all study session records as dictionaries
study_sessions = []

def add_session() :
    """
    Collects study/revision session data from the user
    and stores it as a structured dictionary.
    """

    subject = input("Enter the subject: ").strip()

    try :
        hours = float(input("Enter study duration (in hours): "))

        if (hours <= 0) :
            print("Study duration must be positive.")
            return
    
    except ValueError :
        print("Invalid input. Please enter a number.\n")
        return
    
    session_type = input("Enter the session type (Study/Revision): ").strip().capitalize()
    if session_type not in ["Study", "Revision"] :
        print("Invalid session type.")
        return
    
    # Each session is stored as a dictionary for easy aggregation later
    session = {
        "subject" : subject,
        "hours" : hours,
        "type" : session_type,
        "datetime" : datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    study_sessions.append(session)
    print("✅ Session added Succeccfully.\n")


def view_summary() :
    """
    Displays total study time, subject-wise breakdown,
    and study vs revision distribution.
    """

    if not study_sessions :
        print("No study sessions recorded yet.\n")
        return
    
    total_hours = 0
    subject_total = {}
    study_hours = 0
    revision_hours = 0

    # Aggregate study data subject-wise and by session type
    for session in study_sessions :
        hours = session["hours"]
        subject = session["subject"]
        session_type = session["type"]

        total_hours += hours

        subject_total[subject] = subject_total.get(subject, 0) + hours

        if session_type == "Study" :
            study_hours += hours
        else :
            revision_hours += hours

    print("\n📊 Study Summary")
    print(f"Total Study time: {total_hours:.2f} hours")

    print("\nSubject-wise Breakdown: ")
    for subject, hours in subject_total.items() :
        print(f"- {subject} : {hours:.2f} hours")

    print(f"\nStudy Time: {study_hours:.2f} hours")
    print(f"Revision Time: {revision_hours:.2f} hours\n")


def view_insights() :     # Insights are heuristic-based (rule-based), not ML-driven
    """
    Generates rule-based insights by analyzing study patterns.
    Uses thresholds and proportions to give actionable feedback.
    """
    
    if not study_sessions :
        print("No study data available for insights.\n")
        return
    
    total_hours = sum(session["hours"] for session in study_sessions)

    subject_totals = {}
    revision_hours = 0

    for session in study_sessions :
        subject = session["subject"]
        hours = session["hours"]
        subject_totals[subject] = subject_totals.get(subject, 0) + hours

        if session["type"] == "Revision" :
            revision_hours += hours

    print("\n🧠 Smart Study Insights : ")

    for subject, hours in subject_totals.items() :
        percentage = (hours / total_hours) * 100

        if percentage > 50 :
            print(f"⚠️ You are spending too much time on {subject}. Try balancing other subjects also.\n")

    if total_hours < 3 :
        print("⚠️ Your total study time is low today. Try increasing focus time.\n")

    if revision_hours < (0.2 * total_hours) :
        print("⚠️ Revision time is low. Consider revising studied topics.\n")

    if (total_hours >= 5) :
        print("✅ Good job! You had a productive study day.\n")


def productivity_score() :      # Productivity score is heuristic-based, not ML
    """
    Calculates a productivity score (out of 100)
    using heuristic-based rules such as:
    - Total study time
    - Revision balance
    - Subject distribution
    """

    if not study_sessions :
        print("No study data available.\n")
        return
    
    total_hours = sum(s["hours"] for s in study_sessions)

    subject_total = {}
    revision_hours = 0

    for s in study_sessions :
        subject_total[s["subject"]] = subject_total.get(s["subject"], 0) + s["hours"]

        if s["type"] == "Revision" :
            revision_hours += s["hours"]

    # Score is built incrementally based on multiple productivity factors
    score = 0

    # Time-based score
    if total_hours >= 5 :
        score += 40
    elif total_hours >= 3 :
        score += 25

    # Revision balance
    if revision_hours >= (0.2) * total_hours :
        score += 20

    # Subject balance
    for hours in subject_total.values() :
        if (hours / total_hours) > 0.6 :
            break
    else :
        score += 20

    print(f"\n📈 Productivity Score: {score} / 100 ")

    if (score >= 80) :
        print("🔥 Excellent productivity today!\n")

    elif score >= 60 :
        print("👍 Good work, keep improving.\n")

    else :
        print("⚠️ Try to study more consistently.\n")


def show_menu() :
    """Displays the main menu options to the user."""

    print("====== Smart Study Planner ======")
    print("1. Add Study Session")
    print("2. View Study Summary")
    print("3. View Smart Insights")
    print("4. View Productivity Score")
    print("5. Exit")


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
            view_insights()
        elif choice == "4" :
            productivity_score()
        elif choice == "5" :
            print("Thank You! Bye. Keep studying smart 📚")
            break
        else :
            print("Invalid choice. Try again!\n")


# Entry point of the program
if __name__ == "__main__" :
    main()
    
