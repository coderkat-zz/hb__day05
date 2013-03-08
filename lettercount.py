from sys import argv

script, filename = argv

#def character_count(file_name):
f = open(filename)

# set variable to store file as a string
eachletter = f.read()

 	
f.close()

# convert all letters to lowercase
all_lower = eachletter.lower()

# set ASCII start value ('a')
character = ord('a')
#print character

#for loop to look for each char in ASCII
for item in range(0, 25):
#	print character
	print all_lower.count(chr(character))
	character += 1

	