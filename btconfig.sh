#!/bin/bash

# Appends -C to the end of line with /usr/lib/bluetooth/bluetoothd
oldStr="bluetooth\/bluetoothd"
newStr="bluetooth\/bluetoothd -C"

sed -i -e "s/${oldStr}/${newStr}/" /lib/systemd/system/bluetooth.service

# Make rfcomm-server.py run on boot
crontab -l > mycron
echo "@reboot /usr/bin/python /home/pi/rfcomm-server.py" >> mycron
crontab mycron
rm mycron


