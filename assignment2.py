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
def pids_of_prog(app_name: str) -> list:
    pids = os.popen(f'pidof {app_name}').read().strip().split()
    return pids if pids else []

def rss_mem_of_pid(proc_id: str) -> int:
    rss_mem = 0
    try:
        with open(f'/proc/{proc_id}/smaps', 'r') as f:
            for line in f:
                if 'Rss:' in line:
                    rss_mem += int(line.split()[1])
    except FileNotFoundError:
        pass
    return rss_mem

#Assignment2-milestone2 done





def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']   #here iB means 1024
    suffix_index = 0
    while kibibytes >= 1024 and suffix_index < len(suffixes) - 1:
        kibibytes /= 1024.0
        suffix_index += 1
    return f"{kibibytes:.{decimal_places}f} {suffixes[suffix_index]}"

if __name__ == "__main__":
    args = parse_command_args()

    if not args.program:
        total_mem = get_sys_mem()
        avail_mem = get_avail_mem()
        used_mem = total_mem - avail_mem
        used_percent = used_mem / total_mem
        graph = percent_to_graph(used_percent, args.length)
        if args.human_readable:
            total_mem = bytes_to_human_r(total_mem)
            used_mem = bytes_to_human_r(used_mem)
        print(f"Memory {graph} {int(used_percent * 100)}% {used_mem}/{total_mem}")
    else:
        pids = pids_of_prog(args.program)
        if not pids:
            print(f"{args.program} not found.")
            sys.exit()
        for pid in pids:
            rss = rss_mem_of_pid(pid)
            rss_percent = rss / get_sys_mem()
            graph = percent_to_graph(rss_percent, args.length)
            if args.human_readable:
                rss = bytes_to_human_r(rss)
            print(f"{pid:6} {graph} {rss}")



 # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.


#Thank you for looking at my work!
# I sincerely hope you find my script useful since it offers a straightforward and graphical method of keeping an eye on memory utilization on a Linux machine.
# Any and all comments are valued. As part of the homework for the OPS445 course, I made this original piece of work.

