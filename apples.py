#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-13
Purpose: Apples and Bananas
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file',
                        default=sys.stdin)

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        choices=['a', 'e', 'i', 'o', 'u'],
                        metavar='str',
                        type=str,
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    repl = {}
    for vowel in 'aeiou':
        repl[vowel]=args.vowel
    for vowel in 'AEIOU':
        repl[vowel]=args.vowel.upper()

    if os.path.isfile(args.text): 
        fh = open(args.text).read().rstrip()
        new = fh.translate(str.maketrans(repl))
        print(new)
    else: 
        new = args.text.translate(str.maketrans(repl))
        print(new)    


# --------------------------------------------------
if __name__ == '__main__':
    main()
