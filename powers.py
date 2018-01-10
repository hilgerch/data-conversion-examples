import json
from pprint import pprint

with open('superheros.json') as f:
	data = json.load(f)


#create blank list of powers

powers = []

members = data['members']

for member in members:
	member_powers = member['powers']

	for power in member_powers:
		powers.append(power)



unique_powers = list(set(powers))

pprint(unique_powers)