import os
import signal
import subprocess


def kill_browser():
    try:
        if (os.name == 'posix'):
            browser = subprocess.Popen(['pgrep', 'firefox'], stdout=subprocess.PIPE)
            for pid in browser.stdout:
                os.kill(int(pid), signal.SIGTERM)
        if (os.name == 'nt'):
            os.popen("tskill chrome")
    except:
        print("An error occured while exiting browser.")


def kill_server():
    try:
        if (os.name == 'posix'):
            for line in os.popen("ps -a | grep python3"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGTERM)
        elif (os.name == 'nt'):
            os.popen("tskill python")
        else:
            print("Can't find proper OS.")
    except:
        print("An error occured while disabling server.")


def information():
    print('------------------------------------------------------')
    print('------------------------------------------------------')
    print('-----------------------EXITING------------------------')
    print('------------------------------------------------------')
    print('------------------------------------------------------')