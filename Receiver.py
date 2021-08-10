from socket import *
serverPort = 9000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
seq_num=''
checksum=''
data=''
def savedata(data):
    f=open(r'recvdata.txt','a')
    f.write(str(data))
    print("saved")
    f.close()
def checksumrecv(data,checksum):
    binar=''.join(format(i, '08b') for i in bytearray(data, encoding ='utf-8'))
    bincom=int(binar,2)
    checksum=int(checksum,2)
    return bincom+checksum
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    msg=str(message.decode())
    msg=msg.split("#")
    seq_num=msg[0]
    data=msg[1]
    checksum=msg[2]
    print("seq="+seq_num+"\n")
    print("data="+data)
    print("checksum="+checksum+"\n")
    savedata(data)
    ack=seq_num
    if checksumrecv(data,checksum)==-1:
        print("Status OK")
        serverSocket.sendto(ack.encode(),clientAddress)
    else:
        err="faulty packet"
        serverSocket.sendto(err.encode(),clientAddress)
    print("--------x--------x--------\n")

        

        
