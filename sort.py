# Sifts through the file and outputs the specified string in a .txt file
def sort(file, export, string):
	file = open(rf"{file}", "r+", encoding="utf-8")
	for lines in file.readlines():
		if string in lines:
			print(lines.replace("\n", ""))
			with open(export, "a", encoding="utf-8") as output:
				output.write(lines)

# Verifies if the export file exists or not, if not create file
def check_export(export):
	try:
		file = open(export, "r", encoding="utf-8")
	except IOError:
		file = open(export, "w", encoding="utf-8")

if __name__ == "__main__":
	file_name = input("[!] Input the file name you want to sort: ")
	export_file = input("[!] Submit the export file: ")
	check_export(export_file)
	string = input("[!] Insert the string that you want to sort: ")
	sort(file_name, export_file, string) # Function to sort out the string
