# Ler arquivo para encontrar links do linkedin
import codecs

def read_file():
	#with open("capacita_mdt.txt", encoding ="utf8") as f:
	#	read_file = f.read()
	types_of_encoding = ["utf8", "cp1252", "cp850", "utf-8"]
	for i in types_of_encoding:
		with codecs.open("capacita_mdt.txt", encoding = i, errors ='replace') as f:
			try:
				read_file = f.read()
				break
			except UnicodeDecodeError:
				pass
	f.close()

	return read_file

def find_string(file, string):
	count = 0
	for i in file:
		
			#https://www.linkedin.com/in/amanda-fernandes-2125b83b/
			#[https://https://www.linkedin.com]

if __name__ == "__main__":
    file = read_file()
    #find_string(file, "www.linkedin.com")
    #print(file)
    print(type(file))