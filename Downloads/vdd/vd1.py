import threading
import requests
import urllib.request
import os
from subprocess import Popen
import time

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
		#print(r.text)
		print('request realizado')
	else:print('no hubo request')
                
global screen_status
screen_status = ''
flag = 1
video = ("/home/pi/Downloads/hnd/camalion.mp4")
while True:
    if(flag == 1):
        omx = Popen(['omxplayer','-b', video])
        flag = 0
       
    elif(flag == 2):
        screen()
        print(screen_status)
       
    else:
        time.sleep(10)
        os.system('sudo killall omxplayer.bin')
        print ('programa terminado')
        flag = 2
