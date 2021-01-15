#!/bin/bash

workdir=/root/Shared_Photo_Albums
. venv/bin/activate

daemon_start(){
	cd $workdir
	nohup python3 run.py&
	echo"Serverstarted."
}

daemon_stop(){
	pid=`ps -ef | grep 'python3 run.py' | awk 'BEGIN{ ORS="," }{ print $2 }'`
	arr=(`echo ${pid} | tr ',' ' '`)
	echo ${arr[0]}
	kill -9 ${arr[0]}
	sleep 2
	echo "Serverkilled."
}

case "$1" in
	--start)
		daemon_start
		;;
	--stop)
		daemon_stop
		;;
	--restart)
		daemon_stop
		daemon_start
		;;
	*)
		echo"Usage: ./run.sh {start|stop|restart}"
		exit 1
esac
exit 0
