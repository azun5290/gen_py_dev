import sys 
import re

from dataset import Dataset

class GenPyDev(object):

	input_file  = None
	output_file = None

	def __init__(self, input_file, output_file):
		self.input_file  = input_file
		self.output_file = output_file

	def run(self):
		dataset = Dataset()
		dataset.read(self.input_file)
		dataset.clean_field()
		dataset.find(0, "Corporate-Resource-DS BTSS")
		dataset.save(self.output_file)


if __name__ == "__main__":
	
	if len(sys.argv) != 3:
		print("Usage: {} <input> <output>".format(sys.argv[0]))
		sys.exit()

	gen = GenPyDev(sys.argv[1], sys.argv[2])
	gen.run()
