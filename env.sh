#!/bin/usr/bash

if [ -d "$1" ]; then
	echo "Already exist"
else
	cd "$1"
	python3 -m venv $1
fi
source $1/bin/activate

