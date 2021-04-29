import RPi.GPIO as GPIO  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import time


def main():
    # setting up how we talk with the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # set channel 18 to be used to send signals
    GPIO.setup(18, GPIO.OUT)
    # send a signal to channel 18 - HIGH means "on"
    GPIO.output(18, GPIO.HIGH)
    print("Channel 18 is now 'on'")
    # pause for 5 seconds
    time.sleep(5)
    # send a signal to channel 18 - LOW means "off"
    GPIO.output(18, GPIO.LOW)
    print("Channel 18 is now 'off'")
    # tell the micro computer we are done with all channels
    GPIO.cleanup()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
