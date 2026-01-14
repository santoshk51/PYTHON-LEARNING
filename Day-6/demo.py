data = True
line = 1

with open("sample.txt", "r") as f:
	while data:
		data = f.readline()

		if("badhiya" in data):
			print(f" word found {line}")
			break

		print(data)
		line += 1