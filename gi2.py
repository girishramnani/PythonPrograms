

import celery1

w = celery1.add.delay(1,1000)
import time
print(w.status)
print(w.result)

