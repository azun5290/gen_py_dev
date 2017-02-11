from openpyxl import load_workbook, Workbook


def read_xlsx(filename, intestation=True):

	data = dict()
	wb = load_workbook(filename)
	main_sheet_name = wb.get_sheet_names()[0]
	main_sheet = wb.get_sheet_by_name(main_sheet_name)

	minimum_row = 2 if intestation else 1

	for name, info in main_sheet.iter_rows(min_row=minimum_row):
		data[name.value] = [
			x.split(':') 
			for x in info.value.replace("_x000D_", "\n").split('\n') if x
		]

	return data

def save_xlsx(filename, data, intestation=None):
	
	wb = Workbook()
	main_sheet = wb.active
	main_sheet.title = filename

	starting_row = 1
	if intestation:
		main_sheet.cell(row=starting_row, column=1).value = instestation[0]
		main_sheet.cell(row=starting_row, column=2).value = instestation[1]
		starting_row += 1

	for index, name in enumerate(data.keys(), start=1):
		info_string = '\n'.join([': '.join(x) for x in data[name]])
		main_sheet.cell(row=index, column=1).value = name
		main_sheet.cell(row=index, column=2).value = info_string

	wb.save(filename)
