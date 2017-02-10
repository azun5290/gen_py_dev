from xlrd import open_workbook

book = open_workbook('tester_del_2_short.xlsx')
sheet = book.sheet_by_index(0)

# read header values into the list
keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

dict_list = []
for row_index in xrange(1, sheet.nrows):
    d = {keys[col_index]: sheet.cell(row_index, col_index).value
         for col_index in xrange(sheet.ncols)}
    dict_list.append(d)
    print('  KEYsss   ', d.keys(), '  VALsss  ', d.values())
    print('='*200)

print dict_list
