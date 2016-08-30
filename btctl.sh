#!/usr/bin/expect -f

set prompt "#"

spawn sudo bluetoothctl -a
expect -re $prompt
send "power on\r"
sleep 1
expect -re $prompt
send "discoverable on\r"
sleep 1
expect -re $prompt
send "pairable on\r"
sleep 1
expect -re $prompt
send "agent NoInputNoOutput\r"
sleep 1
expect -re $prompt
send "default-agent\r"
sleep 10
send "quit\r"
expect eof

