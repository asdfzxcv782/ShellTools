#!/bin/sh

function getMemoryStatus(){
	MemoryTotal="$(free -m | grep Mem | awk '{print $2}')";
	MemoryUsed="$(free -m | grep Mem | awk '{print $3}')";
	MemoryFree="$(free -m | grep Mem | awk '{print $4}')"

	python -u ../py/calculateMemory.py $MemoryTotal \
        $MemoryUsed $MemoryFree;
	#get memory usage
	#memory="$(free -m | grep Mem | awk '{print ($3/$2)*100}')";
	#set alarm usage %
	#alarm=20;
	#p=0;
	#wk '{print $2}')num=$(echo "scale=4;$memory-$alarm"|bc|printf "%.*f\n" 0 $num)
	#num=$(echo "scale=4;$memory-$alarm"|bc)
	#num=$(printf "%.*f\n" $0 $num)
	#echo $num
	#if [ $num -gt 0 ];
	#then
       # 	echo "Alarm!";
#	else
       # 	echo "Safe!";
#	fi
}
getMemoryStatus;
