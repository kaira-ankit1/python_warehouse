import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please drink water NOW!!**",
            message = "So how much fluid does the average, healthy adult living in a temperate climate need?.",
            app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(3600)