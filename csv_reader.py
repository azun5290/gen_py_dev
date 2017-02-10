import csv

def parse_csv(filename, intestation=True):

	data = dict()

	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		if intestation:
			next(reader)

		for name, info in reader:
			data[name] = [x.split(':') for x in info.split('\n')]
