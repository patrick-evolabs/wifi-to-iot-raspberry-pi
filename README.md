# WiFi-to-IoT Raspberry Pi

The server component for Raspberry Pi to receive Wi-Fi password via Bluetooth

## Getting Started

To set up the server on your Raspberry Pi, you can simply write the image file provided [here](https://drive.google.com/file/d/0B4uA-g8pjDs4QV9ZTmpmdG9xT0U/view) to the Pi. You will *not* have to follow the set up instructions below. Skip to **How to Use** section for instructions of the app. Your Pi will be ready to receive incoming connection.

Otherwise, if you do *not* want to download the already-set image file, follow the steps below to set up your Pi from scratch.

### Set Up Your Raspberry Pi

* You need a FAT32-formatted 8GB SD card, power supply, Ethernet cable, and a LAN.
* Follow the instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to write the  Raspbian Jessie Lite image to the Pi.
* Insert the SD card to the Pi. Connect your Pi to the router with the Ethernet cable. Connect to your power supply.
* Follow the instructions [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md) to find the IP address of the Pi. Nmap works well for me.
* SSH into the Raspberry Pi. Note that the default username is pi, and the password is raspberry. The address should be pi@piAddressOnLan.

### Bluetooth Configurations on Raspberry Pi

Download pip

```
sudo apt-get install python-pip
```

Download the Bluetooth Module

```
sudo apt-get install python-bluez
```

Download the WiFi Module

```
sudo pip install wifi
```

Download Expect

```
sudo apt-get update
```

```
sudo apt-get install expect
```

### Upload and Run the Scripts

Upload these scripts to the home directory **/home/pi** of your Raspberry Pi. You can accomplish this by using FTP with the same credentials as for SSH: 
* [btctl.sh](https://github.com/patrick-evolabs/wifi-to-iot-raspberry-pi/blob/master/btctl.sh): This script automates **bluetoothctl** and allows the Pi to accept Bluetooth pairing request without keycode.
* [btconfig.sh](https://github.com/patrick-evolabs/wifi-to-iot-raspberry-pi/blob/master/btconfig.sh): The script configures Bluetooth on the Pi, and makes the python script run on boot.
* [rename.sh](https://github.com/patrick-evolabs/wifi-to-iot-raspberry-pi/blob/master/rename.sh): The one-time-only script allows the user to change the Pi's hostname.
* [rfcomm-server.py](https://github.com/patrick-evolabs/wifi-to-iot-raspberry-pi/blob/master/rfcomm-server.py): The Bluetooth server that enables the Pi to wait for incoming serial connection.

Inside the Pi's home directory, make **btconfig.sh** executable and run it:

```
chmod +x btconfig.sh
```

```
sudo ./btconfig.sh
```

Reboot the Pi

```
sudo reboot
```

### Rename Raspberry Pi

If you wish to rename your Pi, make the script executable in the home directory:

```
chmod +x rename.sh
```

Run the command with desired new name as the argument:

```
sudo ./rename.sh newName
```

Reboot the Pi for changes to take effect:

```
sudo reboot
```

## How to Use
### Mobile App
* Unplug the Ethernet cable from the Pi.
* Scan and pair with Raspberry Pi using your device's built-in Bluetooth. This app only lists paired devices.
* Open the [WiFi-to-IOT](https://play.google.com/store/apps/details?id=com.bluepi) app and the Pi should be listed when you click **Select**.
* Select your Pi and connect.
* Once connected, the WiFi section will appear. Choose a WiFi network and enter the password.
* The attempt to connect could take up to 20 seconds.
* Disconnect when you finish.

### Troubleshoot
* If you just rebooted your Pi, it would take up to 15 seconds for the server to restart and be able to listen for connections.
* If you still fail to connect to the Pi multiple times, reboot it.
* The server checks for general network connections. Unplug the Ethernet cable from your Pi so it could correctly report WiFi status. 
* If WiFi connection failed, make sure the network signal is stable, and the password entered is correct.
* Make sure no other devices are connected to the Pi when you attempt to connect.

## Authors

Kelly Cho

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/patrick-evolabs/wifi-to-iot-raspberry-pi/blob/master/LICENSE) file for details.

## Acknowledgments

* [Bluetooth Serial Plugin](https://github.com/don/BluetoothSerial)
* [Raspberry Bluetooth Demo](https://github.com/EnableTech/raspberry-bluetooth-demo)
