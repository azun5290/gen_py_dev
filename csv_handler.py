import csv

def read_csv(filename, intestation=True):
	"""
	Return a list of the elements in the csv file. Each element is stored in a
	list that contains the fields of the element.

	:param string filename: the name of the csv file to read.
	:param bool intestation: flag to indicate if the file contains the
		intestation.
	:rtype: list(list)
	"""
	data = []

	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		if intestation:
			next(reader)

		for element in reader:
			data.append(element)
			#data[name] = [x.split(':') for x in info.split('\n') if x]

	return data

def save_csv(filename, data, intestation=None):
	"""
	Store the list of the elements to the csv file. Each element contains a list
	with the fields of the element.

	:param string filename: the name of the csv file where store the data.
	:param list(list) data: the data to store.
	:param list(string) intestation: the list of the string to write as
		intestation.
	"""

	with open(filename, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		if intestation:
			writer.writerow[instestation]

		for name in data:
			writer.writerow(name)
