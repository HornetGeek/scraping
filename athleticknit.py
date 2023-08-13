import requests
from bs4 import BeautifulSoup
import time
import json
import csv
import html

url ="https://www.athleticknit.com/sportswear/cycling" 


apikey =  '5b622f9390ac2b6ccabb1f5cc946ec9bd3a94578' #'083f286c86d9a799b98a0e845f0a0f47023c38c5'
apikey2 = "5e8200c84ae5debc0a1e17dcf80d520dcfedf657" #'02978353e8421ab1b5ce6b749b7237f676c951f4'
apikey3 = "314adf425fca4a4b17c1a1e923f8a362e8cf04d2"


params = {
    'url': url,
    'apikey': apikey,
	'js_render': 'true',
	'js_instructions': """[
        {"wait":1000},
        {"scroll_y":5000},
        {"wait":5000},
        {"scroll_y":6000},
        {"wait":5000},
        {"click":"#showmore_series_1_subseries-container_4"},
        {"scroll_y":7000},
        {"click":"#showmore_series_1_subseries-container_0"},
        {"wait":3000},
        {"click":"#showmore_series_1_subseries-container_3"},
        {"scroll_y":8000},
        {"scroll_y":9000},
        {"click":"#showmore_series_2_subseries-container_4"},
        {"wait":3000},
        {"click":"#showmore_series_1_subseries-container_2"},
        {"scroll_y":10000},
        {"click":"#showmore_series_15_subseries-container_2"},
        {"wait":5000},
        {"click":"#showmore_series_1_subseries-container_8"},
        {"wait":2000},
        {"click":"#showmore_series_2_subseries-container_1"},  
        {"scroll_y":11000},
        {"click":"#showmore_series_1_subseries-container_6"},
        {"wait":200},
        {"scroll_y":12000},
        {"click":"#showmore_series_2_subseries-container_2"},
        {"wait":200},
        {"scroll_y":13000},
        {"click":"#showmore_series_2_subseries-container_6"},
        {"wait":200},
        {"scroll_y":14000},
        {"click":"#showmore_series_2_subseries-container_8"},
        {"wait":200},
        {"scroll_y":15000},
        {"click":"#showmore_series_3_subseries-container_1"},
        {"wait":200},
        {"scroll_y":16000},
        {"click":"#showmore_series_3_subseries-container_2"},
        {"wait":200},
        {"scroll_y":17000},
        {"click":"#showmore_series_3_subseries-container_4"},
        {"scroll_y":18000},
        {"click":"#showmore_series_3_subseries-container_5"},
        {"wait":200},
        {"scroll_y":19000},
        {"click":"#showmore_series_4_subseries-container_0"},
        {"wait":200},
        {"scroll_y":20000},
        {"click":"#showmore_series-container_12"},
        {"wait":200},
        {"scroll_y":21000},
        {"click":"#showmore_series_15_subseries-container_0"},
        {"wait":200},
        {"scroll_y":22000},
        {"click":"#showmore_series_15_subseries-container_1"},
        {"scroll_y":23000},
        {"wait":200},
        {"click":"#showmore_series-container_c_1"},
        {"scroll_y":24000},
        {"click":"#showmore_series-container_c_2"},
        {"scroll_y":25000},
        {"wait":200},
        {"scroll_y":26000},
        {"scroll_y":27000},
        {"wait":200},
        {"scroll_y":28000},
        {"scroll_y":29000},
        {"wait":200},
        {"scroll_y":30000},
        {"scroll_y":31000},
        {"wait":200},
        {"scroll_y":32000},
        {"wait":200},
        {"scroll_y":33000},
        {"wait":200},
        {"scroll_y":43000},
        {"wait":200},
        {"scroll_y":53000},
        {"wait":200},
        {"scroll_y":63000},
        {"wait":500},
        {"scroll_y":83000},
        {"wait":500},
        {"scroll_y":103000},
        {"wait": 200}

        ]""",
	'premium_proxy': 'true',
	'proxy_country': 'us',
    #'antibot': 'true',
    #'wait_for': '#series_1_subseries-container_0 > div:nth-child(2)',
}
used_api = []
page = requests.get("https://api.zenrows.com/v1/",  params=params)

if "apikey has no more credits remaining" in page.text:
    used_api.append(apikey)

    if apikey in used_api:
        print("You have no more credits for Apikey 1")
        if apikey2 in used_api:
            print("You have no more credits for Apikey 2")
            params['apikey'] = apikey3
            apikey = apikey3
        else:
            params['apikey'] = apikey2
            apikey = apikey2

    page = requests.get("https://api.zenrows.com/v1/",  params=params)
    if "apikey has no more credits remaining" in page.text:
        print("You have no more credits for Apikey 2")

        params['apikey'] = apikey3
        apikey = apikey3
        page = requests.get("https://api.zenrows.com/v1/",  params=params)


soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="instant-search-results-container")
products =  results.find_all("div", class_="product-item")                #results.find_all("h4", class_="result-sub-content")


with open('result_athletichnit.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Parent_SKU','Item_SKU', 'Item_Name', 'Item_Description', 'Category', 'Cost', 'Currency', 'Main_Image_URL','Variation_Theme', 'Color','Size'])


for product in products:
    try:
        product_name = product['data-name']
        #print(str.lower(product['data-categories'].split("///")[2][1:-1]).replace(' ','-'))
        url_dir = str.lower(product['data-categories'].split("///")[2]).strip().replace(' ','-')
        url = "https://www.athleticknit.com/{}/".format(url_dir) + str.lower(product_name)
        print(url)
        print(product_name)
        
        params = {
        'url': url,
        'apikey': apikey,
        'js_render': 'true',
        'wait_for': '#product-price-content > div > table',
        'js_instructions': """[{"wait":2000}]"""
        }

        product_page = requests.get('https://api.zenrows.com/v1/', params=params)
        #print(product_page.content)
        if "apikey has no more credits remaining" in product_page.text:
            used_api.append(apikey)
            if apikey3 not in used_api:
                if apikey in used_api:
                    print("You have no more credits for Apikey 1")
                    if apikey2 in used_api:
                        print("You have no more credits for Apikey 2")
                        params['apikey'] = apikey3
                        apikey = apikey3
                    else:
                        params['apikey'] = apikey2
                        apikey = apikey2
            product_page = requests.get("https://api.zenrows.com/v1/",  params=params)
        soup = BeautifulSoup(product_page.content, "html.parser")
        #print(product_page.content)
        time.sleep(.7)
        image = soup.find('meta', {"property":"og:image"}) #magnifier-item-0-large  #gallery-placeholder__image  product-image-photo
        #sizes = soup.find("table", {"class":"table-size"})
        #print(sizes)

        try:
            outer_dev = soup.find(id="colour-variations-options")
            print(outer_dev)
            colourvariations = outer_dev.find_all('span', {'class': 'tooltip-text'})
            for color in colourvariations:
                print("color variation is: " + str(color.get_text()))
        except Exception as e:
            print(e)

        try:
            image_url = image['content']
            l = image_url.split("/")
            l[7] = 'c50d986f5a2dd703a6afa66f842c9132'
            image_url = '/'.join(l)
            print(image_url)
        except Exception as e:
            print(e)
            print("there is no image")
            

        colors = soup.find(id='product-colors-list')
        try:
            print(colors.get_text())
            colors = colors.get_text().rstrip().replace('/n','').lstrip()
        except Exception as e :
            colors = ""
            print("there is no color")

        

        try:
            name = soup.find("div", {"class":"product-vanity-name"})
            name = name.text.rstrip().replace('\n','')
            print("name is " + name)
        except Exception as e:
            print("there is no name")  

        try:
            price = soup.find(id="customize-start")
            print("price")
            print(price.text[1:])
            price = price.text[1:]
        except Exception as e:
            print("there is no price")


        description = soup.find_all('div', {"class":"product-delivery-city"})[1]
        li_items = description.find('ul')
        #print(str(li_items).replace('\n', ''))
        description = str(li_items).replace('\n', '')

        description = html.unescape(description)
        '''
        print(li_items)
        description = ''
        for li in li_items:
            description+= li.text
            description+=', '

        print("description")
        description = description[:-2]
        print(description)
        '''
        '''
        try:
            description = description['content']
            print(description)
        except Exception as e:
            print("there is no discription")
        '''
        sizes = []
        table = soup.find('table', {"class":"table-size"})
        for row in table.find_all('th'):
            cell = {}
            if "hide" not in row['class']:
                #print(row.text)
                sizes.append(row.text)
        category = 'adult'
        #print("sizesss is hereeeeeee")
        print(sizes)
        with open('result_athletichnit.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            item_sku = product_name.split('-')[1]
            count = 0

            for row in table.find_all("td"):
                
                if "table-size-name" in row['class']:
                    #print(row.text)
                    category = row.text
                    count = 0
                elif "hide" in row['class'] or "custom" in row['class'] or "empty" in row['class']:
                    count+=1
                    #print("unchecked") 

                else:
                    count+=1
                    #print(count)
                    try:
                        csv_row = [product_name.split('-')[0],item_sku,name, description, category,price,'USD', image_url, 'Size,Color',colors, sizes[count] ]
                        writer.writerow(csv_row)
                    except Exception as e:
                        print(e)
                        pass
                    #print("checked")
    except Exception as e:
        print("try again or change apiKeys")    
