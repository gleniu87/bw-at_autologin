# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:13:19 2022

@author: tomas
"""

import os
import psutil
import pyuac
import time
import sys
from pywinauto import Application
from ctypes import *

def autoLogin():
    os.system("taskkill /im bw-at.exe")
    file = open("mpw.txt", "r")
    password = file.readline()
    file.close()
    app = Application().start("bw-at.exe")
    app.window(title='Bitwarden Auto-Type').wait(
        'exists enabled visible active', timeout=10)
    app.BitwardenAutoType.type_keys(password + "{ENTER}", pause=0)
    
def checkIfProcessExists(processName):
    for proc in psutil.process_iter():
        if processName.lower() in proc.name().lower():
            return True           
    return False

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin(["pythonw.exe"] + sys.argv)
else:
    locked = True
    while locked:
        locked = checkIfProcessExists("LogonUI.exe")
        if locked:
            time.sleep(1)                  
    windll.user32.BlockInput(True)
    autoLogin()
    windll.user32.BlockInput(False)