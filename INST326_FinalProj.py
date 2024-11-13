# INST 326
"""
Group Members: Rosane Ndaha, Martin Beck, Toalima Tamasese, Jessica Wu
Assignment: Final Project Check In 1
Date: 11_12_24
"""
import random
import time

# Class and functions within it 

# Smart Study Partner Matching
def match_score(student1, student2):
    """Calculates a compatibility score between two students based on matching attributes.
    
    Args:
        student1: The first student to compare.
        student2: The second student to compare.
        
    Returns:
        score: The compatibility score based on matching interests, grade, and availability.
    """
    score = 0
    if student1.get_grade() == student2.get_grade():
        score += 50  # Same grade adds to compatibility
    if set(student1.get_interests()).intersection(set(student2.get_interests())):
        score += 50  # Shared interests add to compatibility
    return score

def find_study_partner(student, other_students, criteria):
    """Finds the best study partner based on specified criteria such as shared interests, grade level, etc.
    
    Args:
        student: The student looking for a study partner.
        other_students: List of other students to compare with.
        criteria: List of criteria for compatibility (e.g., shared interests, grade level).
        
    Returns:
        best_partner: The student who is the best match for the given student.
        best_score: The compatibility score for the best partner.
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
    """Suggests common study times based on both students' availability.
    
    Args:
        student: The first student whose availability is being checked.
        partner: The second student whose availability is being checked.
        
    Returns:
        common_times: A list of times where both students are available to study.
    """
    common_times = set(student.get_availability()).intersection(set(partner.get_availability()))
    return list(common_times)

def set_study_session(student, partner, time_slot):
    """Schedules a study session for two students and updates their schedules.
    
    Args:
        student: The first student to update their schedule.
        partner: The second student to update their schedule.
        time_slot: The time the study session is scheduled for.
        
    Returns:
        None: Updates the students' schedules with the new session.
    """
    session = {
        'students': (student.get_name(), partner.get_name()),
        'time': time_slot
    }
    student.scheduled_sessions.append(session)
    partner.scheduled_sessions.append(session)
    print(f"Study session scheduled between {student.get_name()} and {partner.get_name()} at {time_slot}.")

# Progress Tracking + Goals

# Break Reminders and Study Tips

def set_break_reminder(break_time_minutes):
    """Reminds user to take a break after a certain amount of time.

    Args: break time in minutes
    
    Returns: take a break message"""
    break_time_seconds = break_time_minutes * 60 #converts input to seconds bc sleep function only takes seconds
    time.sleep(break_time_seconds) #delays message by input time
    print("Take a break!") # break reminder!


def study_tips():
    """returns a study tip to the user when run.
    
    Args: none
    
    Returns: random tip"""
    tip_bank = [] #bank for text to go into
    with open("tips") as fc: #open file with the tips
        for tip in fc: 
            tip_bank.append(tip.strip()) #adds to tip bank 
    random_tip = random.choice(tip_bank) #randomly picks a tip
    print(random_tip) #returns study tip


