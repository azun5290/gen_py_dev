import csv
import re
import collections

# open CSV file for: 1. reading; 2. create output CSV file for writing; AND 3. for appending
inputCSV = open(r'tester_del_2_short.csv', 'rb')
outputCSV = open(r'tst_del_2_sh_OUT.csv', 'wb')
appendCSV = open(r'tst_del_2_sh_OUT_APP.csv', 'ab')

# liset = []
answer = collections.defaultdict(list)
# answer = collections.namedtuple(liset, row)
with open(r'tester_del_2_short.csv', 'r+') as istream:
    for line in istream:
        line = line.strip()
        print(line)

        try:
            k, v = line.split(',', 1)
            # k, v = line.split(',')
            # print(k)
            answer[k.strip()].append(v.strip())
        except ValueError:
            print('Ignoring: malformed line: "{}"'.format(line))

print(answer)
# print(answer).items().__getslice__(0,12)

# create reader, writer & append objects
cr = csv.reader(inputCSV, dialect='excel')
cw = csv.writer(outputCSV, dialect='excel')
ca = csv.writer(appendCSV, dialect='excel')

for row in cr:
    # print(row)
    liset = []
    # answer = collections.defaultdict(liset)
    liset.append(row)
    # with open('tester_filt_2_short.csv', 'r+') as istream:
    print(liset)

# close files
inputCSV.close()
outputCSV.close()
appendCSV.close()