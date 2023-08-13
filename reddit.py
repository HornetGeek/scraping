from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller
from selenium.webdriver.chrome.options import Options

Keyboard =Controller()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

groups_links=[]
videos_links=[]
video_link=input("enter video link:")
videos_links.append(video_link)


driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
reddit=driver.get("https://www.reddit.com/account/login/")
time.sleep(1)
emi =  driver.find_element(By.XPATH,'//*[@id="loginUsername"]').send_keys("seso_m")
pas =  driver.find_element(By.XPATH,'//*[@id="loginPassword"]').send_keys("14785236asd")
login=driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()
time.sleep(2)
search_groups=driver.get("https://www.reddit.com/search/?q=car&type=sr")
time.sleep(4)

I =1
while I<30 :
    print(I)
    g_link=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[{s}]/div/a'.format(s=I)).get_attribute("href")
    print(g_link)
    groups_links.append(g_link)
    I=I+1
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

for li in groups_links:
    try:
        print(li)
        driver.get(li)
        time.sleep(4)
        post=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[1]/input').click()
        #driver.navigate().refresh()
        time.sleep(15)
        titl=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[1]/div/textarea').send_keys("this is topic title")
        time.sleep(2)
        write=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div').send_keys(videos_links[0])
        butto=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div/div[1]/button').click()
        time.sleep(1)
    except:
        continue



