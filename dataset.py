import sys
import re

from difflib import get_close_matches, SequenceMatcher
from file_handler import read_file, save_file
from valid_fields import valid_fields

class Dataset(object):
	"""
	Documentation

	"""

	def __init__(self):
		self.data          = None
		self.invalid_chars = re.compile(r'[\t\n\r\f\v\#]*')
		self.intestation = [
			"name",
			"desc",
			"info"
		]

	def read(self, input_file):
		"""
		Import the dataset from file.

		:param string filename: the name of the file.
		"""
		data, self.intestation = read_file(input_file)

		self.data = []
		for element in data:
			
			info = [x.split(':') for x in element[-1].split('\n')]
			file_fields = [row[0] for row in info]
			d = dict()

			for valid_field in valid_fields:
				try:
					new_field = get_close_matches(valid_field, file_fields, n=1,
							cutoff=0.7)
					index = file_fields.index(new_field[0])
					value = info[index][1]
				except:
					value = ""
			
				d[valid_field] = value

			self.data.append([ *element[:-1], d])
	
	def clean_field(self):
		"""
		Clean the string by removing the unnecessary string.
		"""
		for element in self.data:
			
			info_field = element[-1]

			for key in info_field.keys():
				info_field[key] = self._clean_string(info_field[key])


	def save(self, output_file, blank=None):
		"""
		Write the dataset to specific file.

		:param string filename: the name of the file.
		"""

		data = []

		blank_str = " BLANK" if blank else ""

		for element in self.data:
			
			field_values = [
				" {}".format(value) if value else blank_str
				for value in element[-1].values()
			]

			field_names = list(element[-1].keys())

			info_str = '\n'.join([
				"{}:{}".format(field_names[i], field_values[i])
				for i in range(len(field_names))
			])

			data.append([ *element[:-1], info_str])

			
		save_file(output_file, data)


	def ad(self):
		"""
		Add the user to active directory.
		WARNING: TESTING FUNCTION
		"""

		#pyad.set_defaults(
		#	ldap_server = server,
		#	username	= username,
		#	password	= password
		#)
		group = pyad.from_dn("group_name")
		
		for element in self.data:
			new_user = pyad.ADUser.create()
			new_user.set_attributes()
			group.add_members(new_user)

	def find(self, column, key):
		"""
		Allow to find and modify an existing element; `column` is the index of
		the column where looking for, it can be also the name of the column if
		the intestation exists. `key` is the string to match the element.

		:param int/str column: the column of the dataset
		:param str key: the key to looking for
		"""
		if isinstance(column, str):
			column = self.intestation.index(column)
		elif not isinstance(column, int):
			raise ValueError("Not valid field.")

		for index, element in enumerate(self.data):

			if element[column] == key:
				
				for i, field in enumerate(element[:-1]):
					new_value = input("{}: ".format(self.intestation[i]))
					self.data[index][i] = new_value
				
				for info in element[-1]:
					new_value = input("{}/{}: ".format(
							self.intestation[-1], info
					))
					element[-1][info] = new_value
					

	def __str__(self):
		"""
		Print the dataset.
		"""
		string = ""
		for element in self.data:
			for field in element[:-1]:
				string += "{}\n".format(field)
			for field in element[-1]:
				string += "\t{}: {}\n".format(field, element[-1][field])
		return string

	def _clean_string(self, string):
		"""
		"""
		return self.invalid_chars.sub('', string).strip()
