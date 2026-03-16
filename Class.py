import socket
import threading
from queue import Queue

target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

queue = Queue()
open_ports = []

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        s.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        port_scan(port)

for port in range(start_port, end_port + 1):
    queue.put(port)

threads = []

for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nScan complete.")
print("Open ports:", open_ports)