#!/bin/bash
#show.sh

echo -n "enter name username and press enter:"
read person

echo "${person:-$USER} processes:"
ps -fe | grep "^{person:-$USER}" | more


