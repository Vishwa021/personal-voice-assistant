# setting reminders, checking the weather, and reading the news.
from plyer import notification
import time

#how to set reminder 
def reminder():
    time.sleep(1)  # wait 5 seconds
    notification.notify(
        title="Reminder",
        message="Time to drink water! 💧",
        timeout=5  # notification stays for 5 seconds
    )


    

    