vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},



]

print(vegetables)

import csv


with open('veggies.csv', 'w') as f:
	writer= csv.writer(f)
	writer.writerow(['name','length'])
	for veggie in vegetables:
		#i want the name of the veg
		vegetable_name = veggie['name']
		veggie_name_length = len(veggie['name'])
		#write those to CSV
		row = [vegetable_name, veggie_name_length]
		writer.writerow(row)