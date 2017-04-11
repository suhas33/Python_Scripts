#!/usr/bin/env python
import os
import time
import re
import subprocess
import difflib
import datetime

directory = 'Route_Table/'

with open(directory+'Device_list.txt') as f:
  list_cores = [line.split() for line in f]

for switch in list_cores:
  if switch[2] == 'A':
	os.system("bin/./clogin -x "+directory+"arista "+switch[0]+" >> "+ directory + "/Post_Change/" +switch[1]+".txt")
  else:
	os.system("bin/./clogin -x "+directory+"cisco "+switch[0]+" >> "+ directory + "/Post_Change/" +switch[1]+".txt")
  file1 = directory  + "/Pre_Change/" +switch[1]+".txt"
  file2 = directory  + "/Post_Change/" +switch[1]+".txt"
  diff = difflib.unified_diff(open(file2).readlines(),open(file1).readlines())
  lines = list(diff)[2:]
  added = [line[1:] for line in lines if line[0] == '+']
  removed = [line[1:] for line in lines if line[0] == '-']
  with open (directory+'Manuel_Diff.txt', 'a') as changefromyesterday:
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