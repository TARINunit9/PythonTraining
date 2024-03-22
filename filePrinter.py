import os
databaseLocation = os.listdir()
for file in databaseLocation:
	if file.endswith(".pem"):
		print(file)
		buffer = open(file)
		print(buffer.read())
		buffer.close()