#!/usr/bin/env python3
import sys
from urllib.parse import quote, quote_plus

def main():
    # using
    argv = None
    num_args = None
    unencoded = None

    if not sys.stdin.isatty():
        # data is being piped into the script
        piped = sys.stdin.read()
        argv = piped.split()
        num_args = len(argv)
        if num_args == 0:
            num_args = 1
            unencoded = ""
        if num_args != 0:
            unencoded = argv[0]
        
    else:
        argv = sys.argv
        num_args = len(argv) - 1
        if num_args == 0:
            unencoded = ""
        if num_args != 0:
            unencoded = argv[1]
            
    if num_args != 1:
        # usage
        print("Error: incorrect parameter")
        print("Usage: urlencode \"string_to_encode\"")
    else:
        encoded = quote(unencoded)
        print(encoded)

    return



main()
