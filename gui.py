import who_is
from tkinter import *
from time import sleep
from tkinter import *
from threading import Thread


class MainFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Who-Is Flooder')
        content_frame = Frame(self.parent)
        content_frame.pack(fill=BOTH)
        self.pack()
        self.PPS_INPUT = StringVar()
        self.PPS_INPUT.set("500")
        self.TUNING_FACTOR = StringVar()
        self.TUNING_FACTOR.set("1000")
        self.PPS_TARGET = IntVar()
        self.PPS_TARGET.set(int(self.PPS_INPUT.get()) + int(self.TUNING_FACTOR.get()))
        self.SEC_LENGTH = StringVar()
        self.SEC_LENGTH.set("5")
        self.TARGET_IP = StringVar()
        self.TARGET_IP.set("192.168.1.255")
        self.UDP_PORT = IntVar()
        self.UDP_PORT.set(47808)
        
        pps_label = Label(content_frame, text='How many packets/sec?').grid(row=1, column=1, sticky=E, pady=10)
        gimmie_pps = Entry(content_frame, textvariable=self.PPS_INPUT)
        gimmie_pps.grid(row=1, column=3, sticky=W)
        duration_label = Label(content_frame, text='How long should we test?').grid(row=2, column=1, sticky=E, pady=10)
        gimmie_duration = Entry(content_frame, textvariable=self.SEC_LENGTH)
        gimmie_duration.grid(row=2, column=3, sticky=W)
        duration_units = Label(content_frame, text='<--in seconds').grid(row=2, column=4, sticky=W, padx=5)
        target_label = Label(content_frame, text='Who is your target?').grid(row=3, column=1, sticky=E, pady=10)
        gimmie_target = Entry(content_frame, textvariable=self.TARGET_IP)
        gimmie_target.grid(row=3, column=3, sticky=W)
        target_units = Label(content_frame, text='<--IP Address').grid(row=3, column=4, sticky=W, padx=5)
        go_label = Label(content_frame, text='Click to assault-->').grid(row=4, column=1, padx=5)
        gobutton = Button(content_frame, text="Go!", command=self.do_assault)
        gobutton.grid(row=4, column=2, pady=25)
        tuning_label = Label(content_frame, text='Speed tuning factor:\nPackets/sec fudge factor').grid(row=4, column=3, sticky=E)
        gimmie_tuning = Entry(content_frame, textvariable=self.TUNING_FACTOR)
        gimmie_tuning.grid(row=4, column=4, sticky=E)

    
    def do_assault(self):
        t = Thread(target=who_is.send_packets_with_delay, args=(self.TARGET_IP.get(), int(self.UDP_PORT.get()), int(self.PPS_TARGET.get()), int(self.SEC_LENGTH.get())))
        t.start()