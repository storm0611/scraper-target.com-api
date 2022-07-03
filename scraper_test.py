from attr import attr
from bs4 import BeautifulSoup
from urllib.request import urlopen

TARGET_HOME = "https://www.target.com"
TARGET_ALL_CATEGORIES = "https://www.target.com/c/shop-all-categories/-/N-5xsxf"
TARGET_PRODUCT = "https://www.target.com/p/huggies-little-movers-baby-disposable-diapers-select-size-and-count/-/A-82984217?preselect=53550899#lnk=sametab"

target_url = TARGET_ALL_CATEGORIES

page = urlopen(target_url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
items = soup.select("div.h-padding-h-tight")
file = open('html.txt', 'rw', encoding='uft-8')
file.write(items)

