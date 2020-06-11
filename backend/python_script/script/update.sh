#!/bin/bash

cd ..

source ../../../dpenv/bin/activate

kill -9 `ps -ef | grep python | grep Trading.py| grep checkEvent | awk '{print $2}'`
while true
do
    event_cnt=$(ps -ef | grep python | grep Trading.py | grep checkEvent|wc -l)
	if [ $event_cnt -eq 0 ]
	then
		python Trading.py checkEvent &
	fi
    
    sleep 10

done