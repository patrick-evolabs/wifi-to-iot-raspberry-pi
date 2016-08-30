#!/bin/bash
# Edit the host name of the Raspberry Pi
# Run this script with sudo

echo Run sudo reboot for changes to take effects

newName=$1

# Edit /etc/hosts
sed -i -e "s/raspberrypi/${newName}/" /etc/hosts 

# Edit /etc/hostname
sed -i -e "s/.*/${newName}/" /etc/hostname

/etc/init.d/hostname.sh

