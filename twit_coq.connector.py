import csv
import coqnitics
from PIL import Image
import requests
from io import BytesIO
import urllib.request
from func import function

reader = csv.reader(open('data.csv', newline=''), delimiter=',')
count = 0
for row in reader:
    if row:
        count += 1
        fav_count = row[0]
        created_at = row[2]
        urllib.request.urlretrieve(row[1], '{}{}{}'.format('tmp/train', count,'.jpg'))
        result = coqnitics.requestAPI(count)

        # GETTERS
        colors = function.getBestColours(result['person']['colors'], 3)
        styles = function.getBestStyles(result['person']['styles'], 3) # for styles
        confidence = function.getBestGarments(result['person']['confidence'], 1)

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






