# INST 326
import random

# Partner Matching

# Study Session Scheduler

# Progress Tracking + Goals

# Break Reminders and Study Tips

def break_reminders():
    pass

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


