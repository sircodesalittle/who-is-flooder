# who-is-flooder
A small application that floods an IP network with BACnet "who-Is" messages. Useful for stress testing BACnet controllers.

I developed this application to stress test BACnet controllers. The idea is to flood the network with who-Is messages that the
controller would be forced to process and respond to.

## Getting Started
Initialize your virtual environment (with tkinter) & install dependencies
```
c:\blah> virtualenv venv --system-site-packages
New python executable in C:\blah\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
c:\blah> venv\Scripts\activate
(venv) c:\blah> pip install -r requirements.txt
```

Run the program
```
(venv) c:\blah> python main.py
```