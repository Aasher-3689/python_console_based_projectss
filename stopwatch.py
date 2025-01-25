# Stop watch

from time import sleep

#------------------

num = 0
seconds = 0
minutes = 0
hours = 0

while True:
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    num += 1
    seconds = int(num % 60)
    minutes = int((num / 60) % 60)
    hours = int(num / 3600)
    sleep(1)
