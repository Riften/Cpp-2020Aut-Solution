import sys
import hashlib


def md5(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        file_hash = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(8192)
    return file_hash.hexdigest()


if __name__ == '__main__':
    print(md5(sys.argv[1]))
