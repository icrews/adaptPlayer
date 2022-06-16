import time
from time import sleep
from system import get_system_info

def genre_from_cpu():
    cpu_percentage = get_system_info()
    print("cpu percentage " + str(cpu_percentage))
    if cpu_percentage > 30:
        return "edm"
    elif cpu_percentage > 22:
        return "rap"
    elif cpu_percentage > 18:
        return "rock"
    else: return "lofi"

def schedule_cpu_check():
    t0 = time.time()
    while True:
        t1 = time.time()
        if (t1 - t0 > 5):
            t0 = t1
            print(genre_from_cpu())
        #if button is clicked kill code