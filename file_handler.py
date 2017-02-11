from csv_handler import read_csv, save_csv
from xlsx_handler import read_xlsx, save_xlsx

import os
import sys

def read_file(filename, *args, **kwargs):

	specialized_method = {
		".csv": 	read_csv,
		".xlsx":	read_xlsx
	}

	extension = os.path.splitext(filename)[1]

	read_function = specialized_method.get(extension)

	if read_function is None:
		raise RuntimeError("Not valid file.")
		sys.exit()

	return read_function(filename, *args, **kwargs)

def save_file(filename, *args, **kwargs):

	specialized_method = {
		".csv": 	save_csv,
		".xlsx":	save_xlsx
	}

	extension = os.path.splitext(filename)[1]

	save_function = specialized_method.get(extension)

	if save_function is None:
		raise RuntimeError("Not valid file.")
		sys.exit()

	return save_function(filename, *args, **kwargs)
