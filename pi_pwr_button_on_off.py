#!/home/pi/oprint/bin/``python
# ToDo Test SheBang statement with and without Venv environment

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

# Sets the board numbering type. Board or BCM. In this script I used board.
GPIO.setmode(GPIO.Board)

# One of the push button pins must be connected to the Pi's SCL pin for the power on feature to work. 
# In the script it's set to pin 5. As of 2022-02-15 all current Pi's SCL is pin 5. 
# However, it's strongly recommended that you verify that your SCL pin on your Pi is pin 5.
# There is only one SCL pin per Pi. The other pin of the push button must be connected
# to any open ground pin. 
# Pin 5 is set to an input pin.
# Instead of writing a CPU intesive while loop I use the RPi.GPIO 'wait_for_edge' feature.
# 'wait_for_edge' will detect a rise or fall on the pin and then run the the script saving valuable
# CPU power. I set the pin to up. It makes no difference if you set the pin to up or down. 
# The next part must be the opposite transition.
# Additional infomation can be found at: https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The above code line I set the pin to an 'UP' state. In this line of code I'm telling 'wait_for_edge'
# to watch for a falling state. When you press the button a fall is detected and the the subprocess 
# (line of code below) is initiated. 
GPIO.wait_for_edge(5, GPIO.FALLING)

# Once 'wait_for_edge' detects an interuption the Raspberry Pi will run the following process.
# The following subprocess is the same as if you typed 'sudo shutdown -h now' at the command line to
# halt the Raspberry Pi.
subprocess.call(['shutdown', '-h', 'now'], shell=False)
