#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-07
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item_arg = args.item
    sort_arg = args.sorted

    if sort_arg:
        item_arg.sort()

    if len(item_arg) == 1:
        print(f'You are bringing {item_arg[0]}.')
    elif len(item_arg) == 2:
        print(f'You are bringing {item_arg[0]} and {item_arg[1]}.')
    elif len(item_arg) >= 3:
        # item_arg.insert(-1, ' and ')
        item_arg[-1] = f'and {item_arg[-1]}'
        str_item = ', '.join(item_arg)
        print(f'You are bringing {str_item}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
