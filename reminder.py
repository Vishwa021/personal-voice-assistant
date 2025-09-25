import threading, time
from plyer import notification

def set_reminder(message, delay):
        def notify():
            time.sleep(delay)
            notification.notify(
                title="Reminder",
                message=message,
                timeout=5
            )
        threading.Thread(target=notify, daemon=True).start()

    

    