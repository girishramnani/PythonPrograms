from celery1 import add
rep =add.delay(4,4)
print(rep.get())