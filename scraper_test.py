from itertools import starmap
from pandas import ExcelWriter
import pyppeteer
import bs4
import asyncio
import json
import os
import sys
import datetime
import time
import sqlite3
import requests

TARGET_HOMEPAGE = "https://www.target.com"
TARGET_ALL_CATEGORIES = "https://www.target.com/c/shop-all-categories/-/N-5xsxf"
TARGET_PRODUCT = "https://www.target.com/p/huggies-little-movers-baby-disposable-diapers-select-size-and-count/-/A-82984217?preselect=53550899#lnk=sametab"
SEARCH_DATA = "?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=false&include_sponsored=true&keyword=800897004071&offset=0&page=%2Fs%2F800897004071&platform=desktop&pricing_store_id=3991&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F103.0.0.0+Safari%2F537.36&visitor_id=0181DBA81F220201B2C4F5C04CBA071E"
API_URL = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1"
API_KEY = "9f36aeafbe60771e321a7cc95a78140772ab3e96"
UPC_NUMBER = "800897004071"


target_url = TARGET_PRODUCT

# async def update_db():
    
#     conn = sqlite3.connect('mydb.db')
#     cur = conn.cursor()
#     today = datetime.datetime.today().strftime("%Y-%m-%d")
#     # start - get all information of all products from target.com
#     # sys.stdout = open('log.txt', 'w+')
#     print("---------------------------------------------------------------------------------------")
#     print(datetime.datetime.today())
#     print("====================================================================================")

#     categories = []
#     subcategories = []
#     sub_subcategories = []
#     products = []
#     products_count = []
#     browser = await pyppeteer.launch(
#         handleSIGINT=False,
#         handleSIGTERM=False,
#         handleSIGHUP=False)
#     page = await browser.newPage()

#     # await page.goto("https://www.target.com/c/shop-all-categories/-/N-5xsxf")
#     # content = await page.content()
#     # soup = bs4.BeautifulSoup(content, features="lxml")

#     # # start - finding categories list
#     # components = soup.select('div[data-component-type="Browse - Manual"]')
#     # print(len(components))
#     # for comp in components:
#     #     # soup = bs4.BeautifulSoup(str(comp), features="lxml")
#     #     # soup = bs4.BeautifulSoup(soup.select(
#     #     #    'div.children')[0], features="lxml")
#     #     try:
#     #         children = comp.select('div.children')[0].contents
#     #     except:
#     #         children = comp.select('ul')[0].contents
#     #     print(len(children))
#     #     for category in children:
#     #         category_name = category.a.text
#     #         category_url = category.a['href']
#     #         if category_url.find("http") < 0 and category_url.find(".com") < 0:
#     #             category_url = TARGET_HOMEPAGE + category_url                
#     #         print(category_name, category_url)
#     #         categories.append({
#     #             'name': category_name,
#     #             'url': category_url
#     #         })

#     categories = json.load(open(os.path.join("categories.json")))
#     # print("categories=", categories)
#     # jsonString = json.dumps(categories)
#     # jsonFile = open("categories.json", "w")
#     # jsonFile.write(jsonString)
#     # jsonFile.close()
#     # end - finding categories list

#     # start - finding subcategories or products list
#     cnt = 0
#     # for category in categories:
#     #     print("category=", category)
#     #     category_name = category['name']
#     #     category_url = category['url']
#     #     await page.goto(category_url)
#     #     await asyncio.sleep(5)
#     #     content = await page.content()
#     #     soup = bs4.BeautifulSoup(content, features="lxml")
#     #     products_grid = soup.select('div[data-test="product-grid"] section>div')
#     #     print("products_grid find?=", len(products_grid))
#     #     if len(products_grid):
#     #         # start - finding products in category
#     #         print("start - finding products in category")
#     #         # print(soup.select('h2[data-test="resultsHeading"]'))
#     #         try:
#     #             results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#     #         except:
#     #             continue
#     #         print("results_count=", results_count)

#     #         page_num = 0
#     #         while cnt <= results_count:
#     #             try:
#     #                 results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#     #             except:
#     #                 break
#     #             # print(category_url + "?Nao=" + str(page_num * 24))
#     #             await page.goto(category_url + "?Nao=" + str(page_num * 24))
#     #             await asyncio.sleep(5)
#     #             content = await page.content()
#     #             soup = bs4.BeautifulSoup(content, features="lxml")
#     #             products_grid = soup.select('div[data-test="product-grid"] section>div')
#     #             print("products_grid find?=", len(products_grid))
#     #             if not len(products_grid):
#     #                 # content = await page.content()
#     #                 # soup = bs4.BeautifulSoup(content, features="lxml")
#     #                 # products_grid = soup.select('div[data-test="product-grid"] section>div')
#     #                 break
#     #             for item in products_grid[0].contents:
#     #                 # print(item)
#     #                 # print(item.text)
#     #                 # print(item.a['href'])
#     #                 # pro = item.select('a[data-test="product-title"]')[0]
#     #                 try:
#     #                     product_name = item.text
#     #                     product_category = category_name
#     #                     product_url = item.a['href']
#     #                 except:
#     #                     continue
#     #                 if product_url.find("http") < 0 and product_url.find(".com") < 0:
#     #                     product_url = TARGET_HOMEPAGE + product_url
#     #                 products.append({
#     #                     "category": product_category,
#     #                     "name": product_name,
#     #                     "url": product_url
#     #                 })
#     #                 cnt += 1
#     #                 print("product=", cnt,  {
#     #                     "category": product_category,
#     #                     "name": product_name,
#     #                     "url": product_url
#     #                 })
#     #             page_num += 1
#     #             print("page_num=", page_num)
#     #             # if cnt % 1001 >= 1000:
#     #             #     asyncio.sleep(600)
#     #         products_count.append({
#     #             'category': category_name,
#     #             'count': cnt
#     #         })
#     #         print("products_count in this category=", {
#     #             'category': category_name,
#     #             'count': cnt
#     #         })
#     #         print("end - finding products in category")
#     #         # end - finding products in category
#     #     else:
#             # start - finding subcategories
#             # print("start - finding subcategories in category")
#             # components = soup.select('div[data-component-type="Browse - Manual"]')
#             # print("components find?=", len(components))
#             # if len(components):
#             #     for comp in components:
#             #         # soup = bs4.BeautifulSoup(str(comp), features="lxml")
#             #         # soup = bs4.BeautifulSoup(soup.select(
#             #         #    'div.children')[0], features="lxml")
#             #         try:
#             #             children = comp.select('div.children')[0].contents
#             #         except:
#             #             children = comp.select('ul')[0].contents
#             #         print("children_cnt=", len(children))
#             #         for subcategory in children:
#             #             try:
#             #                 subcategory_name = subcategory.a.text
#             #                 subcategory_url = subcategory.a['href']
#             #             except:
#             #                 continue
#             #             if subcategory_url.find("http") < 0 and subcategory_url.find(".com") < 0:
#             #                 subcategory_url = TARGET_HOMEPAGE + subcategory_url
#             #             subcategories.append({
#             #                 'parent': category_name,
#             #                 'name': subcategory_name,
#             #                 'url': subcategory_url
#             #             })
#             #             print("subcategory=", {
#             #                 'parent': category_name,
#             #                 'name': subcategory_name,
#             #                 'url': subcategory_url
#             #             })
#     #         print("end - finding subcategories in category")
#     #         # end - finding subcategories
#     #     # asyncio.sleep(600)

#     # print("end - finding in category")
#     # end - finding subcategories or products list
        
#     subcategories = json.load(open(os.path.join("subcategories.json")))
#     # print("subcategories=", subcategories)
#     # jsonString = json.dumps(subcategories)
#     # jsonFile = open("subcategories.json", "w")
#     # jsonFile.write(jsonString)
#     # jsonFile.close()
    
#     # print("products=", products)
#     # jsonString = json.dumps(products)
#     # jsonFile = open("category-products.json", "w")
#     # jsonFile.write(jsonString)
#     # jsonFile.close()

#     cnt = 0
#     if len(subcategories):
#         # start - finding products in subcategories
#         print("start - finding products in subcategories")
#         for category in subcategories:
#             category_name = category['parent']
#             subcategory_name = category['name']
#             subcategory_url = category['url']
#             print("subcategory=", category)
#             try:
#                 await page.goto(subcategory_url)
#             except:
#                 continue
#             await asyncio.sleep(5)
#             content = await page.content()
#             soup = bs4.BeautifulSoup(content, features="lxml")
#             products_grid = soup.select('div[data-test="product-grid"] section>div')
#             print("products_grid find?=", len(products_grid))
#             if len(products_grid):
#                 # start - finding products in subcategories
#                 print("start - finding products in subcategories")
#                 # print("results text = ", soup.select('h2[data-test="resultsHeading"]')[0].text)
#                 try:
#                     results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#                 except:
#                     continue
#                 print("results_count=", results_count)
#                 page_num = 0
#                 while cnt <= results_count:
#                     try:
#                         results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#                     except:
#                         break
#                     # print(subcategory_url + "?Nao=" + str(page_num * 24))
#                     await page.goto(subcategory_url + "?Nao=" + str(page_num * 24))
#                     await asyncio.sleep(5)
#                     content = await page.content()
#                     soup = bs4.BeautifulSoup(content, features="lxml")
#                     products_grid = soup.select('div[data-test="product-grid"] section>div')
#                     print("products_grid find?=", len(products_grid))
#                     if not len(products_grid):
#                     #     content = await page.content()
#                     #     soup = bs4.BeautifulSoup(content, features="lxml")
#                     #     products_grid = soup.select('div[data-test="product-grid"] section>div')
#                         break
#                     for item in products_grid[0].contents:
#                         # print(item)
#                         # print(item.text)
#                         # print(item.a['href'])
#                         # pro = item.select('a[data-test="product-title"]')[0]
#                         try:
#                             product_name = item.text
#                             product_category = category_name
#                             product_url = item.a['href']
#                         except:
#                             continue
#                         if product_url.find("http") < 0 and product_url.find(".com") < 0:
#                             product_url = TARGET_HOMEPAGE + product_url
#                         products.append({
#                             "category": product_category,
#                             "name": product_name,
#                             "url": product_url
#                         })
#                         cnt += 1
#                         print("product=", cnt, {
#                             "category": product_category,
#                             "name": product_name,
#                             "url": product_url
#                         })
#                     page_num += 1
#                     print("page_num=", page_num)
#                 products_count.append({
#                     "category": category_name,
#                     "count": cnt
#                 })
#                 print("products_count in this subcategory=", {
#                     "category": category_name,
#                     "count": cnt
#                 })
#                 print("end - finding products in subcategories")
#                 # end - finding products in subcategories
#             else:
#                 # start - finding sub-subcategories
#                 print("start - finding sub-subcategories in subcategory")
#                 components = soup.select('div[data-component-type="Browse - Manual"]')
#                 print("components find?=", len(components))
#                 if len(components):
#                     for comp in components:
#                         # soup = bs4.BeautifulSoup(str(comp), features="lxml")
#                         # soup = bs4.BeautifulSoup(soup.select(
#                         #    'div.children')[0], features="lxml")
#                         try:
#                             children = comp.select('div.children')[0].contents
#                         except:
#                             children = comp.select('ul')[0].contents
#                         print("children_cnt=", len(children))
#                         for subcategory in children:
#                             try:
#                                 sub_subcategory_name = subcategory.a.text
#                                 sub_subcategory_url = subcategory.a['href']
#                             except:
#                                 continue
#                             if sub_subcategory_url.find("http") < 0 and sub_subcategory_url.find(".com") < 0:
#                                 sub_subcategory_url = TARGET_HOMEPAGE + sub_subcategory_url
#                             sub_subcategories.append({
#                                 'parent': category_name,
#                                 'subcategory': subcategory_name,
#                                 'name': sub_subcategory_name,
#                                 'url': sub_subcategory_url
#                             })
#                             print("sub_subcategory=", {
#                                 'parent': category_name,
#                                 'subcategory': subcategory_name,
#                                 'name': sub_subcategory_name,
#                                 'url': sub_subcategory_url
#                             })
#                 print("end - finding sub-subcategories in this subcategory")
#                 # end - finding sub-subcategories
#     print("sub_subcategories=", sub_subcategories)
#     jsonString = json.dumps(sub_subcategories)
#     jsonFile = open("sub-subcategories.json", "w")
#     jsonFile.write(jsonString)
#     jsonFile.close()
#     print("end - finding in subcategories")
    
#     print("products=", products)
#     jsonString = json.dumps(products)
#     jsonFile = open("subcategory-products.json", "w")
#     jsonFile.write(jsonString)
#     jsonFile.close()
#     # end - finding sub-subcategories or products list in subcategories
    
#     if len(sub_subcategories):
#         # start - finding products in subcategories
#         print("start - finding products in subcategories")
#         # for category in sub_subcategories:
#         #     category_name = category['parent']
#         #     subcategory_name = category['name']
#         #     subcategory_url = category['url']
#         #     print("subcategory=", category)
#         #     try:
#         #         await page.goto(subcategory_url)
#         #     except:
#         #         continue
#         #     await asyncio.sleep(5)
#         #     content = await page.content()
#         #     soup = bs4.BeautifulSoup(content, features="lxml")
#         #     products_grid = soup.select(
#         #         'div[data-test="product-grid"] section>div')
#         #     print("products_grid find?=", len(products_grid))
#         #     if len(products_grid):
#         #         # start - finding products in sub-subcategories
#         #         print("start - finding products in subcategories")
#         #         try:
#         #             results_count = int(soup.select(
#         #                 'h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#         #         except:
#         #             continue
#         #         print("results_count=", results_count)
#         #         cnt = 0
#         #         page_num = 0
#         #         while cnt <= results_count:
#         #             try:
#         #                 results_count = int(soup.select(
#         #                     'h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
#         #             except:
#         #                 break
#         #             # print(subcategory_url + "?Nao=" + str(page_num * 24))
#         #             await page.goto(subcategory_url + "?Nao=" + str(page_num * 24))
#         #             await asyncio.sleep(5)
#         #             content = await page.content()
#         #             soup = bs4.BeautifulSoup(content, features="lxml")
#         #             products_grid = soup.select(
#         #                 'div[data-test="product-grid"] section>div')
#         #             print("products_grid find?=", len(products_grid))
#         #             # if not len(products_grid):
#         #             #     content = await page.content()
#         #             #     soup = bs4.BeautifulSoup(content, features="lxml")
#         #             #     products_grid = soup.select('div[data-test="product-grid"] section>div')
#         #             for item in products_grid[0].contents:
#         #                 # print(item)
#         #                 # print(item.text)
#         #                 # print(item.a['href'])
#         #                 # pro = item.select('a[data-test="product-title"]')[0]
#         #                 try:
#         #                     product_name = item.text
#         #                     product_category = category_name
#         #                     product_url = item.a['href']
#         #                 except:
#         #                     continue
#         #                 product_url = TARGET_HOMEPAGE + product_url
#         #                 products.append({
#         #                     "category": product_category,
#         #                     "name": product_name,
#         #                     "url": product_url
#         #                 })
#         #                 cnt += 1
#         #                 print("product=", cnt, {
#         #                     "category": product_category,
#         #                     "name": product_name,
#         #                     "url": product_url
#         #                 })
#         #             page_num += 1
#         #             print("page_num=", page_num)
#         #         products_count.append({
#         #             "category": category_name,
#         #             "count": cnt
#         #         })
#         #         print("products_count in this subcategory=", {
#         #             "category": category_name,
#         #             "count": cnt
#         #         })
#         #         print("end - finding products in subcategories")
#         #         # end - finding products in sub-subcategories
#         #     else:
#         #         pass
#     print("end - finding in sub_subcategories")
#     # end - finding sub-subcategories or products list in subcategories

#     # start - get information from products url
#     # if len(products):
#     #     jsonString = json.dumps(products)
#     #     jsonFile = open("products_url.json", "w")
#     #     jsonFile.write(jsonString)
#     #     jsonFile.close()
#     # # end - get information from products url
#     # # products_url = json.load(open(os.path.join("products_url.json")))
#     # # print("products_url=", products_url)
#     # products_url = products
#     # products = []
#     # for item in products_url:
#     #     product_category = item['category']
#     #     # product_name = item['name']
#     #     target_url = item['url']
#     #     # await page.goto(TARGET_HOMEPAGE + target_url)
#     #     # await asyncio.sleep(5)
#     #     # content = await page.content()
#     #     # soup = bs4.BeautifulSoup(content, features="lxml")
#     #     print("def get_price_name(target_url): " + target_url)
#     #     product_name = 'Not Found'
#     #     product_price = 'Not Found'
#     #     product_description = 'Not Found'
#     #     # product_category = 'Not Found'
#     #     product_upc = 'Not Found'
#     #     product_imageurl = 'Not Found'
#     #     if not target_url:
#     #         print("not target_url")
#     #         # return {"upc": product_upc,
#     #         #         "product_name": product_name,
#     #         #         "product_price": product_price.replace('$', ''),
#     #         #         "product_image": product_imageurl,
#     #         #         "product_description": product_description,
#     #         #         "product_category": product_category
#     #         #         }
#     #     else:
#     #         await page.goto(target_url)
#     #         await asyncio.sleep(5)
#     #         content = await page.content()
#     #         soup = bs4.BeautifulSoup(content, features="lxml")
#     #         if len(soup.select('div[data-test="productNotFound"]')):
#     #             products.append({"product_upc": product_upc,
#     #                              "product_url": target_url,
#     #                              "product_name": product_name,
#     #                              "product_price": product_price.replace('$', ''),
#     #                              "product_image": product_imageurl,
#     #                              "product_description": product_description,
#     #                              "product_category": product_category
#     #                              })

#     #             # return {"upc": product_upc,
#     #             #         "product_name": product_name,
#     #             #         "product_price": product_price.replace('$', ''),
#     #             #         "product_image": product_imageurl,
#     #             #         "product_description": product_description,
#     #             #         "product_category": product_category
#     #             #         }
#     #         else:
#     #             price = soup.select('span[data-test="product-random-weight-price"]')
#     #             # print(price)
#     #             if not len(price):
#     #                 await asyncio.sleep(5)
#     #                 content = await page.content()
#     #                 soup = bs4.BeautifulSoup(content, features="lxml")
#     #                 price = soup.select('span[data-test="product-random-weight-price"]')
#     #             if not len(price):
#     #                 products.append({"product_upc": product_upc,
#     #                                  "product_url": target_url,
#     #                                  "product_name": product_name,
#     #                                  "product_price": product_price.replace('$', ''),
#     #                                  "product_image": product_imageurl,
#     #                                  "product_description": product_description,
#     #                                  "product_category": product_category
#     #                                  })
#     #             else:
#     #                 product_price = price[0].text
#     #                 print(product_price)
#     #                 product_name = soup.select('h1[data-test="product-title"] span')[0].text
#     #                 print(product_name)
#     #                 product_upc = soup.find_all("b", string="UPC")[0].parent.text.split(' ')[1]
#     #                 print(product_upc)
#     #                 product_imageurl = soup.select('button[data-test="product-carousel-item-0"] img')[0]['src']
#     #                 print(product_imageurl)
#     #                 # product_category = soup.select('.PWWrr:nth-child(2) > span > a > span')[0].text
#     #                 # print(product_category)
#     #                 product_description = soup.find_all("h3", string="Description")[0].parent.div.text
#     #                 print(product_description)
#     #                 products.append({"product_upc": product_upc,
#     #                                  "product_url": target_url,
#     #                                  "product_name": product_name,
#     #                                  "product_price": product_price.replace('$', ''),
#     #                                  "product_image": product_imageurl,
#     #                                  "product_description": product_description,
#     #                                  "product_category": product_category
#     #                                  })
#     #     print("product=", {"product_upc": product_upc,
#     #                        "product_url": target_url,
#     #                        "product_name": product_name,
#     #                        "product_price": product_price.replace('$', ''),
#     #                        "product_image": product_imageurl,
#     #                        "product_description": product_description,
#     #                        "product_category": product_category
#     #                        })
#     # await browser.close()
#     # # end - get all information of all products from target.com
#     # # insert new product and update old products in database
#     # for product in products:
#     #     product_upc = product["product_upc"]
#     #     product_url = product["product_url"]
#     #     product_name = product["product_name"]
#     #     product_price = float(product["product_price"])
#     #     product_imageurl = product["product_image"]
#     #     product_description = product["product_description"]
#     #     product_category = product["product_category"]
#     #     if product_upc == 'Not Found':
#     #         # current product is unavailable
#     #         sql_query = "SELECT * FROM products WHERE url=" + "'" + product_url + "'"
#     #         if len(cur.execute(sql_query).fetchall()):
#     #             # it is existed in database
#     #             sql_query = "UPDATE products SET " + \
#     #                 "update_date=" + "'" + today + "', " +  \
#     #                 "close_date=" + "'" + today + "', " +  \
#     #                 "is_available=0" + ", " +  \
#     #                 " WHERE url=" + "'" + product_url + "'"
#     #             print(sql_query)
#     #             cur.execute(sql_query)
#     #             conn.commit()
#     #         else:
#     #             # it is not existed in database
#     #             sql_query = "INSERT INTO products " + \
#     #                         " (url, upc, name, description, image, price, category, open_date, update_date, close_cate, is_available) VALUES (" + \
#     #                         "'" + product_url + "', " + \
#     #                         '"' + product_upc + '", ' + \
#     #                         '"' + product_name + '", ' + \
#     #                         '"' + product_description + '", ' + \
#     #                         "'" + product_imageurl + "', " + \
#     #                         str(product_price) + ", " + \
#     #                         '"' + product_category + '", ' + \
#     #                         '"' + today + '", ' + \
#     #                         '"' + today + '", ' + \
#     #                         '"' + today + '", ' + \
#     #                         '0);'
#     #             print(sql_query)
#     #             cur.execute(sql_query)
#     #             conn.commit()
#     #     else:
#     #         # current product is available
#     #         sql_query = "SELECT * FROM products WHERE upc=" + "'" + product_upc + "'"
#     #         if len(cur.execute(sql_query).fetchall()):
#     #             # it is existed in database
#     #             sql_query = "UPDATE products SET " + \
#     #                         "name=" + "'" + product_name + "'" + ", " + \
#     #                         "description=" + "'" + product_description + "'" + ", " + \
#     #                         "image=" + "'" + product_imageurl + "', " +  \
#     #                         "category=" + "'" + product_category + "', " +  \
#     #                         "price=" + str(product_price) + ", " +  \
#     #                         "update_date=" + "'" + today + "', " +  \
#     #                         " WHERE upc=" + "'" + product_upc + "'"
#     #             print(sql_query)
#     #             cur.execute(sql_query)
#     #             conn.commit()
#     #         else:
#     #             # it is not existed in database = new data
#     #             sql_query = "INSERT INTO products " + \
#     #                         " (url, upc, name, description, image, price, category, open_date, update_date) VALUES (" + \
#     #                         "'" + product_url + "', " + \
#     #                         '"' + product_upc + '", ' + \
#     #                         '"' + product_name + '", ' + \
#     #                         '"' + product_description + '", ' + \
#     #                         "'" + product_imageurl + "', " + \
#     #                         str(product_price) + ", " + \
#     #                         '"' + product_category + '", ' + \
#     #                         '"' + today + '", ' + \
#     #                         '"' + today + '"' + \
#     #                         ');'
#     #             print(sql_query)
#     #             cur.execute(sql_query)
#     #             conn.commit()

#     conn.close()


# asyncio.run(update_db())
API_URL1 = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1"
API_URL2 = "https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1"
API_KEY = "9f36aeafbe60771e321a7cc95a78140772ab3e96"

today = datetime.datetime.today().strftime("%Y-%m-%d")

def insert_into_table(product_info):
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    sql_query = "SELECT * FROM products WHERE tcin=" + \
        "'" + product_info['tcin'] + "' or name=" + \
        '"' + product_info['name'] + '"'
    print(sql_query)
    results = cur.execute(sql_query).fetchall()
    if len(results):
        id = results[0][0]
        sql_query = "UPDATE products SET " + \
                    "price=" + "'" + product_info['price_min'] + "', " +  \
                    "update_date=" + "'" + today + "' " +  \
                    " WHERE id=" + str(id)
        print(sql_query)
        cur.execute(sql_query)
        conn.commit()
    else:
        sql_query = 'INSERT INTO products (url, tcin, upc, name, description, image, category, price, employee, open_date, update_date) ' + " VALUES (" + '"' + product_info['url'] + '", ' + '"' + product_info['tcin'] + '", ' + '"", ' + '"' + product_info['name'] + '", ' + '"' + product_info['description'] + '", ' + '"' + product_info['image'] + '", ' + '"' + product_info['category'] + '", ' + '"' + product_info['price_min'] + '", ' + '"' + product_info['employee'] + '", ' + '"' + today + '", ' + '"' + today + '"' + ");"
        print(sql_query)
        cur.execute(sql_query)
        conn.commit()
    
def get_products_category(categories):
    
    count = 28
    products_info = []
    for category in categories:
        print("category=", category)
        category_name = category['name']
        category_url = category['url']
        category_id = category_url.split('-')[-1]
        print("category_id=", category_id)
        current_page = total_pages = 1
        total_results = 0
        offset = 0
        cnt = 0
        while current_page <= total_pages:
            if cnt > total_results:
                break
            params3 = {
                "key": API_KEY,
                "category": category_id,
                "channel": "WEB",
                "count": str(count),
                "default_purchasability_filter": "false",
                "include_sponsored": "true",
                "offset": str(offset),
                "page": "%2Fs%2F" + category_id,
                "platform": "desktop",
                "pricing_store_id": "3991",
                "useragent": "Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F103.0.0.0+Safari%2F537.36",
                "visitor_id": "0181DBA81F220201B2C4F5C04CBA071E"
            }
            # start_time = datetime.datetime.now()
            response = requests.get(API_URL1, params=params3)
            # print("category response time=", datetime.datetime.now() - start_time)
            start_time = datetime.datetime.now()
            time.sleep(3)
            if response.status_code > 300:
                print("category_requests:", response.status_code)
                break
            searched = response.json()['data']['search']
            overview = searched['search_response']["typed_metadata"]
            print("overview=", overview)
            current_page = overview['current_page']
            offset = overview['offset']
            total_pages = overview['total_pages']
            total_results = overview['total_results']
            products = searched['products']
            print("len(products)=", len(products))
            for product in products:
                try:
                    url = product['item']['enrichment']['buy_url']
                except:
                    url = 'Not Found'
                try:
                    image = product['item']['enrichment']['images']['primary_image_url']
                except:
                    image = 'Not Found'
                try:
                    vender = product['item']['product_vendors'][0]['vendor_name']
                except:
                    vender = 'Not Found'
                try:
                    name = product['item']['product_description']['title']
                except:
                    name = 'Not Found'
                try:
                    description = ''.join(str(sub) for sub in product['item']['product_description']['soft_bullets']['bullets'])
                except:
                    description = 'Not Found'
                try:
                    tcin = product['tcin']
                except:
                    tcin = 'Not Found'
                try:
                    price_min = product['price']['current_retail']
                except:
                    price_min = 'Not Found'
                    
                # tcin_results = get_products_tcin(tcin)
                # if isinstance(tcin_results, int) and tcin_results > 300:
                #     break
                
                products_info.append({
                    "url": str(url),
                    # "upc": tcin_results['upc'],
                    "tcin": str(tcin),
                    # "name": tcin_results['name'],
                    # "description": tcin_results['description'],
                    "name": str(name).replace("\"", " "),
                    "description": str(description).replace('"', '\''),
                    "image": str(image),
                    "category": str(category_name),
                    # "price_max": str(tcin_results['price_max']),
                    # "price_min": str(tcin_results['price_min']),
                    "price_min": str(price_min),
                    "employee": str(vender),
                })
                insert_into_table(products_info[-1])
                print("product_info = ", products_info[-1])
                cnt += 1
            offset += count
            print("category time=", datetime.datetime.now() - start_time)
    return(products_info)        
   
def get_products_tcin(tcin):
    params2 = {
        "key": API_KEY,
        "tcin": str(tcin),
        "is_bot": "false",
        "member_id": "0",
        "pricing_store_id": "3991",
        "has_pricing_store_id": "true",
        "has_financing_options": "true",
        "visitor_id": "0181DBA81F220201B2C4F5C04CBA071E",
        "has_size_context": "true",
        "latitude": "50.130",
        "longitude": "8.670",
        "zip": "60323",
        "state": "HE",
        "channel": "WEB",
        "page": "%2Fp%2FA-" + str(tcin)
    }
    # start_time = datetime.datetime.now()
    response = requests.get(API_URL2, params=params2)
    # print("product response time=", datetime.datetime.now() - start_time)
    start_time = datetime.datetime.now()
    time.sleep(3)
    if response.status_code > 300:
        print("tcin_requests:", response.status_code)
        return response.status_code
    product_info = response.json()['data']['product']
    if len(product_info):
        print("len(tcin_product_info)=", len(product_info))
        try:
            children = product_info['children']
            for child in children:
                if child['tcin'] == str(tcin):
                    barcode = child['item']['primary_barcode']
                    break
                else:
                    barcode = 'Not Found'
        except:
            barcode = "Not Found"
        # category_id = product_info['category']['parent_category_id']
        # barcode = upc
        try:
            name = product_info['item']['product_description']['title']
        except:
            name = 'Not Found'
        try:
            description = product_info['item']['product_description']['downstream_description']
        except:
            description = 'Not Found'
        # vender = product_info['item']['product_vendors']['vendor_name']
        try:
            price_max = product_info['price']['reg_retail_max']
        except:
            price_max = 'Not Found'
        try:
            price_min = product_info['price']['reg_retail_min']
        except:
            price_min = 'Not Found'
        # print("product info=", {
        #     "url": url,
        #     "upc": barcode,
        #     "tcin": tcin,
        #     "name": name,
        #     "description": description,
        #     "image": image,
        #     "category": category,
        #     "price_max": price_max,
        #     "price_min": price_min,
        #     # "employee": vender,
        # })
        # print("product time=", datetime.datetime.now() - start_time)
        return {
            # "url": url,
            "upc": str(barcode),
            "tcin": str(tcin),
            "name": str(name).replace("\"", ""),
            "description": str(description).replace('"', '\''),
            # "image": image,
            # "category": category,
            "price_max": str(price_max),
            "price_min": str(price_min),
            # "employee": vender,
        }
    else:
        # print("product time=", datetime.datetime.now() - start_time)
        return {
            # "url": url,
            "upc": "Not Found",
            "tcin": "Not Found",
            "name": "Not Found",
            "description": "Not Found",
            # "image": image,
            # "category": category,
            "price_max": "Not Found",
            "price_min": "Not Found",
            # "employee": vender,
        }
    
def get_tcin_upc(upc):
    params1 = {
        "key": API_KEY,
        "channel": "WEB",
        "count": "24",
        "default_purchasability_filter": "false",
        "include_sponsored": "true",
        "keyword": str(upc),
        "offset": "0",
        "page": "%2Fs%2F" + str(upc),
        "platform": "desktop",
        "pricing_store_id": "3991",
        "useragent": "Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F103.0.0.0+Safari%2F537.36",
        "visitor_id": "0181DBA81F220201B2C4F5C04CBA071E"
    }
    response = requests.get(API_URL1, params=params1)
    if response.status_code > 300:
        print("upc_requests:", response.status_code)
        return response.status_code
    searched = response.json()['data']['search']
    # print(searched)
    products = searched['products']
    try:
        category = searched['search_response']['facet_list'][0]['details'][0]['display_name']
    except:
        category = "Not Found"
    print("len(products)=", len(products))
    if len(products):
        for product in products:
            try:
                tcin = product['tcin']
            except:
                tcin = "Not Found"
            return {
                'tcin': str(tcin),
                'category': str(category).replace('"', "'")
            }
    else:
        return {
            'tcin': "Not Found",
            'category': "Not Found"
        }
    
def get_products_upc(upc):
    params1 = {
        "key": API_KEY,
        "channel": "WEB",
        "count": "24",
        "default_purchasability_filter": "false",
        "include_sponsored": "true",
        "keyword": str(upc),
        "offset": "0",
        "page": "%2Fs%2F" + str(upc),
        "platform": "desktop",
        "pricing_store_id": "3991",
        "useragent": "Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F103.0.0.0+Safari%2F537.36",
        "visitor_id": "0181DBA81F220201B2C4F5C04CBA071E"
    }
    response = requests.get(API_URL1, params=params1)
    if response.status_code > 300:
        print("upc_requests:", response.status_code)
        return response.status_code
    searched = response.json()['data']['search']
    # print(searched)
    products = searched['products']
    category = searched['search_response']['facet_list'][0]['details'][0]['display_name']
    for product in products:
        url = product['item']['enrichment']['buy_url']
        image = product['item']['enrichment']['images']['primary_image_url']
        tcin = product['tcin']
        params2 = {
            "key": API_KEY,
            "tcin": str(tcin),
            "is_bot": "false",
            "member_id": "0",
            "pricing_store_id": "3991",
            "has_pricing_store_id": "true",
            "has_financing_options": "true",
            "visitor_id": "0181DBA81F220201B2C4F5C04CBA071E",
            "has_size_context": "true",
            "latitude": "50.130",
            "longitude": "8.670",
            "zip": "60323",
            "state": "HE",
            "channel": "WEB",
            "page": "%2Fp%2FA-" + str(tcin)
        }
        response = requests.get(API_URL2, params=params2)
        if response.status_code > 300:
            print("tcin_requests:", response.status_code)
            return response.status_code
        product_info = response.json()['data']['product']
        category_id = product_info['category']['parent_category_id']
        barcode = upc
        name = product_info['item']['product_description']['title']
        try:
            description = product_info['item']['product_description']['downstream_description']
        except:
            description = product_info['item']['product_description']['soft_bullet_description']
            
        # vender = product_info['item']['product_vendors']['vendor_name']
        price_max = product_info['price']['reg_retail_max']
        price_min = product_info['price']['reg_retail_min']
        # print("product info=", {
        #     "url": url,
        #     "upc": barcode,
        #     "tcin": tcin,
        #     "name": name,
        #     "description": description,
        #     "image": image,
        #     "category": category,
        #     "price_max": price_max,
        #     "price_min": price_min,
        #     # "employee": vender,
        # })
        return {
            "url": url,
            "upc": barcode,
            "tcin": tcin,
            "name": name,
            "description": description,
            "image": image,
            "category": category,
            "price_max": price_max,
            "price_min": price_min,
            # "employee": vender,
        }


if __name__ == '__main__':
    # upc = input("Enter UPC:")
    # print(get_products_upc(upc))
    categories = json.load(open(os.path.join("categories.json")))
    print(len(get_products_category(categories)))