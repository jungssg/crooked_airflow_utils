import sys

nnn = 1


def hello():
    print("hello")

def pong():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ing")
    else:
        print('ping')

def ping():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ong")
    else:
        print('pong')


if __name__ == "__main__":
    ping()
    pong()
