import os
import json

def search():
    print("Enter the drive character. eg. S,P,C")
    drive_letter = input()
    path = drive_letter.upper() + ":\\" #change to your directory.
    temp_1 = open("temp.txt",'w',encoding="utf-8")
    for f in os.walk(path):
        print("Currently Indexing:-",f[0])
        temp_1.write(str(f))
        temp_1.write("\n")
