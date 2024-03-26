import socket
import struct
import time
import zlib

def calculate_crc(data):
    return zlib.crc32(data)

def send_command(command, data):
    # 创建一个 bytearray 对象来存储数据
    buffer = bytearray()
    buffer.append(0x4E)
    buffer.append(0x66)
    size = len(data)
    buffer.extend(struct.pack('!H', size))
    buffer.extend(struct.pack('!H', command))
    buffer.extend(data)
    crc = calculate_crc(buffer[2:])
    buffer.extend(struct.pack('!I', crc))
    return buffer

def main():
    command = 0x2001
    command_new = 0x50B1
    data = b'{"robot": 1, "status": 1}'
    data_new = b'{"robot": 1, "open": true}'

    host = '192.168.1.14'
    port = 6001

    packet = send_command(command, data)

    packet_new = send_command(command_new, data_new)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        sock.sendall(packet)
        print("Data sent successfully")
        time.sleep(2)
        sock.sendall(packet_new)
        print("Data_new sent successfully")
        time.sleep(2)
    except Exception as e:
        print("Error:",e)
    finally:
        sock.close()

if __name__ == '__main__':
    main()