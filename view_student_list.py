import cognitive_face as CF
import cv2
import numpy as np
import sys
import json
import os
import msvcrt
import json

KEY = ''  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
BASE_URL = ''  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
file_path = "capfile.jpg"
teamid = "bbdan"

print(json.dumps(CF.person.lists(teamid),ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))
