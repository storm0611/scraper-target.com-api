from tarfile import CompressionError
import pyppeteer
import bs4
import asyncio
import json
import os

TARGET_HOMEPAGE = "https://www.target.com"
TARGET_ALL_CATEGORIES = "https://www.target.com/c/shop-all-categories/-/N-5xsxf"
TARGET_PRODUCT = "https://www.target.com/p/huggies-little-movers-baby-disposable-diapers-select-size-and-count/-/A-82984217?preselect=53550899#lnk=sametab"
TARGET_BLACK_OWNED = "/c/black-owned-or-founded-brands-at-target/-/N-q8v16"
TARGET_GROCERY = "/c/grocery/-/N-5xt1a"
TARGET_CLOTHING_SHOES_ACESSORIES = "/c/clothing-shoes-accessories/-/N-rdihz"
TARGET_PRIDE = "/c/pride/-/N-5589f?lnk=C_PRIDE_WEB-73285_3"
TARGET_BABY = "/c/baby/-/N-5xtly"
TARGET_HOME = "/c/home/-/N-5xtvd"
TARGET_COLLEGE = "/c/on-to-college/-/N-5q0g0"
TARGET_PATIO_GARDEN = "/c/patio-garden/-/N-5xtq9"
TARGET_FURNITURE = "/c/furniture/-/N-5xtnr"
TARGET_KITCHEN_DINING = "/c/kitchen-dining/-/N-hz89j"
TARGET_TOYS = "/c/toys/-/N-5xtb0"
TARGET_ELECTRONICS = "/c/electronics/-/N-5xtg6"
TARGET_VIDEO_GAMES = "/c/video-games/-/N-5xtg5"
TARGET_MOVIES_MUSIC_BOOKS = "/c/movies-music-books/-/N-5xsxe"
TARGET_SPORTS_OUTDOORS = "/c/sports-outdoors/-/N-5xt85"
TARGET_BEAUTY = "/c/beauty/-/N-55r1x"
TARGET_PERSONAL_CARE = "/c/personal-care/-/N-5xtzq"
TARGET_HEALTH = "/c/health/-/N-5xu1n"
TARGET_PETS = "/c/pets/-/N-5xt44"
TARGET_HOUSEHOLD_ESSENTIALS = "/c/household-essentials/-/N-5xsz1"
TARGET_LUGGAGE = "/c/luggage/-/N-5xtz1"
TARGET_SCHOOL_OFFICE_SUPPLIES = "/c/school-office-supplies/-/N-5xsxr"
TARGET_PARTY_SUPPLIES = "/c/party-supplies/-/N-5xt3c"
TARGET_BULLSEYE_PLAYGROUND = "/c/bullseye-s-playground/-/N-tr36l"
TARGET_GIFT_IDEAS = "/c/gift-ideas/-/N-96d2i"
TARGET_GIFT_CARDS = "/c/gift-cards/-/N-5xsxu"
TARGET_CLEARANCE = "/c/clearance/-/N-5q0ga"


target_url = TARGET_PRODUCT

async def main():
    categories = []
    subcategories = []
    sub_subcategories = []
    products = []
    browser = await pyppeteer.launch(
                                handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False)
    page = await browser.newPage()
    
    # await page.goto("https://www.target.com/c/shop-all-categories/-/N-5xsxf")
    # content = await page.content()
    # soup = bs4.BeautifulSoup(content, features="lxml")
    
    # # start - finding categories list
    # components = soup.select('div[data-component-type="Browse - Manual"]')
    # print(len(components))
    # for comp in components:
    #     # soup = bs4.BeautifulSoup(str(comp), features="lxml")
    #     # soup = bs4.BeautifulSoup(soup.select(
    #     #    'div.children')[0], features="lxml")
    #     try:
    #         children = comp.select('div.children')[0].contents
    #     except:
    #         children = comp.select('ul')[0].contents
    #     print(len(children))
    #     for category in children:
    #         category_name = category.a.text
    #         category_url = category.a['href']
    #         print(category_name, category_url)
    #         categories.append({
    #             'name': category_name,
    #             'url': category_url
    #         })
    
    categories = json.load(open(os.path.join("categories.json")))
    print(categories)
    # jsonString = json.dumps(categories)
    # jsonFile = open("categories.json", "w")
    # jsonFile.write(jsonString)
    # jsonFile.close()
    # end - finding categories list
    
    # start - finding subcategories or products list
    for category in categories:
        category_name = category['name']
        category_url = category['url']
        print(category)
        await page.goto(TARGET_HOMEPAGE + category_url)
        await asyncio.sleep(2)
        content = await page.content()
        soup = bs4.BeautifulSoup(content, features="lxml")
        products_grid = soup.select('div[data-test="product-grid"] section>div')
        # print(len(products_grid))
        if len(products_grid):
        # start - finding products
            # print(soup.select('h2[data-test="resultsHeading"]'))
            try:
                results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" ")[0])
            except:
                continue
            print(results_count)
            cnt = 0
            page_num = 0
            while cnt <= results_count:
                print(category_url + "?Nao=" + str(page_num * 24))
                await page.goto(TARGET_HOMEPAGE + category_url + "?Nao=" + str(page_num * 24))
                await asyncio.sleep(2)
                content = await page.content()
                soup = bs4.BeautifulSoup(content, features="lxml")
                products_grid = soup.select('div[data-test="product-grid"] section>div')
                print(len(products_grid))
                # if not len(products_grid):
                #     content = await page.content()
                #     soup = bs4.BeautifulSoup(content, features="lxml")
                #     products_grid = soup.select('div[data-test="product-grid"] section>div')
                for item in products_grid[0].contents:
                    # print(item)
                    # print(item.text)
                    # print(item.a['href'])
                    # pro = item.select('a[data-test="product-title"]')[0]
                    try:
                        product_name = item.text
                        product_category = category_name
                        product_url = item.a['href']
                    except:
                        continue
                    products.append({
                        "category": product_category,
                        "name": product_name,
                        "url": product_url
                    })
                    print({
                        "category": product_category,
                        "name": product_name,
                        "url": product_url
                    })
                    cnt += 1
                page_num += 1
        # end - finding products
        else:
        # start - finding subcategories
            components = soup.select('div[data-component-type="Browse - Manual"]')
            print(len(components))
            if len(components):
                for comp in components:
                    # soup = bs4.BeautifulSoup(str(comp), features="lxml")
                    # soup = bs4.BeautifulSoup(soup.select(
                    #    'div.children')[0], features="lxml")
                    try:
                        children = comp.select('div.children')[0].contents
                    except:
                        children = comp.select('ul')[0].contents
                    print(len(children))
                    for subcategory in children:
                        subcategory_name = subcategory.a.text
                        subcategory_url = subcategory.a['href']
                        print(subcategory_name, subcategory_url)
                        subcategories.append({
                            'parent': category['name'],
                            'name': subcategory_name,
                            'url': subcategory_url
                        })
            print(subcategories)
            jsonString = json.dumps(subcategories)
            jsonFile = open(category_name + "-subcategories.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
        # end - finding subcategories
    # end - finding subcategories or products list
    if len(subcategories):
    # start - finding products in subcategories
        for category in subcategories:
            category_name = category['parent']
            subcategory_name = category['name']
            subcategory_url = category['url']
            print(category)
            await page.goto(TARGET_HOMEPAGE + subcategory_url)
            await asyncio.sleep(2)
            content = await page.content()
            soup = bs4.BeautifulSoup(content, features="lxml")
            products_grid = soup.select('div[data-test="product-grid"] section>div')
            print(len(products_grid))
            if len(products_grid):
                # start - finding products in subcategories
                results_count = int(soup.select('h2[data-test="resultsHeading"]')[0].text.split(" "))
                print(results_count)
                cnt = 0
                page_num = 0
                while cnt <= results_count:
                    print(subcategory_url + "?Nao=" + str(page_num * 24))
                    await page.goto(TARGET_HOMEPAGE + subcategory_url + "?Nao=" + str(page_num * 24))
                    await asyncio.sleep(2)
                    content = await page.content()
                    soup = bs4.BeautifulSoup(content, features="lxml")
                    products_grid = soup.select('div[data-test="product-grid"] section>div')
                    print(len(products_grid))
                    # if not len(products_grid):
                    #     content = await page.content()
                    #     soup = bs4.BeautifulSoup(content, features="lxml")
                    #     products_grid = soup.select('div[data-test="product-grid"] section>div')
                    for item in products_grid[0].contents:
                        pro = item.select('a[data-test="product-title"]')[0]
                        product_name = pro.text
                        product_category = category_name
                        product_url = pro.get("href")
                        products.append({
                            "category": product_category,
                            "name": product_name,
                            "url": product_url
                        })
                        print({
                            "category": product_category,
                            "name": product_name,
                            "url": product_url
                        })
                        cnt += 1
                    page_num += 1
            # end - finding products in subcategories
            else:
                # start - finding sub-subcategories
                components = soup.select('div[data-component-type="Browse - Manual"]')
                print(len(components))
                if len(components):
                    for comp in components:
                        # soup = bs4.BeautifulSoup(str(comp), features="lxml")
                        # soup = bs4.BeautifulSoup(soup.select(
                        #    'div.children')[0], features="lxml")
                        try:
                            children = comp.select('div.children')[0].contents
                        except:
                            children = comp.select('ul')[0].contents
                        print(len(children))
                        for subcategory in children:
                            subcategory_name = subcategory.a.text
                            subcategory_url = subcategory.a['href']
                            print(subcategory_name, subcategory_url)
                            sub_subcategories.append({
                                'parent': category_name,
                                'name': subcategory_name,
                                'url': subcategory_url
                            })
                print(subcategories)
            # end - finding sub-subcategories
    # end - finding sub-subcategories or products list in subcategories
    if len(sub_subcategories):
        print("sub_subcategories not empty")
    
    # start - get information from products url
    if len(products):
        for product in products:
            print(product)
    # end - get information from products url
    
    await browser.close()
    
    

asyncio.run(main())
