import os
import json


def indexer():
    count = 0
    dict = {}
    with open("temp.txt",'r',encoding="utf-8") as a_file:
        for line in a_file:
            count+=1

            line  =(line[1:len(line)-2])
            line.replace("(","")
            line.replace(")","")
            folder_start = line.find("[")
            folder_end = line.find("]")

            location = line[1:folder_start-3]
            folder_list = line[folder_start+1:folder_end].split(",")
            files_list = line[folder_end+4:-1].split(",")
            for i in files_list:
                i = i.strip()
                filename, file_extension = os.path.splitext(i[1:-1])
                file_extension = file_extension.lower()
                if location.endswith("//") or location.endswith("\\"):
                    temp_location = location+i[1:-1]
                else:
                    temp_location = location+'//'+i[1:-1]
                temp_location = temp_location.replace("\\","//")
                temp_location = temp_location.replace("\\\\","//")
                temp_location = temp_location.replace("////","//")
                print(temp_location)
                if file_extension not in dict:
                    dict[file_extension] = [temp_location]
                elif file_extension in dict:
                    dict[file_extension].append(temp_location)
    a_file = open("group_dictionary.json", "w")
    json.dump(dict, a_file)
    a_file.close()
    print(dict)
