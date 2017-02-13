import sys
import re

from difflib import get_close_matches
from file_handler import read_file, save_file

class Info(object):
	SHARE_NAME = 	'Share Owner Name'
	SALARY_NO =		'Salary No'
	DELEGATE_NAME =	'Delegate Owner Name'
	DELEGATE_SALARY = 'Delegate Salary No'
	DATA_CLASSIF =	'Data Classification'

class Dataset(object):
	"""
	Documentation

	"""

	def __init__(self):
		self.data          = None
		self.invalid_chars = re.compile(r'[\t\n\r\f\v\#]*')
		self.valid_fields  = [
			Info.SHARE_NAME,
			Info.SALARY_NO,
			Info.DELEGATE_NAME,
			Info.DELEGATE_SALARY,
			Info.DATA_CLASSIF
		]

	def read(self, input_file):
		"""
		"""
		self.data = read_file(input_file)
	
	def reformat(self):
		"""
		"""
		for name in self.data:

			new_info = []
			for info in self.data[name]:
			
				valid_info = get_close_matches(info[0], self.valid_fields, n=1)
				
				if valid_info:
					try:
						valid_value = self._clean_string(info[1])
					except IndexError:
						valid_value = ""

					new_info.append([valid_info[0], valid_value])
					
			self.data[name] = new_info


	def save(self, output_file):
		"""
		"""
		save_file(output_file, self.data)

	def __str__(self):
		"""
		"""
		string = ""
		for name in self.data:
			string += "{}\n".format(name)
			for info in self.data[name]:
				string += "\t{}\n".format(' '.join(info))
		return string

	def _clean_string(self, string):
		"""
		"""
		return self.invalid_chars.sub('', string).strip()
