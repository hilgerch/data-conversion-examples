#Read from name.txt
with open('name.txt') as f:
	my_name = f.read()

#Write to hello.txt
with open("hello.txt", "w") as f:
	f.write("hello my name is " + my_name )
