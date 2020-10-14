#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-07
Purpose: Jump the Five - Encrypt incoming phone numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='str',
                        help='Phone number to be encrypted')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.number

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }
    for i in numbers:
        if jumper.get(i):
            print(jumper.get(i), end='')
        else:
            print(i, end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
