#!/usr/bin/env python3
import re
import os
import time
import pathlib
import argparse
import subprocess
import urllib.request
import requests
def fetch_fib_number(index):
    resp = urllib.request.urlopen(f"http://www.protocol5.com/Fibonacci/{index}.htm")
    html = [h.strip().decode('utf-8') for h in resp.readlines()]
    represents = []
    for line in html:
        match = re.search(r"<li><h4>.+?</h4><div>(.+?)</div></li>", line)
        if match:
            represents.append(match.group(1))

    return {
        "base2": represents[0],
        "base3": represents[1],
        "base5": represents[2],
        "base6": represents[3],
        "base8": represents[4],
        "base10": represents[5],
        "radix16": represents[6],
        "radix36": represents[7],
        "radix63404": represents[8]
    }

def main(index, base, result):
    start_time = time.time()
    expect = fetch_fib_number(args.index)[base]

    if result == expect:
        print("Pass")
        exit(0)
    else:
        print("No pass")
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, dest="port",help="localhost port")
    parser.add_argument("-i", type=str, dest="index",help="Fibonacci number index")
    parser.add_argument("-b", action='store', dest="base", help="Fibonacci number base (default: base10)")
    args = parser.parse_args()

    FIB_NUMBER_BASE = args.base
    FIB_INDEX = int(args.index)
    if FIB_INDEX < 0:
        print("Fibonacci index is less than 0")
        exit(1)

    link = "http://localhost:"+args.port+"/fib/"+args.index
    RESULT = requests.get(link).text

    if not FIB_NUMBER_BASE:
        FIB_NUMBER_BASE = "base10"

    main(FIB_INDEX, FIB_NUMBER_BASE,RESULT)