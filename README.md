# Group-Search
This is a group based search designed on python, which allows for searching in groups instead of a particular key term.

## When do I use it??
Imagine a scenario you want to search for multiple files, or search for document and you cannot rememember the name, or just to figure out how many documents do I have?
This is what the code can do.\
:white_check_mark:1. Searching for all pdf or jpg files.\
:white_check_mark:2. can also be used for such a large group of extensions at once, these extensions are pre defined in various categories in categories complete folder.\
:x:3. Normal search (like a normal windows search).....(Still in development).

## How does the code work??
The search is done by indexing a complete directory, and storing the results in a dictionary. The dictionary file is dumped in a .json file (Not the best way, but I am working on it.) The indexing usually takes 4-5 mins, but is dependent on the size and the number of files present in directory. As of right now we can only index and search on any single partition of harddisk, searching on a different partition will require to reindex and the old index is lost. That said, you can save different copies of this code for diiferent partitions. 
## How do I run the code??
The code can be run by simply running the main_search(RUN ME).py file.
> ### Dependencies used. (It should all preinstalled, just for good measures)
>- import pprint (pip install pprint.)
>- import platform (should be preinstalled.)
>- import re (re is a built-in module,so no need to install)
>- import json (json is a built-in module,so no need to install)
>- import os (OS is python's standard library, so no need to install)
>- import time (time is python's standard library, so no need to insatll)

## Various Parts of Program:
- ### The code shows when the last time the drive was indexed and also provides with an option to reindex.
![image of command prompt](https://drive.google.com/uc?export=view&id=1xMpLrFeFifir5CBtscdCkbF_zwJUnNmY)
>* Indexing :- It takes some time, it basically creates a dictionary of any particular partition. Runtime is usually dependent on the number of files and also the used space of the partiton. More space used, more time spent on indeixng. (It took me 2 mins to index 542 GB files.) 
>* Using an old index is possible if you want to search for files which were created before the last time you indexed. Having a rough idea if the file was created before you indexed the last time is always helpful.
 - ### After indexing is completed or being skipped.
![image of command prompt](https://drive.google.com/uc?export=view&id=1m2oFwLezpHP6MFC3oW0WdQg9-PzqA79a)
>* Category Search :- Main use case scenario is when you want to search for every file with the same extension or from a group of predefined extensions.The predefined extensions can be chnaged in the category-complete folder.\
>* Normal Search :- It can be used when we know the exact file name, if the directory is already indexed the search is generally completed within few seconds.
>* Usual Search :- (Work in Progress) It will provide the same flexibility as windows search provide.

## Limited User Base.
* [gaganyadav80](https://github.com/gaganyadav80)
* Hopefully someone else.
