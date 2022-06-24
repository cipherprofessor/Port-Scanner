import socket
ip = '192.168.114.151'
port_list=[10,25,20,80,90,8080,23,21,22,135,445,139,902,5357,912,139,445]

for port in port_list:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = s.connect_ex((ip,port))

    if result == 0:
        print('_' *60)
        print('Port',port,'Open')
        print('_'*60)
    else:
        print('Port',port,'Closed')