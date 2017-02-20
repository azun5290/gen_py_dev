from csv_handler import read_csv, save_csv
from xlsx_handler import read_xlsx, save_xlsx

import os
import sys

def read_file(filename, *args, **kwargs):
	"""
	Interface to manage several type of file: it recalls the specialized
	function according to the file extension. It raises `RuntimeError` for
	unknown type of file.

	:param string filename: the name of the file.
	"""
	# Get the right function to read the dataset
	specialized_method = {
		".csv": 	read_csv,
		".xlsx":	read_xlsx
		# Add line here to manage new type file
		# <extension>: <name of function>
		# ".example": read_example
	}
	extension = os.path.splitext(filename)[1]

	read_function = specialized_method.get(extension)

	if read_function is None:
		raise RuntimeError("Not valid file.")
		sys.exit()

	# Read the data from file
	return read_function(filename, *args, **kwargs)


def save_file(filename, *args, **kwargs):
	"""
	Interface to manage several type of file: it recalls the specialized
	function according to the file extension. It raises `RuntimeError` for
	unknown type of file.

	:param string filename: the name of the file.
	"""
	# Get the right function to read the dataset
	specialized_method = {
		".csv": 	save_csv,
		".xlsx":	save_xlsx
		# Add line here to manage new type file
		# <extension>: <name of function>
		# ".example": save_example
	}

	extension = os.path.splitext(filename)[1]

	save_function = specialized_method.get(extension)

	if save_function is None:
		raise RuntimeError("Not valid file.")
		sys.exit()

	# Save the data to file
	save_function(filename, *args, **kwargs)
