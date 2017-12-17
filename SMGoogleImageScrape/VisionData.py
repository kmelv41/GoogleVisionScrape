import io
from google.cloud import vision
import json

vision_client = vision.Client()

lblDict = []

for i in range(501):

	file_name = 'Screenshots/shot'+str(i)+'.png'

	with io.open(file_name,'rb') as image_file:
		content = image_file.read()
		image = vision_client.image(content=content)

	labels = image.detect_labels()

	shotDict = {'shot'+str(i):[]}

	for label in labels:
		shotDict['shot'+str(i)].append(label.description)

	lblDict.append(shotDict)
	print(shotDict)

with open('photodescriptions.json', 'w') as fout:
	json.dump(lblDict, fout)

