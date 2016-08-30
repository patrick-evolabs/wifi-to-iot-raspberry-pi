# Set this script to run at boot
# sudo crontab -e
# Add the line below to the bottom of the file
# @reboot /usr/bin/python /path/to/your/script.py

import os
import json
import time
import subprocess
from bluetooth import *
from wifi import Cell, Scheme


# time for the pi to start up
time.sleep(15)

def main ():

    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "SampleServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
#                      protocols = [ OBEX_UUID ] 
                        )

    # Make the Pi discoverable
    subprocess.call(["hciconfig", "hci0", "leadv", "0"]);
    subprocess.call(["hciconfig", "hci0", "leadv", "3"]);
                   
    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)


    try:
        while (True):
	    input  = client_sock.recv(1024)

	    # ready to scan for available wifi
	    if (input == "READY"):
		ssids = []
    		for cell in Cell.all ('wlan0'):
        	    if (cell.signal > (-50)):
            		ssids.append ("<b>" + cell.ssid + "</b><br/> Signal Strength: Strong")
		    elif (cell.signal > (-65)):
			ssids.append ("<b>" + cell.ssid + "</b><br/> Signal Strength: Medium")
 		    elif (cell.signal > (-75)):
			ssids.append ("<b>" + cell.ssid + "</b><br/> Signal Strength:  Weak ")

    		output = {}	
    		output["wifi"] = ','.join (ssids)
    		j_out  = json.dumps (output)
    		client_sock.send (j_out + "\n")
	    
	    else:
         	j_in   = json.loads (input.rstrip())
   	    	ssid   = j_in["ssid"].rstrip()
	    	pwd    = j_in["password"].rstrip()
		            
		# edit wifi config file	    
	    	writeFile (ssid, pwd)

		# check if password is too short
		if 'Failed to bring up wlan0' in open ('wlan0.log').read():
                    output = {}
                    output["danger"] = "WiFi password entered incorrect."
	            j_out  = json.dumps (output)
                    client_sock.send (j_out + "\n")

                else:
                    output = {}
                    output["info"] = "Connecting to WiFi " + ssid + " ..."
                
		    j_out  = json.dumps (output)
                    client_sock.send (j_out + "\n")
 
                    iterator = 0
		    output = {}
		
		    while True :

			iterator += 1
		    
		        time.sleep (3)  	               
	
			# this check for "any" network connection
			# make sure the pi is not connected to ethernet
   			ping_ret = subprocess.call(['ping -c 2 -w 1 -q 192.168.1.1 |grep "1 received" > /dev/null 2> /dev/null'], shell=True)

			if ping_ret:
			    if (iterator == 7):
				output["danger"] = "Please make sure the password entered is correct and WiFi signal is stable."
	                        break
			else:
		             output["success"] = "WiFi connection succeeded!"
			     break
		   
		    j_out = json.dumps (output)
		    client_sock.send (j_out + "\n")    
   
    except IOError:
        pass

    print("Disconnected From the Device")

    client_sock.close()
    server_sock.close()


def writeFile (ssid, pwd):

    lines = []

    with open ("/etc/wpa_supplicant/wpa_supplicant.conf") as infile:
	for line in infile:
	    if (line.startswith ("network={")):
		break	
	    lines.append (line)
    with open ("/etc/wpa_supplicant/wpa_supplicant.conf", 'w') as outfile:
	for line in lines:
	    outfile.write(line)
	outfile.write ("network={\n\tssid=\"" + ssid + "\"\n\tpsk=\"" + pwd + "\"\n}")

    os.system ('sudo ifdown wlan0')
    os.system ('sudo ifup wlan0 > wlan0.log')

  
while (True):
    main ()

