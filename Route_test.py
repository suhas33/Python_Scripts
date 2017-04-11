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

with open(directory+'Device_list_test.txt') as f:
  list_cores = [line.split() for line in f]

for switch in list_cores:
  if switch[2] == A:
	os.system("bin/./clogin -x "+directory+"commands.txt "+switch[0]+" >> "+ directory + today + "/" +switch[1]+".txt")
  elif switch[2] == C:
	os.system("bin/./clogin -x "+directory+"cisco "+switch[0]+" >> "+ directory + today + "/" +switch[1]+".txt")
