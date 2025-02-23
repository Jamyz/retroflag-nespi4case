#!/usr/bin/env python3
from gpiozero import Button, LED
import os
from signal import pause
import time

powerPin = 3
resetPin = 2
ledPin = 14
powerenPin = 4
hold = 1
led = LED(ledPin)
led.on()
power = LED(powerenPin)
power.on()

def when_pressed():
    led.blink(.2, .2)
    time.sleep(2)
    os.system("sudo shutdown -h now")

def when_released():
    led.on()

def reboot():
    #select hard or safe reboot
    os.system("sudo reboot")#comment or uncomment for hard reboot
    #os.system("sudo shutdown -r now")# comment or uncomment for safe reboot

btn = Button(powerPin, hold_time=hold)
rebootBtn = Button(resetPin)
rebootBtn.when_pressed = reboot
btn.when_pressed = when_pressed
btn.when_released = when_released
pause()