#!/usr/bin/env python3
"""Two positional arguments"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='Two positional arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('color',
                        metavar='COLOR',
                        type=str,
                        help='First argument')

    parser.add_argument('size',
                        metavar='SIZE',
                        type=int,
                        help='Second argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    print('color =', args.color)
    print('size =', args.size)


# --------------------------------------------------
if __name__ == '__main__':
    main()
