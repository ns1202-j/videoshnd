import threading
import requests
import urllib.request
import os
import subprocess
from subprocess import Popen
import time
from omxplayer.player import OMXPlayer

def screen():
	global screen_status
	url= 'http://143.198.132.112/smarthh/pantalla.php'
	status_code = 200
	try:
		status_code = requests.get(url,timeout = 10)
		print(status_code)

	except requests.exceptions.ConnectTimeout:
		status_code = 3
	except requests.exceptions.ConnectionError:
		status_code = 3
	if status_code == 200 or "[200]":
		query = {'lat':'45','lon':'180'}
		r = requests.post('http://143.198.132.112/smarthh/pantalla.php')
		screen_status = r.text
#		print(r.text)
		print('request realizado')
	else:print('no hubo request')
                
global screen_status
screen_status = ''
flag = 1
video = ("/home/pi/Downloads/hnd/camalion.mp4")
video2 = ("/home/pi/Downloads/AnimatedSF.mp4")
a = 'no video'

while True:
    screen()
    if((screen_status == '2') and (a != 'omx1')):
        omx1 = Popen(['omxplayer','-b', video])
        a = 'omx1'
    elif((screen_status == '1') and (a != 'omx2')):
        omx1.quit()
        omx2 = Popen(['omxplayer','-b', video2])
        a = 'omx2'
    elif(screen_status == '3'):
        os.system('sudo killall omxplayer.bin')
        a = 'no video'
    else:
        pass
        
