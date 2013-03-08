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


find_list = [0] * 26
#pos 0 == a == ASCII 97

for letter in all_lower:
	new_char = ord(letter) - ord('a')
	find_list[new_char] += 1
		#add 1 to the index that represents that char
print find_list

