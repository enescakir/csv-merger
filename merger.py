import os, csv, argparse, re

parser = argparse.ArgumentParser(description='CSV merger app')
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--pattern', dest="pattern", action='store')
parser.add_argument('-o', '--output', dest="output", action='store', required=True)
parser.add_argument('-d', '--directory', dest="directory", action='store')
parser.add_argument('-nh','--noheader', dest="header", action='store_true')
arguments = parser.parse_args()

pattern = ".*?"
directory = os.getcwd()

if arguments.pattern:
    pattern = arguments.pattern

if arguments.directory:
    pattern = arguments.directory

outputFileName = arguments.output
csvFiles = []

curlist = os.listdir(directory)
for name in curlist:
    if name.endswith('.csv') and re.search(patterm, name):
        newpath = directory + "/" + name
        if not os.path.isdir(newpath):
            csvFiles.append(newpath)
