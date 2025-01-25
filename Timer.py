# countdown timer

from time import sleep

#-------------------

while True:
    my_time = input("Enter the time in seconds: ")
    try:
        my_time = int(my_time)
        if my_time > 86400:
            print("More than 24 hours is not valid")
        else:
            break
    
    except ValueError or ZeroDivisionError:
        print("Invalid choice! please write in integers")

#---------------------

for time in range(my_time, 0, -1):
    seconds = int(time % 60)
    minutes = int((time/60) % 60)
    hours = int(time/3600)

    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    sleep(1)

print("TIME'S UP!")
