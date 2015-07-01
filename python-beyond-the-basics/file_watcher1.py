__author__ = 'Girish'
import os,time
folder ="."
before = os.listdir(folder)
while 1:
    time.sleep(2)
    after = os.listdir(folder)
    li = [f for f in after if f not in before]
    li2 = [f for f in before if f not in after]
    for x in li : print("added ",x)
    for y in li2 : print("removed ",y)
    before = after