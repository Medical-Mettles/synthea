import sys
import os
import requests
print "URL :"+sys.argv[1]

dir_path = "/Users/kumarelubandi/WorkSpace/synthea/output/fhir"
entries = os.listdir(dir_path)
url = sys.argv[1]
for entry in entries:
	print(entry)
	filename=dir_path+"/"+entry
	with open(filename) as f:
		# bundle =  f.read()
		x = requests.post(url, data = f.read())
		print(x.text)

