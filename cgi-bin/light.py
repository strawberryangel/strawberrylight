#! /usr/bin/python
import urlparse
import os
import RPi.GPIO as GPIO


# Sophie's program to get the information from the web browser and turn the light on or off.

if "QUERY_STRING" not in os.environ:
    print 'Content-type: application/json\n\n'
    print '{"success":false,"message":"No QUERY_STRING"}'
    exit()

if os.environ["QUERY_STRING"] == "":
    print 'Content-type: application/json\n\n'
    print '{"success":false,"message":"QUERY_STRING has nothing in it."}'
    exit()

query_string = urlparse.parse_qs(os.environ["QUERY_STRING"])

if "light" not in query_string:
    print 'Content-type: application/json\n\n'
    print '{"success":false,"message":"No light in QUERY_STRING."}'
    exit()

light = query_string["light"].pop(0)

if light not in ["0", "1"]:
    print 'Content-type: application/json\n\n'
    print '{"success":false,"message":"Light can only be 0 or 1."}'
    exit()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

if light == "0":
    GPIO.output(11, GPIO.LOW)
else:
    GPIO.output(11, GPIO.HIGH)

print 'Content-type: application/json\n\n'
print '{"success":true,"light":' + light + '}'
