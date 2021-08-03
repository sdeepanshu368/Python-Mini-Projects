import time
from plyer import notification


if __name__ == '__main__':
	while True:
		notification.notify(
			title="It's Time to Drink Water!!",
			message="Health experts commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon a day. This is called the 8×8 rule and is very easy to remember.",
			app_icon=r"C:\Users\Intel\PycharmProjects\RP\files\glass.ico",
			timeout=5  # seconds
		)
		time.sleep(60)  # seconds
