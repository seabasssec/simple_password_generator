import argparse
from os import urandom

parser = argparse.ArgumentParser(description='This simple program generate passwords. For example "python3 simple_password_generator.py -s 2 -l 16"')
 
parser.add_argument('-s', '--set', metavar='set', required=True, choices={1,2}, help='Type of generate. 1 - without special charecters. 2 - with special charecters "!" and "="', type=int)
parser.add_argument('-l', '--length', metavar='length', required=True, help='Length of password', type=int)

args = parser.parse_args()

length = args.length

def generator(length, set_of_chars):
    res = "".join(set_of_chars[c % len(set_of_chars)] for c in urandom(length))
    return res

if __name__ == '__main__':
    if args.set == 1:
        set_of_chars = "abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789"
        print(generator(length, set_of_chars))


    if args.set == 2:
        set_of_chars = "abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789!="
        while True:
            result = generator(length, set_of_chars)
            if "!" not in result or "=" not in result:
                pass
            else:
                break
        print(result)