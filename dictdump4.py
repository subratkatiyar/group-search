import os
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
def pre_defined_category_search():
    path="category-complete"
    temp = os.listdir(path)
    count = 0
    for category in temp:
        count+=1
        print("{0}.{1}".format(count,category.replace('.json','')))

    a = int(input("Enter your choice, eg:- 15 for documents "))
    os.system('cls')
    print("The formats in ",temp[a-1].replace('.json',''),'includes:-')

    with open(path+"\\"+temp[a-1],'r') as inf:
        file_formats = eval(inf.read())
    pp.pprint(file_formats)

    with open('group_dictionary.json','r') as inf:
        dict_from_file = eval(inf.read())

    for format_type in file_formats:
        try:
            internal_counter = 0
            for file in dict_from_file["."+format_type.lower()]:
                internal_counter+=1
                print("{0}.{1}".format(internal_counter,file[file.rfind("//")+2:]))

        except:
            print("No {0} files found".format(format_type))

def manual_category_search():
    print("Enter the file extension to search for (eg. .pdf or .mp4)")
    file_format = input()
    with open('group_dictionary.json','r') as inf:
        dict_from_file = eval(inf.read())

    internal_counter = 0
    for file in dict_from_file[file_format]:
        internal_counter+=1
        print("{0}.{1}".format(internal_counter,file[file.rfind("//")+2:]))

def normal_search():
    os.system('cls')
    print("Enter the complete file name along with extension.")
    file_name = input()
    with open('group_dictionary.json','r') as inf:
        dict_from_file = eval(inf.read())
    filename, file_extension = os.path.splitext(file_name)
    try:
        temp_list = (dict_from_file[file_extension])
    except KeyError:
        print("No files with the following extensions were found.")
    file_path_found = [x for x in temp_list if re.search(file_name, x)]
    internal_counter = 0
    if len(file_path_found) == 0:
        print("No files with the same name was found.")
        print("printing all files with same extension.")
        for similar_files in temp_list:
            internal_counter += 1
            print("{0}.{1}".format(internal_counter,similar_files[similar_files.rfind("//")+2:]))
    else:
        print("File found at:-",file_path_found)
