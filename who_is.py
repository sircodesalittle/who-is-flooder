from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST
from binascii import unhexlify
from time import sleep


def init_socket():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    return sock


def init_payload():
    # Payload for UDP packet (A Broadcast who-Is with specified full instance number range)
    # This packet is 480 bits long
    data = '81 0b 00 12 01 20 ff ff 00 ff 10 08 09 00 1b 3f ff ff'
    # take data string and return list datatype. Use space as separator.
    # should return ['81', '0b', '00'...]
    data_list = data.split(' ')
    # Join elements of the list with an empty space
    who_is_data = ''.join(data_list)
    return unhexlify(who_is_data)


WHO_IS = init_payload()
SOCK = init_socket()


def sendpacket(target_ip, udp_port):
    SOCK.sendto(WHO_IS, (target_ip, udp_port))


def send_packets_with_delay(target_ip, udp_port, pps, seconds):
    for _ in range(seconds):
        for _ in range(pps):
            sendpacket(target_ip, udp_port)
            sleep(1.0000 / pps)
