import queue
from multiprocessing import Process,Queue 


class Counte(Process):
	proc = "@"
	def __init__(self,val,post):
		Process.__init__(self)
		self.val = val
		self.post = post
		
	def run(self):
		for i in range(3):
			print(self.proc +str(self.pid))
			self.post.put([self.pid,i+self.val])
		


if __name__ =="__main__":
	q = Queue()
	pros1 = Counte(1,q)
	pros2 = Counte(10,q)
	pros3 = Counte(100,q)
		
	counter =9
	pros1.start()
	pros2.start()
	pros3.start()
	waitcounter =0
	while counter:
		try:
			print(q.get(block=False))
		except queue.Empty:
			waitcounter+=1
		else:
			counter-=1
	pros1.join()
	pros2.join()
	pros3.join()
	print(waitcounter)
