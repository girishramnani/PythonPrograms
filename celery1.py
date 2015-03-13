from celery import Celery

celery = Celery('tut1',backend='redis://',broker='redis://')

@celery.task
def add(a,b):
	
	print(a+b)