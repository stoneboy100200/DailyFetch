#!/usr/bin/python
# *******************************************
# AUTHOR: Li Seven
# MAIL: Seven.Li@cn.bosch.com
# BRIEF: Fetch src code from remote everyday
# *******************************************

import os,subprocess,sys


NINCG3_PATH="/home/lse9szh/project/nincg3"
if not os.path.exists(NINCG3_PATH):
   print "[Error] %s doesn't exist!" %NINCG3_PATH
   sys.exit()

os.chdir(NINCG3_PATH)
print "Repository:", os.getcwd()
subprocess.call(["git", "fetch", "origin"])
