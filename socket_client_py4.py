import socket
buf = 1024
direc = ("direccion_ip_servidor", 20000)

if __name__ == '__main__':
    miSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        peticion = input('?: ').strip()
        if peticion == "":
            break
        miSocket.sendto("%s" %peticion, direc)
        resp, adr = miSocket.recvfrom(buf)
        print ("=> %s" % resp) 
    miSocket.close()
    print ("Fin del cliente UDP")
