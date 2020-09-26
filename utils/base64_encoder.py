import sys
import base64


def base64_encode(filepath: str):
    encoded_string = base64.b64encode(open(filepath, "rb").read())
    print(encoded_string.decode('ascii'))


if __name__ == '__main__':
    base64_encode(sys.argv[1])
