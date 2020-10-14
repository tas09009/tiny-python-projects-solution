#!/usr/bin/env python3
"""
Author : taniya <taniya@localhost>
Date   : 2020-10-08
Purpose: Howler for Ron Weasley
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler for Ron Weasley',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper())
    out_fh.close()  
   

# --------------------------------------------------
if __name__ == '__main__':
    main()








