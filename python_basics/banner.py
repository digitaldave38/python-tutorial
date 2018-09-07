import sys

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

message = sys.argv[1]

if __name__ == '__main__':
    banner(sys.argv[1])