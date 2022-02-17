#!/home/pi/oprint/bin/python3

#  Copyright ---->
#  BitsVital LLC. Copyright (c) 2022. All Rights Reserved.
#  Created by BitsVital LLC. Lead Computer Engineer: David Swanson
#  Pi Power Button On Off Script For Octoprint
#  Pi Power Button On Off Script For Octoprint by BitsVital comes
#  with ABSOLUTELY NO WARRANTY! Use at your own peril/risk!
#  https://github.com/bitsvital/octoprint_on_off_button_script
#  This script is licensed under the:
#  Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
#  Full License: http://creativecommons.org/licenses/by-nc-sa/4.0/
#  End of Copyright <-----

#  Instructions -> Please read README.md

import RPi.GPIO as GPIO
import subprocess

# Sets the board numbering type. Board or BCM. In this script I used board.
GPIO.setmode(GPIO.BOARD)

# One of the push button pins must be connected to the Pi's SCL pin for the power on feature to work. 
# In the script it's set to pin 5. It's strongly recommended that you verify that your SCL pin on your Pi is pin 5.
# There is only one SCL pin per Pi. The other pin of the push button must be connected to any open ground pin. 
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
