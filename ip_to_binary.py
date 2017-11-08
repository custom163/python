#!/usr/bin/Python

ip = raw_input("Please enter the IP address: \n")

list = ip.split(".")

for i in list:
    new = bin(int(i))
    new = new.split("b")[1]
    while len(new) < 8:
        new = "0" + new
    print new
