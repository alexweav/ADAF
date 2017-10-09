import argparse

from DataStreamRegistry import *

def main():
    args = GetArgumentValues()
    reg = DataStreamRegistry(args.ip, args.port)
    print("Starting server at", args.ip, "on port", args.port)
    while reg.GetInputs():
        reg.ReadSockets()

def GetArgumentValues():
    parser = argparse.ArgumentParser(description='Server for the ADAF')
    parser.add_argument('--ip', type=str, nargs='?', default='localhost',
                        help='The IP address of the server')
    parser.add_argument('--port', type=int, nargs='?', default=10000,
                        help='The port to communicate over')
    return parser.parse_args()

main()
