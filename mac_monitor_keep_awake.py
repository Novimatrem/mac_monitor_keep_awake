import subprocess
from subprocess import call
import time

def prevent_sleep():
    """Forces display, system, and disk to stay awake at full power."""
    try:
        subprocess.Popen(["caffeinate", "-dimu", "-t", "60"])
    except FileNotFoundError:
        pass

def prevent_sleeptwo():
    """Forces display, system, and disk to stay awake at full power."""
    try:
        subprocess.Popen(["caffeinate"])
    except FileNotFoundError:
        pass

def prevent_crash():
    """makes sure that spawning a coffee constantly doesn't actually hurt perf"""
    try:
        subprocess.Popen(["killall", "caffeinate"])
    except FileNotFoundError:
        pass

while (True):
	{
    prevent_crash(), # makes sure that spawning a coffee constantly doesn't actually hurt perf
    print("woke"),
    prevent_crash(), # makes sure that spawning a coffee constantly doesn't actually hurt perf
    time.sleep(1.5),
    prevent_crash(), # makes sure that spawning a coffee constantly doesn't actually hurt perf
    prevent_sleep(),
    prevent_sleeptwo(),
    time.sleep(1.5), # don't lag the system with many attempts super quickly
    prevent_crash() # makes sure that spawning a coffee constantly doesn't actually hurt perf
    
}

