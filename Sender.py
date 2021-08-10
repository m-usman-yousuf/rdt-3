from socket import *
import time
err="faulty packet"
servername='localhost'
serverport=9000
s=socket(AF_INET,SOCK_DGRAM)
Ack=None
def checksum(st):
    binar=''.join(format(i, '08b') for i in bytearray(st, encoding ='utf-8'))
    bincom=bin(~int(binar,2))
    return bincom
def datatopkt():
    data=open(r'D:\Semester 6\Computer Networks\Assignment 3\V7.0\sdata.txt','r')
    lines = data.readlines()
    return lines
def send(data):
    global Ack
    count=0
    for i in range(len(data)):
        pkt=str(count%2)+"#"+data[i]+"#"+str(checksum(data[i]))
        s.sendto(pkt.encode(),(servername,serverport))       
        count+=1
        s.settimeout(2)
        try:
             Ack, serverAddress = s.recvfrom(2048)
             s.settimeout(None)
        except socket.timeout:
            print("ACK Not Received. Resending Packet")
            s.sendto(pkt.encode(),(servername,serverport))       
            count+=1
            s.settimeout(2)
            Ack, serverAddress = s.recvfrom(2048)
            s.settimeout(None)

        if Ack!=None:
            print("ACK Received")
        if Ack!=count%2:
            pass
        if Ack.decode()==err:
            print("Sent Data Corrupted. Resending")
            s.sendto(pkt.encode(),(servername,serverport))       
            count+=1
            s.settimeout(2)
            Ack, serverAddress = s.recvfrom(2048)
            s.settimeout(None)
                
        print(Ack.decode())
        
send(datatopkt())
s.close()


