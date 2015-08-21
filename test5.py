import requests
count=0
from multiprocessing import Pool
from random import randint
import random
import string
from concurrent.futures import ThreadPoolExecutor

# def random_words():
#     return "".join([random.choice(string.ascii_letters) for i in range(randint(5,10))])

import os
from threading import Thread
def work():
    def random_words():
        return "".join([random.choice(string.ascii_letters) for i in range(randint(5,10))])
    count = 0 
    while True:
        print("\r Process {}: {} thread ".format(os.getpid(),count),end="")
        count+=1
        response = requests.post("http://www.csinu.890m.com/register.php",
                      data={'name':'test{}'.format(count),'email':'{}@gmail.com'.format(random_words())})
        print("\r Process {}: {}  code: {}".format(os.getpid(),count,response.status_code),end="")

        

with ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(work)
    print(future.result())


    


