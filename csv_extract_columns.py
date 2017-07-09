#!/usr/bin/env python
"""extract_column_from_csv.py: 

    given a csv file and names of columns, write a new csv file.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import csv
import numpy as np
import re
import sys

from collections import defaultdict

def main(args):
    print("[DEBUG]: %s" % args)
    results = defaultdict(list)
    with open(args['input_file'], 'r') as f:
        lines = f.read().split('\n')
    header, lines = lines[0].split(','), lines[1:]
    colsToExtract, newHeader = [], []
    for i, h in enumerate(header):
        for c in args['col']:
            if re.search(r'%s' % c, h):
                colsToExtract.append(i)
                newHeader.append(h)

    data = np.genfromtxt(args['input_file'], delimiter=','
            , skip_header=True, usecols=colsToExtract
            )

    outfile = args['output_file']
    print("Writing extracted data to %s" % outfile)
    np.savetxt(outfile, data, delimiter=',', header=",".join(newHeader),
            comments='')


if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Select columns from csv file.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--input_file', '-in'
        , required = True
        , help = 'Input csv file'
        )
    parser.add_argument('--col', '-c'
        , action = 'append'
        , help = '''Column to select. All columns matching this pattern (regex
        python) will be selected'''
        )
    parser.add_argument('--output_file', '-out'
        , required = False
        , default = sys.stdout
        , type = argparse.FileType('w')
        , help = 'Output file to write to'
        )

    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    main(vars(args))
