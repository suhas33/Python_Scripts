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
        os.system("bin/./clogin -x "+directory+"custom "+switch[0]+" >> "+ directory + "/Post_Change/" +switch[1]+".txt")
  else:
        os.system("bin/./clogin -x "+directory+"custom "+switch[0]+" >> "+ directory + "/Post_Change/" +switch[1]+".txt")