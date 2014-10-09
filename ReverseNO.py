# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 20:41:49 2014

@author: girish
"""



import thread
import time
import multiprocessing
# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print("Error: unable to start thread")

while 1:
   pass


