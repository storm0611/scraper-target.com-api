import os
import sqlite3
import json

categories = json.load(open(os.path.join("categories.json")))
current_categories = json.load(open(os.path.join("current.json")))
f = open("extra.txt", "w")
cnt = 0
for category in categories:
    category_name = category['name'].replace("\u2019s", "")
    catetory_name = category_name.replace("\u2019", "")
    if not category_name in current_categories:
        f.write(category_name + "\n")
        cnt += 1
        
print(cnt)