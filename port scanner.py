import socket



print("###################################################")
print("############## nati port scanner ##################")
print("###################################################")
print("                                     ====== only for linux (OS) don't work for windows ======                              ")


def port_scan(host):
    open_ports = []
    for port in range(1, 1001):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.gaierror:
            print('Hostname could not be resolved.')
            continue
        except socket.error:
            print("Couldn't connect to server")
            continue
    return open_ports

def main():
    host = input("Enter the host IP address: ")

    open_ports = port_scan(host)

    if open_ports:
        print(f"Open ports on {host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {host}")

if __name__ == "__main__":
    main()
