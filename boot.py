import board
import storage

#True:  save/edit CPX code enabled.  Write files to CPX disabled
#False: save/edit CPX code disabled. Write files to CPX enabled
storage.remount("/", readonly=False) 


#To allow CPX code editing again, go to REPL and change this file name to BAK
import os
os.listdir("/")
os.rename("/boot.py", "/boot.bak")