
import json
import os
import datetime
import time
import sqlite3
import requests

API_URL1 = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1"
API_URL2 = "https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1"
API_KEY = "9f36aeafbe60771e321a7cc95a78140772ab3e96"

today = datetime.datetime.today().strftime("%Y-%m-%d")
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

table_name = ""

def insert_into_table(product_info):
    
    global table_name
    
    disc = "0"
    sql_query = "SELECT discount FROM discounts WHERE category_name=" + \
        "'" + product_info['category'] + "'"
    print(sql_query)
    results = cur.execute(sql_query).fetchall()
    # print(results)
    if len(results):
        disc = str(results[0][0])
    sql_query = "SELECT * FROM " + '"' + table_name + '"' + " WHERE tcin=" + \
        "'" + product_info['tcin'] + "'"
    print(sql_query)
    results = cur.execute(sql_query).fetchall()
    if len(results):
        id = results[0][0]
        sql_query = "UPDATE " + '"' + table_name + '"' + " SET " + \
                    "price=" + "'" + product_info['price_min'] + "', " +  \
                    "disc=" + "'" + disc + "', " +  \
                    "update_date=" + "'" + today + "' " +  \
                    " WHERE id=" + str(id)
        print(sql_query)
        cur.execute(sql_query)
        conn.commit()
    else:
        sql_query = 'INSERT INTO ' + '"' + table_name + '"' + ' (url, tcin, name, description, image, category, price, disc, employee, open_date, update_date) ' + \
            " VALUES (" + \
            '"' + product_info['url'] + '", ' + \
            '"' + product_info['tcin'] + '", ' + \
            '"' + product_info['name'] + '", ' + \
            '"' + product_info['description'] + '", ' + \
            '"' + product_info['image'] + '", ' + \
            '"' + product_info['category'] + '", ' + \
            '"' + product_info['price_min'] + '", ' + \
            '"' + disc + '", ' + \
            '"' + product_info['employee'] + '", ' + \
            '"' + today + '", ' + \
            '"' + today + '"' + ");"
        print(sql_query)
        cur.execute(sql_query)
        conn.commit()
    
def get_products_category(categories):
    
    global table_name
    
    count = 24
    products_info = []
    for category in categories:
        print("category=", category)
        category_name = category['name']
        table_name = category_name + "_products"
        table_name = table_name.replace(" ", "")
        print(table_name)
        sql_query = "CREATE TABLE IF NOT EXISTS " + '"' + table_name + '"' + \
                    " ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, " + \
                    "url TEXT," + \
                    "tcin TEXT," + \
                    "upc TEXT," + \
                    "name TEXT," + \
                    "description TEXT," + \
                    "image TEXT," + \
                    "category TEXT," + \
                    "price TEXT," + \
                    "disc TEXT," + \
                    "stock TEXT," + \
                    "employee TEXT," + \
                    "open_date TEXT," + \
                    "update_date TEXT," + \
                    "is_available integer DEFAULT 1," + \
                    "last_sold TEXT," + \
                    "last_price TEXT);"
        print(sql_query)
        cur.execute(sql_query)
        conn.commit()
        category_url = category['url']
        category_id = category_url.split('-')[-1]
        print("category_id=", category_id)
        current_page = total_pages = 1
        total_results = 0
        offset = 0
        cnt = 0
        time_one_page = datetime.timedelta(seconds=0)
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
            if time_one_page.total_seconds() < 5 :
                time.sleep(5 - time_one_page.total_seconds())
            response = requests.get(API_URL1, params=params3)
            # print("category response time=", datetime.datetime.now() - start_time)
            start_time = datetime.datetime.now()
            if response.status_code > 300:
                print("category_requests:", response.status_code)
                time.sleep(5)
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
            if not len(products):
                print("products not found")
                offset += count
                time.sleep(5)
                break
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
                    description = ''.join(str(
                        sub) for sub in product['item']['product_description']['soft_bullets']['bullets'])
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
                if tcin != 'Not Found':
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
            time_one_page = datetime.datetime.now() - start_time
            print("one page time=", time_one_page)
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
        try:
            image = product_info['item']['enrichment']['images']['primary_image_url']
        except:
            image = 'Not Found'
        try:
            url = product_info['item']['enrichment']['buy_url']
        except:
            url = 'Not Found'
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
            "url": url,
            "upc": str(barcode),
            "tcin": str(tcin),
            "name": str(name).replace("\"", ""),
            "description": str(description).replace('"', '\''),
            "image": str(image),
            # "category": category,
            "price_max": str(price_max),
            "price_min": str(price_min),
            # "employee": vender,
        }
    else:
        # print("product time=", datetime.datetime.now() - start_time)
        return {
            "url": 'Not Found',
            "upc": "Not Found",
            "tcin": "Not Found",
            "name": "Not Found",
            "description": "Not Found",
            "image": "Not Found",
            # "category": category,
            "price_max": "Not Found",
            "price_min": "Not Found",
            # "employee": vender,
        }
    

if __name__ == '__main__':
    # upc = input("Enter UPC:")
    # print(get_products_upc(upc))
    categories = json.load(open(os.path.join("categories.json")))
    print(len(get_products_category(categories)))
    conn.close()