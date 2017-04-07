import sys 
import re
import argparse

from dataset import Dataset

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument(
            '--read-intestation',
            dest='rintestation',
            action='store_true'
    )
	parser.add_argument(
            '--write-intestation',
            dest='wintestation',
            action='store_true'
    )
	parser.add_argument(
			'input_file',
			metavar='input_file',
			type=str
	)
	parser.add_argument(
			'output_file',
			metavar='output_file',
			type=str
	)
	parser.set_defaults(rintestation=False, wintestation=False)
	args = parser.parse_args()

	dataset = Dataset()
	dataset.read(args.input_file, read_intestation=args.rintestation)
	dataset.clean_field()
	dataset.save(args.output_file, write_intestation=args.wintestation)
