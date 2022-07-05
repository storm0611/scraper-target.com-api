import pyppeteer
import bs4
import asyncio

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

async def scrap_upc_details(target_url):
    product_name = 'Not Found'
    product_price = 'Not Found'
    product_description = 'Not Found'
    product_category = 'Not Found'
    product_upc = 'Not Found'
    product_imageurl = 'Not Found'

    browser = await pyppeteer.launch(handleSIGINT=False,
                                     handleSIGTERM=False,
                                     handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto("https://www.target.com/c/shop-all-categories/-/N-5xsxf")
    content = await page.content()
    # soup = bs4.BeautifulSoup(content, features="lxml")
    # content = soup.select('.bkUrcF')[0]
    soup = bs4.BeautifulSoup(content, features="lxml")
    components = soup.select('data-component-type="Browse - Manual"')
    categories = []
    for comp in components:
        soup = bs4.BeautifulSoup(comp, features="lxml")
        soup = bs4.BeautifulSoup(soup.select(
            'div.children')[0], features="lxml")
        for category in soup.contents:
            category_name = category.a.text
            category_url = category.a['href']
            categories.append({
                'name': category_name,
                'url': category_url
            })
    print(categories)
    await browser.close()
    
    

print(asyncio.run(scrap_upc_details(target_url)))
