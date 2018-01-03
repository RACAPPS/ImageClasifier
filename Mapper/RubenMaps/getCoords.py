import sys
import exifread
import os

photo = open(str(sys.argv[1]), 'rb')
tags = exifread.process_file(photo)
photo.close()
if 'GPS GPSLatitudeRef' not in tags.keys():
    os.system('"C:\\Program Files\\RubenMaps\\404.html"')
else:
    gpsLat = tags['GPS GPSLatitude']
    gpsLong = tags['GPS GPSLongitude']
    gpsLatRef = tags['GPS GPSLatitudeRef']
    gpsLongRef = tags['GPS GPSLongitudeRef']
    gpsLat = str(gpsLat).replace('[', '').replace(']', '').split(', ')
    gpsLong = str(gpsLong).replace('[', '').replace(']', '').split(', ')
    gpsLat[2] = gpsLat[2].split('/')
    gpsLat[2] = float(gpsLat[2][0]) / float(gpsLat[2][1])
    gpsLong[2] = gpsLong[2].split('/')
    gpsLong[2] = float(gpsLong[2][0]) / float(gpsLong[2][1])
    gpsLat = float(gpsLat[0]) + float(gpsLat[1])/60 + float(gpsLat[2])/(60*60);
    gpsLong = float(gpsLong[0]) + float(gpsLong[1])/60 + float(gpsLong[2])/(60*60);
    if str(gpsLatRef) == 'S':
        gpsLat *= -1
    if str(gpsLongRef) == 'W':
        gpsLong *= -1
    os.system('start chrome "https://www.google.com/maps/search/?api=1&query=' + str(gpsLat) + ',' + str(gpsLong) + '"')
