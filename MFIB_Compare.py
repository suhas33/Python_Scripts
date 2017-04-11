#!/usr/bin/env python
import os
import time
import re
import subprocess
import difflib
import datetime

# Timestamp on Filename
today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday1 = datetime.datetime.now() - datetime.timedelta( days = 1 )
yesterday = yesterday1.strftime("%Y-%m-%d")

directory = 'Route_Table/'

if not os.path.exists(directory+today):
    os.makedirs(directory+today)

with open(directory+'Device_list.txt') as f:
  list_cores = [line.split() for line in f]

for switch in list_cores:
  if switch[2] == 'A':
	os.system("bin/./clogin -x "+directory+"arista_mfib "+switch[0]+" >> "+ directory + today + "/" +switch[1]+"_mfib.txt")
  else:
	os.system("bin/./clogin -x "+directory+"cisco_mfib "+switch[0]+" >> "+ directory + today + "/" +switch[1]+"_mfib.txt")
  file1 = directory + today + "/" +switch[1]+"_mfib.txt"
  file2 = directory + yesterday + "/" +switch[1]+"_mfib.txt"
  diff = difflib.unified_diff(open(file2).readlines(),open(file1).readlines())
  lines = list(diff)[2:]
  added = [line[1:] for line in lines if line[0] == '+']
  removed = [line[1:] for line in lines if line[0] == '-']
  with open (directory+'Diff_' + today + '_mfib.txt', 'a') as changefromyesterday:
	   changefromyesterday.write("-------------------------------------------------------------\n")
	   changefromyesterday.write(switch[1]+"\n")
	   changefromyesterday.write("-------------------------------------------------------------\n")
	   for line in added:
		   if line not in removed:
			   changefromyesterday.write("Added: " + line)
	
	   for line in removed:
		   if line not in added:
			   changefromyesterday.write("Removed: " + line)
changefromyesterday.close()
os.system ("cat "+directory+"Diff_"+today+"_mfib.txt | grep -v login")