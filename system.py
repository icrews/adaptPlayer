import platform
import multiprocessing
import psutil

def get_system_info():
    sys = platform.platform()
    if sys[0:3] == "mac":
        get_mac_sys_info()
    elif sys[0:3] == "Win":
        get_windows_sys_info()
    else: print("err")

def get_mac_sys_info():
    print("mac")
    print("cpu usage percentage: %s" %  psutil.cpu_percent())
    # print(psutil.cpu_stats())
    # print(psutil.cpu_freq())
    return

def get_windows_sys_info():
    print("win")
    print("cpu usage percentage: %s" %  psutil.cpu_percent())
    return

if __name__ == '__main__':
	get_system_info()



