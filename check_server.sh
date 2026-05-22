#!/bin/bash
function check_server() {
	server=$1
	ping -c 1 $server > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		echo " $server is online"
	else
		echo " $server is offline"
	fi
}

for server in $(cat servers.txt); do
	check_server $server
done
