# port_scanner.py

import socket
import os
from datetime import datetime

def scan_ports(target, start_port=1, end_port=1024):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"scan_{target}_{timestamp}.log")

    with open(log_file, "w") as f:
        header = f"Scan Report for {target} | Started at: {timestamp}\n{'-'*60}\n"
        print(header)
        f.write(header)

        try:
            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                result = sock.connect_ex((target, port))
                if result == 0:
                    result_line = f"[OPEN ] Port {port} is open\n"
                else:
                    result_line = f"[CLOSED] Port {port} is closed\n"

                print(result_line, end="")
                f.write(result_line)
                sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
        except socket.gaierror:
            print("[!] Hostname could not be resolved")
        except socket.error:
            print("[!] Could not connect to server")

        footer = f"\nScan finished at: {datetime.now()}\n"
        print(footer)
        f.write(footer)

if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ")
    scan_ports(target_ip)

