#!/usr/bin/env python3
"""
Program: shopping_reminder_add_items.py

Description: Add items to my "Shopping" list in the Apple Reminders
application.

Author: Brett Hutley <brett@hutley.net>
Date: 2022-10-04
License: MIT License

"""
import subprocess
import sys


def add_reminder_to_shopping_list(item):
    applescript = '''
    tell application "Reminders"
        tell list "Shopping"
            make new reminder at end with properties {name:"%s"}
        end tell
    end tell
    ''' % (item, )
    subprocess.run(['/usr/bin/osascript', '-e', applescript])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <item to add>")
        print(__doc__)
        exit(1)

    for i in range(1, len(sys.argv)):
        add_reminder_to_shopping_list(sys.argv[i])
