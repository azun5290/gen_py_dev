import csv

def read_csv(filename, intestation=True):

	data = dict()

	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		if intestation:
			next(reader)

		for name, info in reader:
			data[name] = [x.split(':') for x in info.split('\n') if x]

	return data

def save_csv(filename, data, intestation=None):

	with open(filename, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		if intestation:
			writer.writerow[instestation]

		for name in data:
			info_string = '\n'.join([': '.join(x) for x in data[name]])
			writer.writerow([name, info_string])
