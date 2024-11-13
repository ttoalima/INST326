# INST 326
import random
import time

# Partner Matching

# Study Session Scheduler

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


