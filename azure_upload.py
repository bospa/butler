#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os
import sys
import msvcrt
import cv2
import cognitive_face as CF
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess

file_path='capfile.jpg'

def uploader():
    account_name='pictu'
    account_key='' # Replace with valid azure account key
    container_name='pictu'
    service = BlockBlobService(account_name=account_name,account_key=account_key)
    service.create_blob_from_path(container_name,'capfile.jpg',file_path)

def face_capturing():
    KEY = '' # Replace with a valid subscription key (keeping the quotes in place).
    CF.Key.set(KEY)
    BASE_URL = '' # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    capture = cv2.VideoCapture(0)

    print("space key: take a picture")
    print("x key : exit")
    while True:        
        char = ord(msvcrt.getch())
        if char == 26 or char == 120:
            exit()
        if char == 32 or char == 129:
            print("take a picture")
            break
    #camera capturing
    capture = cv2.VideoCapture(0)
    ret, image = capture.read()
    if not ret:
        print('not captured')
        face_capturing()
        return
    cv2.imwrite(file_path,image)
    print("")
    print("success capturing!")
    detect = CF.face.detect(file_path)
    if detect == []:
        print("failed face detecting")
        face_capturing()
        return

if __name__ == '__main__':
    while True:
        face_capturing()
        uploader()
        os.remove(file_path)
