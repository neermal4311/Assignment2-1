#!/usr/bin/env python3
#Nirmal Gautam-ngautam11-ops445-168555225
# Nirmal Gautam - ngautam11 - OPS445 - Assignment 2A
# This script visualizes memory usage of a system and its processes with bar charts.
# It is my original work of Nirmal Gautam and was developed as part of the OPS445 course.
# The script allows for viewing system memory and the memory usage of specified programs. and this is Created on :8th  December 2024

import argparse
import os
import sys

def parse_command_args() -> object:
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in Human readable format.")
    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    return parser.parse_args()

#Here this creates argparse function and for to make human readable i used -h and -r for running only

def percent_to_graph(percent: float, length: int=20) -> str:
    num_hashes = int(round(percent * length))
    return f"[{'#' * num_hashes}{' ' * (length - num_hashes)}]"  
#bar graph string
#Here this is for percentage to graph function

def get_sys_mem() -> int:
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemTotal' in line:
                return int(line.split()[1])

def get_avail_mem() -> int:
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemAvailable' in line:
                return int(line.split()[1])
#Assignment1-milestone1 done
