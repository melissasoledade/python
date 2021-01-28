# Ler arquivo para encontrar links do linkedin
# Gravar links em txt

import codecs
import re

def read_file():
	text = ['a']

	types_of_encoding = ["utf8", "cp1252", "cp850", "utf-8"]
	for i in types_of_encoding:
		with codecs.open("capacita_mdt.txt", encoding = i, errors ='replace') as f:
			try:
				read_file = f.readlines()
				break
			except UnicodeDecodeError:
				pass
	f.close()

	for line in read_file:
		text.append(line.split())

	return text

def find_string(file, string):
	links = []
	count = 0
	for line in file:
		for i in line:
			if(string in i):				
				links.append(i)
				count += 1
	with open("links_linkedin.txt", "w") as f:
		for link in links:
			f.write("%s\n" %link)

	return count

if __name__ == "__main__":
    file = read_file()
    links = find_string(file, "www.linkedin.com")
    print("Quantidade de links gravados: %d\n" % links)
    #print(file)