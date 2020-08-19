import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 30000        # The port used by the server

while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
       # s.sendall(b'Hello, world')
        data = s.recv(1024)
        if data == b'Cell1_ProcTime_Lower':
            s.sendall(b'360')
        elif data == b'Cell1_ProcTime_Upper':
            s.sendall(b'540')
        elif data == b'Cell1_SetupTime_Lower':
            s.sendall(b'30')
        elif data == b'Cell1_SetupTime_Upper':
            s.sendall(b'45')
        elif data == b'Cell1_MTTR':
            s.sendall(b'5400')
        elif data == b'Cell1_Availability':
            s.sendall(b'95')    
        elif data == b'Cell2_ProcTime_Lower':
            s.sendall(b'180')
        elif data == b'Cell2_ProcTime_Upper':
            s.sendall(b'270')
        elif data == b'Cell2_SetupTime_Lower':
            s.sendall(b'60')
        elif data == b'Cell2_SetupTime_Upper':
            s.sendall(b'120')
        elif data == b'Cell2_MTTR':
            s.sendall(b'4800')
        elif data == b'Cell2_Availability':
            s.sendall(b'90')    
            
