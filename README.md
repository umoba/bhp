# Black Hat Python (2nd Edition): Chapter 2 - Basic Networking Tools

This repository contains implementations and prototypes based on **Chapter 2** of the 2nd Edition of *Black Hat Python*. The focus is on moving beyond standard tools to build custom Python 3 scripts for network interaction.

## Environment Setup: Virtualization with UTM

To safely test these scripts for this project without risking the host operating system, a virtualized environment is used:

* **Virtualization Software**: **UTM** (optimized for Apple Silicon) is used to host a **Kali Linux** virtual machine.
* **Networking Configuration**: The VM uses a bridged or shared network adapter to communicate with external hardware, such as a **Raspberry Pi**, on the same local network.
* **Connection Requirements**: Testing is conducted on a network without **AP Isolation** to ensure the Kali VM and Raspberry Pi can establish a direct TCP handshake.



## Project Structure

Following the 2nd Edition curriculum, the directory includes the following Python 3 modules:

| File | Description |
| :--- | :--- |
| `backdoorProto.py` | A functional reverse shell prototype for remote command execution. |
| `netcat.py` | A custom Python 3 replacement for the standard Netcat tool. |
| `proxy.py` | A TCP proxy for intercepting and modifying traffic in transit. |
| `simpleTCPClient.py` | A basic client for sending byte-encoded data to a TCP server. |
| `simpleTCPServer.py` | A multi-threaded server capable of handling multiple connections. |
| `simpleUDPClient.py` | A client for the connectionless UDP protocol. |
| `ssh_cmd.py` | Executing commands on a remote SSH server using Paramiko. |
| `ssh_rcmd.py` | Sending commands from an SSH server to a client. |
| `ssh_server.py` | Implementation of an SSH server using the Paramiko library. |

---

## Prototype: Reverse Shell Backdoor

The `backdoorProto.py` script is a practical application of the TCP client concepts covered in the book. It establishes a "reverse" connection from a target device (Raspberry Pi) back to the attacker's machine (Kali VM).

### Setup Instructions

1. **Listener Side (Kali VM)**:
   Open a terminal and start a Netcat listener to wait for the incoming connection:
   ```bash
   nc -lnvp 4444

2. **Target Side (Raspberry Pi)**: 
    While ensuring that server_ip and server_port matches with that of the listener's side, run:
    ```python
    python backdoorProto.py
