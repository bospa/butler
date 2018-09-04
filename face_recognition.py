# coding: UTF-8
import cognitive_face as CF
import cv2
import json
import msvcrt

def getid(name):
    teamid = "bbdan"
    #search personId by name 
    member = CF.person.lists(teamid)
    for mem in member:
        if mem['name'] == name:
            return mem['personId']
    print(name+" was not found")
    exit()

def face_capturing():

    KEY = '' # Replace with a valid subscription key (keeping the quotes in place).
    CF.Key.set(KEY)
    BASE_URL = '' # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    teamid = "bbdan"
    """
    #create group
    CF.person_group.create(teamid)
    """

    CF.person_group.train(teamid)
    name = input("your name is : ")

    print("")
    print("space key : take a picture")
    print("x key : exit")
    print("")

    while True:
        char = ord(msvcrt.getch())
        if char == 26 or char == 120:
            exit()
        if char == 32:
            print("take a picture")
            break

    #camera capturing
    capture = cv2.VideoCapture(0)
    ret, image = capture.read()
    if not ret:
        print('failed capturing data')
        exit()

    capfile = 'capfile.jpg'
    cv2.imwrite(capfile,image)

    #face detection
    faces = CF.face.detect(capfile)
    if faces == []:
        print('failed caturing')
        exit()

    #search personId by name 
    personid = getid(name)

    verify = CF.face.verify(faces[0]['faceId'],person_group_id=teamid,person_id=personid)
    print(json.dumps(verify,indent=4))

if __name__ == '__main__':
    face_capturing()
