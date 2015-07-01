__author__ = 'Girish'
import configparser as cp
print(dir(cp.cp))
conf = cp.ConfigParser()
conf['NAME'] ={'name':"girish",'version':1}
with open("file.ini") as confg:
    conf.write(confg)

