import os
import sqlite3
import json

categories = json.load(open(os.path.join("categories.json")))
current_categories = json.load(open(os.path.join("categories.json")))
