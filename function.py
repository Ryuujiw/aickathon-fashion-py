from db import mydb

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

    return ratio
        

def getBestConfidence(parent, number): 
    if(len(parent) < number):
        numbers = len(parent)
 
    confidence = []

    for i in range(0, len(parent)):
        confidence.append(parent[i]['confidence'])
        
    confidence.sort(reverse=True)
    return confidence


x = int(input())
y = int(input())
z = int(input())

color_name = []
color_ratio = getBestColours(color,x)
for i in range (len(color_ratio)):
    for w in range(x):
        if(color_ratio[i] == color[w]['ratio']):
            color_name.append(color[w]['colorName'])


style_name = []
style_confidence = getBestConfidence(style,y)
for i in range (len(style_confidence)):
    for w in range (y):
        if(style_confidence[i] == style[w]['confidence']):
            style_name.append(style[w]['styleName'])


garment_name = []
garment_confidence = getBestConfidence(garment, z)
for i in range (len(garment_confidence)):
    for w in range (z):
        if(garment_confidence[i] == garment[w]['confidence']):
            garment_name.append(garment[w]['typeName'])


data_insert = []
for i in range (0,3):
    try:
        data_insert.append(color_name[i])
    except IndexError:
        data_insert.append('')
for i in range (0,3):
    try:
        data_insert.append(style_name[i])
    except IndexError:
        data_insert.append('')
for i in range (0,1):
    try:
        data_insert.append(garment_name[i])
    except IndexError:
        data_insert.append('')

        
mycursor = mydb.cursor()
sql = "INSERT INTO tbl_clothe (Colour1, Colour2, Colour3, Style1, Style2, Style3, Garment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val= (data_insert)
mycursor.execute(sql, val)
    
mydb.commit()
print(mycursor.rowcount, "record inserted.")