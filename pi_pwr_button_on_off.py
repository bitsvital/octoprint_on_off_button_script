#!/home/pi/oprint/bin/python

#  Copyright ---->
#  BitsVital LLC. Copyright (c) 2022. All Rights Reserved.
#  Created by BitsVital LLC. Lead Computer Engineer: David Swanson
#  Pi Power Button On Off Script
#  Pi Power Button On Off Script by BitsVital comes with ABSOLUTELY NO WARRANTY!
#  Use at your own peril/risk!
#  Original program located at: # ToDo Enter GitHub Address
#  This script is licensed under the:
#  Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
#  Full License: http://creativecommons.org/licenses/by-nc-sa/4.0/
#  End of Copyright <-----

#  Instructions / Description / Remarks ---->
#  Pin 5 GPIO3 (SCL)
#  Pin 6 Ground
#  Connect a 2 pin push button to pins 5 and 6 of your Raspberry Pi
#  The script will use the RPI.GPIO library method 'wait_for_edge'
#  Edge detection will detect a change from Low/High or High/Low
#  Wait For Edge will block execution of this script until an interrupt
#  is detected. Once 'wait_for_edge' detects a 'falling' edge the script
#  will be triggered and the Pi will be shutdown.
#  End of Instructions / Description / Remakrs <----

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
