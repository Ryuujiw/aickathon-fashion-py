import csv
import coqnitics
from PIL import Image
import requests
from io import BytesIO
import urllib.request

reader = csv.reader(open('data.csv', newline=''), delimiter=',')
count = 0
for row in reader:
    if row:
        count += 1
        fav_count = row[0]
        urllib.request.urlretrieve(row[1], '{}{}{}'.format('tmp/train', count,'.jpg'))
        coqnitics.requestAPI(count)