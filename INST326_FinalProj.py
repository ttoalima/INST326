import random
import time
import argparse
import csv


class Student:
    def __init__(self, name, grade, interests, availability, study_goals):
        """
        Initializes a new Student object.
        
        Args:
        - name (str): Name of the student.
        - grade (str): Grade level of the student.
        - interests (list): List of the student's interests.
        - availability (dict): Dictionary of availability (e.g., days of the week and times).
        - study_goals (dict): Dictionary with subjects as keys and target study hours as values.
        """
        self.name = name
        self.grade = grade
        self.interests = interests
        self.availability = availability
        self.study_goals = study_goals  # target hours per subject
        self.progress = {subject: 0 for subject in study_goals}  # actual hours spent per subject
        self.study_time = {}  # track time per study session
        self.study_hours = 0  # total hours studied
        self.scheduled_sessions = []
        
    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_interests(self):
        return self.interests

    def get_availability(self):
        return self.availability

    def get_study_goals(self):
        return self.study_goals

    def get_progress(self):
        return self.progress

    def get_study_time(self):
        return self.study_time

    def get_study_hours(self):
        return self.study_hours

    def get_scheduled_sessions(self):
        return self.scheduled_sessions
        
# Progress Tracking + Goals
    def update_progress(self, subject, hours_studied):
        """
        Updates the progress for a specific subject by adding study hours.

        Args:
        - subject (str): The subject being studied.
        - hours_studied (int): The number of hours studied.

        Returns:
        - dict: The updated progress dictionary.
        """
        if subject not in self.study_goals:
            print(f"{subject} is not in the study goals. Please set a study goal first.")
            return self.progress

        self.progress[subject] += hours_studied
        self.study_hours += hours_studied
        if self.progress[subject] >= self.study_goals[subject]:
            print(f"{self.name} has met the study goal for {subject}!")
        return self.progress



    def get_progress_report(self):
        """
        Generates a progress report comparing actual study hours against target study goals.

        Returns:
        - dict: A dictionary showing each subject's target vs actual hours and the status.
        """
        report = {}
        for subject, target_hours in self.study_goals.items():
            actual_hours = self.progress.get(subject, 0)
            status = "On Track" if actual_hours >= target_hours else "Falling Behind"
            report[subject] = {
                "Target Hours": target_hours,
                "Actual Hours": actual_hours,
                "Status": status
            }
        return report
        
# Break Reminders and Study Tips
    def set_study_goal(self, subject, target_hours):
        """
        Sets or updates the study goal for a specific subject.

        Args:
        - subject (str): The subject for which to set the goal.
        - target_hours (int): The target study hours for the subject.

        Returns:
        - dict: The updated study goals dictionary.
        """
        self.study_goals[subject] = target_hours
        if subject not in self.progress:
            self.progress[subject] = 0  # Initialize progress for the new subject
        print(f"Set a study goal of {target_hours} hours for {subject}.")
        return self.study_goals


# Smart Study Partner Matching
def match_score(student1, student2):
    """
    Calculates a compatibility score between two students based on matching attributes.
    
    Args:
    - student1 (Student): The first student to compare.
    - student2 (Student): The second student to compare.
    
    Returns:
    - int: The compatibility score based on matching interests, grade, and availability.
    """
    score = 0
    if student1.get_grade() == student2.get_grade():
        score += 50  # Same grade adds to compatibility
    if set(student1.get_interests()).intersection(set(student2.get_interests())):
        score += 50  # Shared interests add to compatibility
    return score

def find_study_partner(student, other_students, criteria=None):
    """
    Finds the best study partner based on specified criteria such as shared interests, grade level, etc.
    
    Args:
    - student (Student): The student looking for a study partner.
    - other_students (list): List of other Student objects to compare with.
    - criteria (list): Optional list of criteria for compatibility (e.g., shared interests, grade level).
    
    Returns:
    - tuple: The best partner and their compatibility score.
    """
    best_score = 0
    best_partner = None
    for other_student in other_students:
        if other_student != student:
            score = match_score(student, other_student)
            if score > best_score:
                best_score = score
                best_partner = other_student
    return best_partner, best_score

# Study Session Scheduler
def suggest_study_times(student, partner):
    """
    Suggests common study times based on both students' availability.
    
    Args:
    - student (Student): The first student whose availability is being checked.
    - partner (Student): The second student whose availability is being checked.
    
    Returns:
    - list: A list of times where both students are available to study.
    """
    common_times = [
        f"{day}: {student.get_availability()[day]}"
        for day in student.get_availability()
        if day in partner.get_availability()
    ]
    return common_times

def set_study_session(student, partner, time_slot):
    """
    Schedules a study session for two students and updates their schedules.
    
    Args:
    - student (Student): The first student to update their schedule.
    - partner (Student): The second student to update their schedule.
    - time_slot (str): The time the study session is scheduled for.
    """
    session = {
        'students': (student.get_name(), partner.get_name()),
        'time': time_slot
    }
    student.scheduled_sessions.append(session)
    partner.scheduled_sessions.append(session)
    print(f"Study session scheduled between {student.get_name()} and {partner.get_name()} at {time_slot}.")

# Break Reminders and Study Tips
def set_break_reminder(break_time_minutes):
    """
    Reminds the user to take a break after a specified time.
    """
    while True:
        print("Starting break timer...")
        break_time_seconds = break_time_minutes * 60
        time.sleep(break_time_seconds)
        print("Take a break!")

        break_time = break_time_seconds / 4
        time.sleep(break_time)
        print("Break over, back to work! Remember to set another break!")

        # Explicitly print the prompt for better testing visibility
        print("Restart timer?\n(Yes/No)\n", end="")
        restart_timer = input().upper()
        print(f"Input received: {restart_timer}")

        if restart_timer == "YES":
            continue
        elif restart_timer == "NO":
            break
        else:
            print("Invalid input. Exiting.")
            break


def study_tips():
    """
    Returns a random study tip to the user.

    Reads tips from a file named 'tips.txt'. If the file is missing or empty, 
    provides an appropriate message to the user.
    """
    tip_bank = []
    try:
        with open("tips.txt") as fc:
            for tip in fc:
                tip_bank.append(tip.strip())
    except FileNotFoundError:
        print("File is missing! Please ensure tips.txt is in the same folder.")
        return

    if not tip_bank:
        print("No tips available in the file.")
        return

    random_tip = random.choice(tip_bank)
    print(f"Here's a tip!: '{random_tip}'")

if __name__ == "__main__":
    # Entry point for the script
    parser = argparse.ArgumentParser(description='Read a CSV file from the command line.')
    parser.add_argument('csv_file', type=str, help='The path to the CSV file.')
    args = parser.parse_args()
