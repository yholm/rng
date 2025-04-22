import random 
import time
import os

categories = [
    ("Trash", 50.0),       
    ("Mediocre", 28.0),    
    ("Above Average", 12.0), 
    ("Fabled", 6.5),      
    ("Mythical", 2.6),     
    ("Ancient", 0.9),      
    ("Whimsical", 0.8),    
    ("Omnipotent", 0.1)    
]

category_names, probabilities = zip(*categories)

def spin_wheel():
    print("Click enter to Spin...")
    input() # Wait for user input 

    print("\nSpinning...", end="") 
    for _ in range(3): 
        for category in category_names: 
            print(f"\r{category}", end="", flush=True)  
            time.sleep(0.1)

    print("\r...Selecting...", end="", flush=True)
    time.sleep(0.5)

    chosen_category = random.choices(category_names, probabilities)[0]
    
    print(f"\nCongrats! You got: {chosen_category}")
spin_wheel()