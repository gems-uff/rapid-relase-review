import argparse
import pybtex

parser = argparse.ArgumentParser(description='Process bibtext for snowballing')
parser.add_argument('bibfile', metavar='i', 
                    help='the bibfile to parse')
parser.add_argument('group', metavar='g' )

args = parser.parse_args()
