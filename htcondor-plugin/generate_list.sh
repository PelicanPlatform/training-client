#!/bin/bash

grep "USW00014837" -A 9 ghcnd-stations.txt | cut -d " " -f 1 > station_list.txt

