from time import sleep
from plyer import notification

# You can change this time variables value to change the difference between time

time = 30

def notify():
    while True:
        notification.notify(
            title="Dehydrate yourself, Please Drink Water",
            message="Water is the best dehydrator in the world",
            app_icon="assets/water.ico",
            timeout=15
        )
        sleep(60*time)
