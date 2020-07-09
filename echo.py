#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Triston Reeves"


import sys
import argparse

def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    # your code here
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help="Text to echo")
    parser.add_argument('-u', '--upper', action="store_true", help="Transfer text to uppercase")
    parser.add_argument('-l', '--lower', action="store_true", help="Transfer text to lowercase")
    parser.add_argument('-t', '--title', action="store_true", help="Transfer text to titlecase")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    msg = args.text
    if args.lower:
        msg = msg.lower()
    if args.upper:
        msg = msg.upper()
    if args.title:
        msg = msg.title()

    print(msg)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
