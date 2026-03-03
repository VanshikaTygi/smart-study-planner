# Tracker file (data collection) :-


# Used to timestamp each study session (date & time tracking)
from datetime import datetime

# In-memory storage (temporary - will connect to CSV in next step)
study_sessions = []


def add_session() :
    """
    Collects study/revision session data from the user
    and stores it as a structured dictionary.
    """

    subject = input("Enter the subject: ").strip().title()

    try :
        hours = float(input("Enter study duration (in hours): "))

        if (hours <= 0) :
            print("Study duration must be positive.")
            return
    
    except ValueError :
        print("Invalid input. Please enter a number.\n")
        return
    

    STUDY_KEYWORDS = {"study", "learn", "learning", "reading", "practice", "coding"}
    REVISION_KEYWORDS = {"revision", "revise", "review"}

    raw_type = input("Enter the session type (Study/Revision): ").strip().lower()

    if raw_type in STUDY_KEYWORDS :
        session_type = "Study"
    elif raw_type in REVISION_KEYWORDS :
        session_type = "Revision"
    else :
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

        # Initialize subject dictionary if not exists
        if subject not in subject_total :
            subject_total[subject] = {
                "Study" : 0,
                "Revision" : 0
            }

        subject_total[subject][session_type] += hours

        if session_type == "Study" :
            study_hours += hours
        else :
            revision_hours += hours

    print("\n📚📊 Study Summary")
    print("-" * 40)

    print("\nSubject-wise Breakdown: ")
    for subject, data in subject_total.items() :
        study = data["Study"]
        revision = data["Revision"]
        total = study + revision

        print(f"\n📘 {subject} ")
        print(f"  Study     :  {study:.2f} hours")
        print(f"  Revision  :  {revision:.2f} hours")
        print(f"  Total     :  {total:.2f} hours")

    print("\n" + "-" * 40)
    print(f"\nTotal Study Time: {study_hours:.2f} hours")
    print(f"Total  Revision Time: {revision_hours:.2f} hours\n")
    print(f"Grand Total Time: {total_hours:.2f} hours\n")



