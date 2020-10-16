#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-15
Purpose: Telephone
"""

import argparse
import sys
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file',
                        default=[sys.stdin])

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1') 

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    mutations = args.mutations
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    new_str = ''
    if mutations >= 0:
        rounding_num = round(len(text) * mutations)
        text_num = [i for i in range(len(text))]
        rand_indexes = random.sample(text_num, k=rounding_num)
        for num, char in enumerate(text):
            if num in rand_indexes:
                new_str += random.choice(alpha)[0]
            else:
                new_str += char
            
        for stoppage in rand_indexes:
            new_str += 
        

    print(f'You said: "{text}"')
    print(f'I heard : "{new_str}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
