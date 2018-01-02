import os
import exifread
import shutil
import datetime


for file in os.listdir("./fotos"):
    imgPath = os.path.join('./fotos/', file)
    photo = open(imgPath, 'rb')
    tags = exifread.process_file(photo)
    photo.close()
    if 'Image DateTime' in tags.keys():
        date = tags['Image DateTime']
    elif(file.endswith('mp4')):
        date = os.path.getmtime(imgPath)
        date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y:%m:%d')
    else:
        date = os.path.getmtime(imgPath)
        date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y:%m:%d')
    if 'GPS GPSLatitudeRef' in tags.keys():
        gpsLat = tags['GPS GPSLatitude']
        gpsLong = tags['GPS GPSLongitude']
        gpsLatRef = tags['GPS GPSLatitudeRef']
        gpsLongRef = tags['GPS GPSLongitudeRef']

    date = str(date)[0:10].split(':')
    resPath = './result/' + date[0]
    if not os.path.exists(resPath):
        os.makedirs(resPath)
    resPath = resPath + '/' + date[0] + '-' + date[1]
    if not os.path.exists(resPath):
        os.makedirs(resPath)
    resPath = resPath + '/' + date[0] + '-' + date[1] + '-' + date[2]
    if not os.path.exists(resPath):
        os.makedirs(resPath)
    shutil.move(imgPath, resPath + '/' + file)

    if 'gpsLat' in locals():
        print(str(gpsLat) + ' ' + str(gpsLatRef))
        print(str(gpsLong) + ' ' + str(gpsLongRef))
