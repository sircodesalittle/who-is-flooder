#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  metered_bcast.py
#
#  Copyright 2017  <phredmund@raspberrypi>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST
from time import sleep
from tkinter import *
from binascii import unhexlify


LGR_IP = "192.168.1.70"
WC_IP = "192.168.1.24"
PC_IP = "192.168.1.2"
BCAST_IP = "192.168.1.255"
Z = 0

# Payload for UDP packet (A Broadcast who-Is with specified full instance number range)
# This packet is 480 bits long
data = '81 0b 00 12 01 20 ff ff 00 ff 10 08 09 00 1b 3f ff ff'
# take data string and return list datatype. Use space as separator.
# should return ['81', '0b', '00'...]
data_list = data.split(' ')
# Join elements of the list with an empty space
who_is_data = ''.join(data_list)
#
# This worked in Python 2, but not in Python 3:
# who_is_data = ''.join(data_list).decode('hex')
#
MESSAGE = unhexlify(who_is_data)

root = Tk()


def do_it(event=None):
    x = 0
    reps = 0
    while x <= PPS_TARGET.get():
        # print "Sending packet #", str(x+1)
        sendpacket()
        # print("Sleeping", str(1.0000000/PPS_TARGET.get()))
        sleep(1.0000 / PPS_TARGET.get())
        x = x + 1
        if x == PPS_TARGET.get():
            print("Round #", str(reps + 1))
            reps = reps + 1
            x = 0
        if reps == int(SEC_LENGTH.get()):
            print("Done!")
            break

    return 0


def sendpacket():
    mysock.sendto(MESSAGE, (TARGET_IP.get(), UDP_PORT.get()))


# print("Sending a packet!")

PPS_INPUT = StringVar()
PPS_INPUT.set("500")
TUNING_FACTOR = StringVar()
TUNING_FACTOR.set("1000")
PPS_TARGET = IntVar()
PPS_TARGET.set(int(PPS_INPUT.get()) + int(TUNING_FACTOR.get()))
SEC_LENGTH = StringVar()
SEC_LENGTH.set("5")
TARGET_IP = StringVar()
TARGET_IP.set("192.168.1.255")
UDP_PORT = IntVar()
UDP_PORT.set(47808)
mysock = socket(AF_INET, SOCK_DGRAM)
mysock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

pps_label = Label(root, text='How many packets/sec?').grid(row=1, column=1, sticky=E, pady=10)
gimmie_pps = Entry(root, textvariable=PPS_INPUT)
gimmie_pps.grid(row=1, column=3, sticky=W)
duration_label = Label(root, text='How long should we test?').grid(row=2, column=1, sticky=E, pady=10)
gimmie_duration = Entry(root, textvariable=SEC_LENGTH)
gimmie_duration.grid(row=2, column=3, sticky=W)
duration_units = Label(root, text='<--in seconds').grid(row=2, column=4, sticky=W, padx=5)
target_label = Label(root, text='Who is your target?').grid(row=3, column=1, sticky=E, pady=10)
gimmie_target = Entry(root, textvariable=TARGET_IP)
gimmie_target.grid(row=3, column=3, sticky=W)
target_units = Label(root, text='<--IP Address').grid(row=3, column=4, sticky=W, padx=5)
go_label = Label(root, text='Click to assault-->').grid(row=4, column=1, padx=5)
gobutton = Button(root, text="Go!")
gobutton.bind("<Button-1>", do_it)
gobutton.grid(row=4, column=2, pady=25)
tuning_label = Label(root, text='Speed tuning factor:\nPackets/sec fudge factor').grid(row=4, column=3, sticky=E)
gimmie_tuning = Entry(root, textvariable=TUNING_FACTOR)
gimmie_tuning.grid(row=4, column=4, sticky=E)
root.mainloop()