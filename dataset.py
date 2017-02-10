import sys
import re

from csv_reader import parse_csv

class Dataset(object):

	def __init__(self):
		self.data          = None
		self.invalid_chars = re.compile(r'[\t\n\r\f\v\#]*')

	def read(self, input_file):
		self.data = parse_csv(input_file)
	
	def reformat(self):
		
		for name in self.data:

			new_info = []
			for info in self.data[name]:
				
				if len(info) != 2:
					continue
				
				tmp = [self._clean_string(i) for i in info]
				if all(tmp):
					new_info.append(tmp)

			self.data[name] = new_info

	def save(self, output_file):
		print("Store...")

	def __str__(self):

		string = ""
		for name in self.data:
			string += "{}\n".format(name)
			for info in self.data[name]:
				string += "\t{}\n".format(' '.join(info))
		return string

	def _clean_string(self, string):
		return self.invalid_chars.sub('', string).strip()
