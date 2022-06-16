import time
from time import sleep
from .system import get_system_info

def genre_from_cpu():
    cpu_percentage = get_system_info()
    print("cpu percentage " + str(cpu_percentage))
    if cpu_percentage > 37:
        return ["edm", "anime", "dubstep"]
    elif cpu_percentage > 27:
        return ["hip-hop", "rock", "country", "soundtracks"]
    elif cpu_percentage > 18:
        return ["jazz", "psych-rock", "r-n-b"]
    else: return ["study", "classical", "chill"]

def schedule_cpu_check():
    t0 = time.time()
    while True:
        t1 = time.time()
        if (t1 - t0 > 300):
            t0 = t1
            print(genre_from_cpu())
        #if button is clicked kill code