from openpyxl import load_workbook


def read_xlsx(filename, intestation=True):

	data = dict()
	wb = load_workbook(filename)
	main_sheet_name = wb.get_sheet_names()[0]
	main_sheet = wb.get_sheet_by_name(main_sheet_name)

	minimum_row = 2 if intestation else 1

	for name, info in main_sheet.iter_rows(min_row=minimum_row):
		data[name.value] = [
			x.replace("_x000D_", "").split(':') 
			for x in info.value.split('\n') if x
		]

	return data

def save_xlsx(filename, data, intestation=None):
	pass
