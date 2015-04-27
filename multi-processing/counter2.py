import os, time, queue
from multiprocessing import Process, Queue # process-safe shared queue
 # queue is a pipe + locks/semas

 
class Counter(Process):
 	label = ' @'
 	def __init__(self, start, queue): # retain state for use in run
 		self.state = start
		self.post = queue
		Process.__init__(self)


	def run(self): # run in newprocess on start()
		for i in range(3):
			time.sleep(1)
			self.state += 1
			print(self.label ,self.pid, self.state) # self.pid is this child's pid
			self.post.put([self.pid, self.state]) # stdout file is shared by all
			print(self.label, self.pid, '-')