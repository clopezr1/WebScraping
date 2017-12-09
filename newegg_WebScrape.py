from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

steam_Url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&bop=And&PageSize=96&order=BESTMATCH'

# Opens connections, grabs page
uClient = uReq(steam_Url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product on page
containers = page_soup.find_all("div", {"class": "item-container"})
print(len(containers))
filename = "products.csv"
f = open(filename, "w")

headers = "Brand, Product_name, Price, Shipping\n\n"

f.write(headers)

# loops through each product and returns details
for container in containers:
    brand_container = container.find_all("a", {"class": "item-brand"})
    brand = brand_container[0].img["title"]

    title_container = container.find_all("a", {"class": "item-title"})
    product_name = title_container[0].text

    price_container = container.find_all("li", {"class": "price-current"})
    price = price_container[0].strong.text + price_container[0].sup.text

    shipping_container = container.find_all("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(brand.replace(","," ") + "," + product_name.replace(",", "|") + "," + "$ " + price.replace(",","'") + "," + shipping + "\n")

f.close()
