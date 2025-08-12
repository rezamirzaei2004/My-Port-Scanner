import socket
import sys

def scan (ip , port):
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip,port))
        if result == 0 :
            return True
        else:
            return False
        
    except Exception as a:
        print(f"error : {a}")
        return False
    
def main ():
    if len (sys.argv)!=4:
        print("input: ip - start port - end port")
        sys.exit()

    ip=sys.argv[1]
    start_port=int(sys.argv[2])
    end_port=int(sys.argv[3])

    print(f"scaning {start_port} to {end_port} for {ip} ")

    open_ports = []
    for port in range ( start_port ,end_port +1):
        if scan(ip,port):
            open_ports.append(port)
            print(F"{port} is open")
        else:
            print(f"{port} is close",end="\r")
    print("scan finished")
    if open_ports :
        print(f" open ports : {open_ports}")
    else:
        print("open port not found")

if __name__ == "__main__":
    main()




