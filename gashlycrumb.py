#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-12
Purpose: Gashlycrumb
"""

import argparse
from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        help='Letter(s)',
                        metavar='letter',
                        nargs='+',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # # compact method using dictionary comprehension
    # line_dict = {line[0]: line.rstrip() for line in args.file}
    
    # for letter in args.letter:
    #     print(lookup.get(letter.upper(), f'I do not know "{letter}".'))

    line_dict = {}
    for line in args.file:
        line_dict[line[0]] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in line_dict:
            print(line_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
