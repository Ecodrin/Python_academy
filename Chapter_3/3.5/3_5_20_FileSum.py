def main():
    su = 0
    with open('numbers.num', 'rb') as f:
        x = f.read(2)
        while x:
            su += int.from_bytes(x, "big")
            x = f.read(2)
    print(su % (2 ** 16))


if __name__ == '__main__':
    main()


#b'\x16\xe1\x11&SX\xf0\xadv\xf4\x87\xcdh<x\x95w\xde\xe1\xf0\x08f\x0f\xb6\xf7Z\xcd\xdaK\x9dv\x97\xb0\x1fh\x99\xa6\xff\xa3sI o\xd1Im\xedE\x98\xfe\xe4\xfe\x02\xaa\x1f0\x06\x8e\x19\x00PnR\xa2\x1a\x04\xaa\xe9c\xa0\x0b*t\xb7\xca\xc7\xef\xbe\xe5\xb8'