#! /usr/bin/env python
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Beating Heart Project')

    #parser.add_argument(dest='filenames', metavar='filename',nargs='*')
    #both input and output args optional, use cwd if not supplied or -i
    parser.add_argument('-i',dest='input')
    parser.add_argument('-o',dest='output')
    parser.add_argument('-v',dest='visual')
    parser.add_argument('-c',dest='charts')
    parser.add_argument('-t',dest='params')
    #files like .wav or .csv or .xls
    parser.add_argument('-p',dest='phase')

    args = parser.parse_args()

if __name__ == '__main__':
	main()
