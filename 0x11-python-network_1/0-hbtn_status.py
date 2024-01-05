#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as r:
        re = r.read()
    print("Body response:")
    print("\t- type: {}".format(type(re)))
    print("\t- content: {}".format(re))
    print("\t- utf8 content: {}".format(re.decode('utf-8')))
