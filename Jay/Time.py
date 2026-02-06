from time import *

def get_time():
    print("The current time is", asctime()[11:16])

def get_date():
    print("The date is", asctime()[:10])

def timer(hours, minutes, seconds):
    total_time = hours * 3600 + minutes * 60 + seconds
    
    for _ in range(total_time):
        time_left = f"{hours:02}:{minutes:02}:{seconds:02}"
        print("Time left:", time_left)
        
        sleep(1)
        seconds -= 1
        
        if seconds < 0:
            minutes -= 1
            seconds = 59
        
        if minutes < 0:
            hours -= 1
            minutes = 59
    
    print("Time's up!")

def alarm(hours, minutes):
    while True:
        current_time = asctime()[11:16]
        if current_time == f"{hours:02}:{minutes:02}":
            print("Alarm ringing!")
            break
        sleep(1)