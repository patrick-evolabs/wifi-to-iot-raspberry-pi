# wifi-to-iot-raspberry-pi
Raspberry Pi-side component to receive Wi-Fi password via Bluetooth

Raspberry Pi Setup
You need a SD card, power supply, and Ethernet cable.
Follow the instructions here to write the (minimal) images for Raspbian OS to the Pi.
Insert the SD card to the Pi. Connect your Pi to the Ethernet and power it up.
Follow the instructions here to find the IP address of the Pi. 
SSH to the Raspberry Pi.
Rename Your Raspberry Pi
Upload rename.sh to home directory. Make the script executable: chmod +x rename.sh 
Run sudo ./rename.sh newName
sudo reboot for changes to take effect. (You can reboot after you finish the next section)
Bluetooth Configurations on Raspberry Pi
Download pip	 			sudo apt-get install python-pip
Download the Bluetooth module 	sudo apt-get install python-bluez
Download Expect			sudo apt-get install expect
Download the WiFi module 		sudo pip install wifi
Upload rfcomm-server.py to the Pi’s home directory.
Upload btconfig.sh to the Pi. Make the script executable: chmod +x btconfig.sh
Run sudo ./btconfig.sh
sudo reboot
Pair Your Device with Raspberry Pi
sudo bluetoothctl
Inside the bluetoothctl interface, type in commands:
agent on 		 “Agent registered”
pairable on		 “Changing pairable on succeeded”
discoverable on	 “Changing discoverable on succeeded”
scan on		 Will return a list of devices found.
Once the device you want to pair your Pi with has been discovered (make sure to turn on Bluetooth on your device), enter the command pair XX:XX:XX:XX:XX:XX
The bluetoothctl agent should ask you to confirm the passkey (yes/no). Input yes.
You should also receive a pairing request on your device. Confirm the request.
The Pi will print out “Pairing Successful” if the devices have been paired.
Trust your device by entering trust XX:XX:XX:XX:XX:XX
Enter quit to exit the bluetoothctl agent.
Unplug Ethernet cable from the Pi.
Connect Raspberry Pi to WiFi Networks
Once you succeed in pairing your Pi to your device, you can open the app.
Scan for your Raspberry Pi and connect. Note that if you just rebooted your Pi, it will take a while for the server to restart and be able to listen for connections.
If you have failed to connect multiple times, try to reboot your Pi.
Select the WiFi you wish to connect and enter the password.
Note that the server checks for general network connections, so be sure to unplug the Ethernet cable from your Pi. This way it could correctly report WiFi status! 
Disconnect when you’re done.
