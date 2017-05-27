import os, csv, argparse, re

parser = argparse.ArgumentParser(description='CSV merger app')
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--pattern', dest="pattern", action='store')
parser.add_argument('-o', '--output', dest="output", action='store', required=True)
parser.add_argument('-d', '--directory', dest="directory", action='store')
parser.add_argument('-nh','--noheader', dest="noheader", action='store_true')
arguments = parser.parse_args()

pattern = ".*?"
directory = os.getcwd()

if arguments.pattern:
    pattern = arguments.pattern

if arguments.directory:
    directory = arguments.directory

output = arguments.output
csv_files = []

curlist = os.listdir(directory)
for name in curlist:
    if name.endswith('.csv') and re.search(pattern, name):
        newpath = directory + "/" + name
        if not os.path.isdir(newpath):
            csv_files.append(newpath)

outputFile = open(output, 'w')
writer = csv.writer(outputFile, delimiter=',');

print("\nFound CSV File Count: " + str(len(csv_files)))

for key, file in enumerate(csv_files):
    reader = csv.reader(open(file))
    rows = list(reader)
    total_count = len(rows)
    print("\t" + file[file.rfind("/")+1:] + " => " + str(total_count) + " rows")
    if not arguments.noheader:
        if(key == 0):
            writer.writerow(rows.pop(0));
    for row in rows:
        writer.writerow(row);
outputFile.close()
total_count = len(list(csv.reader(open(output))))
print("Output: " + output + " => " + str(total_count) + " rows\n")
