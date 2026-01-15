with open("log.txt", "a") as file:
	file.write("Program run successfully")

with open("log.txt", "r") as file:
	print(file.read())