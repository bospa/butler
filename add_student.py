import cognitive_face as CF
import cv2
import numpy as np
import sys
import json
import os
import msvcrt

KEY = '' # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
BASE_URL = '' # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

file_path = "capfile.jpg"
teamid = "bbdan"

def getid(name):
    #search personId by name 
    member = CF.person.lists(teamid)
    for mem in member:
        if mem['name'] == name:
            return mem['personId']
    print("new student : create student data")
    CF.person.create(teamid,name)
    return getid(name)
    
name = input("input student name : ")
personid = getid(name)

print("resist " + name + "'s face")
print("space key: take a picture")
print("x key : exit")
print("")
while True:        
    char = ord(msvcrt.getch())
    if char == 26 or char == 120:
        exit()
    if char == 32 or char == 129:
        print("take a picture!")
        break
#camera capturing
capture = cv2.VideoCapture(0)
ret, image = capture.read()
if not ret:
    print('camera not captured')
    exit()
cv2.imwrite(file_path,image)
CF.person.add_face(file_path,teamid,personid)
os.remove(file_path)
