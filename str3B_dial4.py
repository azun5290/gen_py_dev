import csv
import re

# open CSV file for: 1. reading; 2. create output CSV file for writing; AND 3. for appending
inputCSV = open(r'tester_del_2_short.csv', 'rb')
outputCSV = open(r'tester_del_2_short_OUT_X.csv', 'wb')
appendCSV = open(r'tester_del_2_short_OUT_X.csv', 'ab')

# create reader, writer & append objects
cr = csv.reader(inputCSV, dialect='excel')
cw = csv.writer(outputCSV, dialect='excel')
ca = csv.writer(appendCSV, dialect='excel')

# pre-defined fields can be added as follows:
# cw.writerow(['FIELD1_','FIELD2_','FIELD3_','FIELD4_'])

# delete existing field names in input CSV
# ???????????????????????????

# loop through input csv, check for blanks, and write all changes to append csv
for xl_row in cr:
    # print(xl_row)
    for each_string in xl_row:
        line_string = (' ').join(each_string)
        print line_string


    '''
    for each_list in xl_row:
        #print(each_list)
        lines = each_list.split('\n')
        i = 0
        print(lines)
#        if lines[i] = 'Share':
#            lines[i] = ' ****** ' + lines[i]

#        i +=1

        #for
        # ca.writerow(lines.format().rsplit(','))


#        liset = []

    '''

    '''
    for col_name, row in iter(cr):
        print(col_name + '\n' + '='*24 + '\n' + row + '\n' + '*'*24 + '\n')
        # print(row) ---- gen  ----
        liset.append(row)
        print(liset.__sizeof__())
        '\n'.join('{}' for _ in range(len(liset))).format(*liset)
        clean_elem = re.sub(r'\s+', ' ', row.replace(' |', ';'))
        liset = ','.join(map(str, liset))
        print(clean_elem)
        ca.writerow(liset.format().rsplit(','))
'''
# close files
inputCSV.close()
outputCSV.close()
appendCSV.close()
