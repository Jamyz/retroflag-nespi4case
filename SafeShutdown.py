#!/usr/bin/env python3
import RPi.GPIO as GPIO
import os
import time

powerPin = 3
resetPin = 2
ledPin = 14
powerenPin = 4
hold = 1

# Configuration de la bibliothèque RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(powerenPin, GPIO.OUT)

# Allumer les LEDs initialement
GPIO.output(ledPin, GPIO.HIGH)
GPIO.output(powerenPin, GPIO.HIGH)

def when_pressed(channel):
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.2)
    time.sleep(2)
    os.system("sudo shutdown -h now")

def when_released(channel):
    GPIO.output(ledPin, GPIO.HIGH)

def reboot(channel):
    # Sélectionner redémarrage hard ou safe
    os.system("sudo reboot")  # décommenter pour redémarrage hard
    # os.system("sudo shutdown -r now")  # décommenter pour redémarrage safe

# Définir les événements
GPIO.add_event_detect(powerPin, GPIO.FALLING, callback=when_pressed, bouncetime=200)
GPIO.add_event_detect(resetPin, GPIO.FALLING, callback=reboot, bouncetime=200)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
