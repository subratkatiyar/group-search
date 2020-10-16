import os
import time
import pprint
import platform
from search_index import *
from work_on_index import *
from dictdump4 import *

def creation_date(path_to_file):
    try:
        if platform.system() == 'Windows':
            date =  os.path.getmtime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                date = stat.st_birthtime
            except AttributeError:
                date = stat.st_mtime
        return(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date)))
    except FileNotFoundError:
        return("File not found. Consider reindexing.(Normal index coming soon)")

print("Group Index was last modified on:-",creation_date("group_dictionary.json"))
print("Normal Index was last modified on:-",creation_date("normal_dictionary.json"))

def options():
    print("1.category search (use if you are not sure of file name, or to get every file with particular extension (eg:-.pdf) )")
    print("2.normal search (use if you know the file name with file type (eg test.jpg) )")
    print("3.Usual Search (same as windows search)...under development")
    choice_1 = int(input("Choose 1 or 2:-"))
    if choice_1 == 1:
        print("1.pre defined category search")
        print("2.manual category search")
        option = int(input("Choose 1 or 2:-"))
        if option == 1:
            pre_defined_category_search()
        elif option == 2:
            manual_category_search()

#yet to add a usual search.
        else:
            os.system('cls')
            print("How Hard Is It To Select A Correct Option.")
            options()
    elif choice_1 == 2:
        normal_search()
    else:
        os.system('cls')
        print("How Hard Is It To Select A Correct Option.")
        options()


print("Do you want to index your drive?")
print("1.Yes")
print("2.No")
def index_toggle_confirmation():
    index_toggle = int(input())
    if index_toggle == 1:
        search()
        indexer()
        os.system('cls')
        options()
    elif index_toggle ==2:
        options()
    else:
        print("Either select 1 or 2.")
        index_toggle_confirmation()
index_toggle_confirmation()
