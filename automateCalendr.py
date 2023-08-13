from selenium import webdriver
import time
import psycopg2
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"



driver.get("https://animetitans.com/%D9%85%D9%88%D8%A7%D8%B9%D9%8A%D8%AF-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A7%D8%AA/")
time.sleep(3)

img_links = [[],[],[],[],[],[],[]]
eposides_num = [[],[],[],[],[],[],[]]
eposides_title = [[],[],[],[],[],[],[]]

for l,n,t in zip(driver.find_element_by_class_name("sch_monday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_monday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_monday").find_elements_by_class_name("tt") ):
    img_links[0].append(l.get_attribute("src"))
    eposides_num[0].append(n.text)
    eposides_title[0].append(t.text)

    with open('{}.jpg'.format(t.text), 'wb') as handle:
        response = requests.get(l.get_attribute("src"), stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

for l,n,t in zip(driver.find_element_by_class_name("sch_tuesday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_tuesday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_tuesday").find_elements_by_class_name("tt") ):
    img_links[1].append(l.get_attribute("src"))
    eposides_num[1].append(n.text)
    eposides_title[1].append(t.text)


for l,n,t in zip(driver.find_element_by_class_name("sch_wednesday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_wednesday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_wednesday").find_elements_by_class_name("tt") ):
    img_links[2].append(l.get_attribute("src"))
    eposides_num[2].append(n.text)
    eposides_title[2].append(t.text)

for l,n,t in zip(driver.find_element_by_class_name("sch_thursday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_thursday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_thursday").find_elements_by_class_name("tt") ):
    img_links[3].append(l.get_attribute("src"))
    eposides_num[3].append(n.text)
    eposides_title[3].append(t.text)

for l,n,t in zip(driver.find_element_by_class_name("sch_friday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_friday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_friday").find_elements_by_class_name("tt") ):
    img_links[4].append(l.get_attribute("src"))
    eposides_num[4].append(n.text)
    eposides_title[4].append(t.text)

for l,n,t in zip(driver.find_element_by_class_name("sch_saturday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_saturday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_saturday").find_elements_by_class_name("tt") ):
    img_links[5].append(l.get_attribute("src"))
    eposides_num[5].append(n.text)
    eposides_title[5].append(t.text)

for l,n,t in zip(driver.find_element_by_class_name("sch_sunday").find_elements_by_class_name("attachment-post-thumbnail"),driver.find_element_by_class_name("sch_sunday").find_elements_by_class_name("sb"),driver.find_element_by_class_name("sch_sunday").find_elements_by_class_name("tt") ):
    img_links[6].append(l.get_attribute("src"))
    eposides_num[6].append(n.text)
    eposides_title[6].append(t.text)



print(img_links)
print(eposides_num)
print(eposides_title)




