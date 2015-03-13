import string
import time
import socket
import threading
from multiprocessing import Process as worker
from queue import Queue
'''
enumerate a site's domain name like this:
1-9 a-z + .google.com
1.google.com
2.google.com
.
.
1a.google.com
.
.
zz.google.com

'''

start = time.time()
def create_host(char):
    '''
    if char is '1-9a-z'
    create char like'1,2,3,...,zz'
    '''
    for i in char:
        yield i
    for i in create_host(char):
        if len(i)>1:
            return False
        for c in char:
            yield c + i


char = string.digits + string.ascii_lowercase
site = '.google.com'


def getaddr():
    while True:
        url = q.get()
        try:
            res = socket.getaddrinfo(url,80)
            print(url + ":" + res[0][4][0])
        except:
            pass
        q.task_done()

NUM=1000  #thread's num
q=Queue()

for host in create_host(char):
    q.put(host+site)
for i in range(NUM):
    w=worker(target=getaddr)
    w.start()

end = time.time()

print(end-start)
