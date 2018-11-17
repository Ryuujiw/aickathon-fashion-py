result = {
	 "person": {
		  "boundingBox": {
			   "x": 168,
			   "y": 4,
			   "w": 299,
			   "h": 896
		  },
		  "colors": [
			   {
					"hex": "#ebc4cd",
					"colorName": "pink",
					"colorGeneralCategory": "Red",
					"ratio": 0.24675324675324675
			   },
			   {
					"hex": "#e4b6b8",
					"colorName": "pink_light",
					"colorGeneralCategory": "Red",
					"ratio": 0.36363636363636365
			   },
			   {
					"hex": "#d9a6a6",
					"colorName": "tan",
					"colorGeneralCategory": "Brown",
					"ratio": 0.48888888888888888
			   }
		  ],
		  "styles": [
			   {
					"styleName": "Romantic",
					"confidence": 0.4469371946294496
			   },
			   {
					"styleName": "Elegant",
					"confidence": 0.14566914378339832
			   },
			   {
					"styleName": "Vintage",
					"confidence": 0.11145916723322409
			   }
		  ],
		  "garments": [
			   {
					"typeName": "Skirt",
					"boundingBox": {
						 "x": 170,
						 "y": 303,
						 "w": 297,
						 "h": 301
					},
					"confidence": 0.5021743178367615
			   },
			   {
					"typeName": "Dress",
					"boundingBox": {
						 "x": 174,
						 "y": 140,
						 "w": 293,
						 "h": 465
					},
					"confidence": 0.49173223972320557
			   }
		  ]
	 }
}

color = result['person']['colors']
style = result['person']['styles']
garment = result['person']['garments']

def getBestColours(parent, number):

	ratio = []
	if(len(parent) < number):
		numbers = len(parent)

	for i in range(0, len(parent)):
		ratio.append(parent[i]['ratio'])

	ratio.sort(reverse=True)

	for i in range(0, number):
		print(ratio[i])

def getBestConfidence(parent, number): 
	if(len(parent) < number):
		numbers = len(parent)
 
	confidence = []

	for i in range(0, len(parent)):
		confidence.append(parent[i]['confidence'])
		
	confidence.sort(reverse=True)

	for i in range(0, number):
		print(confidence[i])

getBestColours(color,3)
getBestConfidence(garment, 2)