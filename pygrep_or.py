#!/usr/bin/env python3

"""Utility script to mimic grep in python.

    <filename> <search str1> <search str2> ... -o <outfile>

    The -o is optional.

    Example use1 : This example will search through the file pygrep.py for the strings '4e0000', 'Poll', and 'cancel'.
                   If any of the 3 are found in a given line, it will output the line to stdout.

        python3 pygrep.py 4e0000 Poll cancel -o blah.txt

    Example use 2: This example will search through the file pygrep.py for the strings '4e0000', 'Poll', and 'cancel'.
                   If any of the three are found in a given line, it will output the line to both stdout and to the file
                   blah.txt.


"""

import argparse
import pathlib
import re
import sys
from typing import List


class FilterNotFound(Exception):
    pass


def grep(infile: str, filter_by: List[str], outfile=None):
    print(f"Input file : {pathlib.Path(outfile).parent.absolute()}/{infile}")

    if outfile:
        print(f"writing output to {pathlib.Path(outfile).parent.absolute()}/{outfile}")
        outfile = open(outfile, "w+")

    print(f"Filtering by {' '.join(filter_by)}")

    try:
        with open(infile, "r") as file:

            for line in file:

                found = False
                for filter_str in filter_by:
                    if re.search(filter_str, line):
                        found = True
                        break
                if not found:
                    continue

                if outfile:
                    outfile.write(line)
                else:
                    print(line, end="")

    except FileNotFoundError:
        print("    failed to open input file", file=sys.stderr)
        print("    usage : <filename> <search str1> <search str2> ...", file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help='input file name')
    parser.add_argument('filter_by', type=str, nargs='*', help="filter your search by")
    parser.add_argument('-o', '--outfile', type=str, required=False, help="output file")
    args = parser.parse_args()

    infile = args.infile
    filters = args.filter_by
    outfile = args.outfile

    grep(args.infile, args.filter_by, args.outfile)
