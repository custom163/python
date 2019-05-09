#!/usr/bin/python

ip = raw_input("Please enter the IP address: \n")

list = ip.split(".")

def convert(ip_list):
    x = []
    for i in list:
        new = bin(int(i))
        new = new.split("b")[1]
        while len(new) < 8:
            new = "0" + new
        x.append(new)
    return x

print( ".".join(convert(list)) )



