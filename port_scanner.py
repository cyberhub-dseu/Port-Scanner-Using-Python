import socket
from datetime import datetime
import threading
import pyfiglet

# Display banner
banner = pyfiglet.figlet_format("Cyber Hub")
underline = '-' * len(banner.splitlines()[0])
print(banner)
print(underline)

# Define the target
target = input("Enter the target IP address or domain: ")

# Translate hostname to IPv4
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Display information
print(f"\nScanning target: {target_ip}")
print(f"Scanning started at: {str(datetime.now())}\n")

# Function to scan a specific port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Lower timeout for faster scanning
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        s.close()

# Create threads for each port
threads = []

# Scan ports between 1 and 1024
for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"\nScanning finished at: {str(datetime.now())}")
