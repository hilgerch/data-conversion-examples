#Read superheros.json into a variable
import json
from pprint import pprint

with open ('superheros.json') as f:
	data = json.load(f)



#select the members

members = data['members']

import csv

with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = [

		'name',
		'age',
		'secretIdentity',
		'powers',
		'squadName',
		'homeTown',
		'formed',
		'secretBase',
		'active'


		]

	writer.writerow(header)

# Loop over the members

	for m in members:
		row = [
			m['name'],
			m['age'],
			m['secretIdentity'],
			str(m['powers']),
			data['squadName'],
			data['homeTown'],
			data['formed'],
			data['secretBase'],
			data['active'],

		]

		writer.writerow(row)


# For each member, output the row 

# Save that to a CSV file 

