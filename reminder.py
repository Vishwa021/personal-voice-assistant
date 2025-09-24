# setting reminders, checking the weather, and reading the news.
from plyer import notification
import time

#how to set reminder 
def reminder(rem, t):
    time.sleep(t)  # wait 5 seconds
    notification.notify(
        title="Reminder",
        message= rem,
        timeout= 5 # notification stays for 5 seconds
    )


    

    