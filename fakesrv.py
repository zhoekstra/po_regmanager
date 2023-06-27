#!/usr/bin/env python

import os
import sys
import socket
import signal
import argparse


def handleUDP(cs, MSG, PORT):
    data, addr = cs.recvfrom(1024)
    print("{0:s}:{1:d}->UDP{3:d}: {2:s}".format(addr[0], addr[1], data.rstrip('\n'), PORT))
    if MSG:
        cs.sendto("{0:s}".format(MSG), addr)


def handleTCP(cs, addr, MSG, PORT):
    print("Connection from: {0:s}:{1:d}->TCP{2:d}".format(addr[0], addr[1], PORT))
    try:
        data = cs.recv(1024)
        print("{0:s}:{1:d}->TCP{3:d}: {2:s}".format(addr[0], addr[1], data.rstrip('\n'), PORT))
        if MSG:
            cs.sendall("{0:s}".format(MSG))
        cs.close()
    except:
        print("Some error, killing connection")
        cs.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tcp', action='store_true', dest='istcp', help="listen on TCP", default=True)
    parser.add_argument('-u', '--udp', action='store_true', dest='isudp', help="listen on UDP", default=False)
    parser.add_argument('-p', '--port', action='store', dest='PORT', type=int, help='port number to listen on',
                        required=True)
    parser.add_argument('-m', '--message', action='store', dest='MSG', help="message to output on connection",
                        default="Hello World!")
    parser.add_argument('-f', '--file', action='store', dest='FILE', default="",
                        help="file to read a message from, read out on conneciton")
    args = parser.parse_args()

    FILE = args.FILE
    MSG = args.MSG
    istcp = args.istcp
    isudp = args.isudp
    PORT = args.PORT

    if FILE:
        try:
            with open(FILE, "r") as f:
                MSG = f.read()
        except:
            print("File \"{0:s}\" does not exist. Exiting...")
            return 1

    if istcp and isudp:
        print("Both TCP and UDP specified, exiting...")
        return 1

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    if istcp:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', PORT))
        s.listen(100)
        print("Listening on {} TCP".format(PORT))
        while 1:
            (cs, addr) = s.accept()
            pid = os.fork()
            if pid == 0:
                s.close()
                handleTCP(cs, addr, MSG, PORT)
                sys.exit(0)
            cs.close()

    elif isudp:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', PORT))
        print("Listening on {} UDP".format(PORT))
        while 1:
            handleUDP(s, MSG, PORT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
