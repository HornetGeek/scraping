from selenium import webdriver
#from webdriver_manager.firefox import firefoxmanager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import keyboard 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import threading
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


JS_ADD_TEXT_TO_INPUT = """ 
  var elm = arguments[0], txt = arguments[1]; 
  elm.value += txt; 
  elm.dispatchEvent(new Event('change')); 
  """ 
#elem =driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
text = u"""
  𝗦𝗘𝗖𝗨𝗥𝗜𝗧𝗬 𝗟𝗘𝗔𝗥𝗡𝗘𝗥𝗦𝗛𝗜𝗣𝗦 𝟮𝟬𝟮𝟯 | 𝗦𝗘𝗥𝗩𝗘𝗦𝗧


  A Security Learnership Is Available For 2023 Where You Can Train To Work Whilst Earning A Monthly Allowance. Servest Security Is Offering A 12 Month Learnership Program To Young South Africans Residing Within KZN, Gauteng And Pretoria Regions.


  𝗥𝗘𝗤𝗨𝗜𝗥𝗘𝗠𝗘𝗡𝗧
  ■ Grade 12
  ■ Must Be A Go Getter
  ■ Must Be Interested And Willing To Learn
  ■ Excellent Communication Skills
  ■ Must Be Residing Within Kzn , Gauteng And Pretoria Region
  ■ Have An Interest In The Security Industry


  https://jobdrivesa.co.za/job/servest-security-learnerships-2023-2024-at-servest/
  """

#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"
chrome_options = Options()
accounts = {}
#mode = input("Enter the mode: ")
videos_links = []

#video_link = input("Enter video Link")

#videos_links.append(video_link)
def automate_facebook(num_of_shares,keywords,num_of_keyword,account,youtube_link,file):

    list_of_groups = []
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com")
        time.sleep(5)
        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(str(account[0]))


        password = driver.find_element(By.XPATH, '//*[@id="pass"]')
        password.send_keys(str(account[1]))
        driver.find_element(By.NAME, "login").click()
        time.sleep(5)
       # driver.find_element(By.XPATH, '/html').click()

        #time.sleep(3)
        if file == "no":


            driver.get('https://www.facebook.com/search/groups/?q={}'.format(keywords[random.randint(1,num_of_keyword-1)]))
            #time.sleep(3)
            #driver.find_element(By.XPATH, '/html/body').click()
            #time.sleep(5)
            #driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[9]/div[1]/a/div/div[2]').click()

            time.sleep(5)
            #try:
            
            #print("please Enter valid keywork")
            #time.sleep(5)
            num_of_group = 1
            while num_of_group<= int(num_of_shares):
                try:
                    htmlElem = driver.find_element(By.CSS_SELECTOR,'html')
                    htmlElem.send_keys(Keys.DOWN[random.randint(0, 3)])
                    group_post = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a'.format(num_of_group))
                    time.sleep(2)
                    link_of_group = group_post.get_attribute('href')
                    list_of_groups.append(link_of_group)
                    num_of_group+=1
                    print(list_of_groups)
                except Exception as e :
                    pass
            #driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a\
            #').click()

            time.sleep(6)

            num_of_share = 1
            for link in list_of_groups:
                driver.get(link)
                time.sleep(4)
                driver.find_element(By.XPATH,'/html').click()
                try:
                    tt =driver.find_element(By.CSS_SELECTOR,'div[class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]').click()
                    time.sleep(10)
                    print("i get it")   
                except:
                    time.sleep(2)
                    cl=driver.find_element(By.CSS_SELECTOR,'div[class="x6s0dn4 x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt"]')
                    driver.execute_script("arguments[0].click();",cl)
                    print("we sent join request")
                    link = link[{}].format(num_of_group)
                    pass
                    
                    
                #driver.execute_script("arguments[0].click();", box_of_post)
                #time.sleep(4)
                
                #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[data-offset-key='33h2m-0-0']"))).send_keys("sfasdfsdf")  
                #n=len(post_content
                #line=0
                #s=driver.find_element(By.CSS_SELECTOR,'div[aria-label="Create a public post…"]')
                JS_ADD_TEXT_TO_INPUT = """ 
                  var elm = arguments[0], txt = arguments[1]; 
                  elm.value += txt; 
                  elm.dispatchEvent(new Event('change')); 
                  """ 
                elem = driver.find_element(By.CSS_SELECTOR,'div[aria-label="Create a public post…"]')
                text = u"""
                  𝗦𝗘𝗖𝗨𝗥𝗜𝗧𝗬 𝗟𝗘𝗔𝗥𝗡𝗘𝗥𝗦𝗛𝗜𝗣𝗦 𝟮𝟬𝟮𝟯 | 𝗦𝗘𝗥𝗩𝗘𝗦𝗧


                  A Security Learnership Is Available For 2023 Where You Can Train To Work Whilst Earning A Monthly Allowance. Servest Security Is Offering A 12 Month Learnership Program To Young South Africans Residing Within KZN, Gauteng And Pretoria Regions.


                  𝗥𝗘𝗤𝗨𝗜𝗥𝗘𝗠𝗘𝗡𝗧
                  ■ Grade 12
                  ■ Must Be A Go Getter
                  ■ Must Be Interested And Willing To Learn
                  ■ Excellent Communication Skills
                  ■ Must Be Residing Within Kzn , Gauteng And Pretoria Region
                  ■ Have An Interest In The Security Industry


                  https://jobdrivesa.co.za/job/servest-security-learnerships-2023-2024-at-servest/
                  """       

                driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, text) 
                #while line<len(post_content) :
                   # for m in post_content[line]:
                   #     s.send_keys(m)
                   #     time.sleep(0.07)
                   # time.sleep(3)
                    #s.send_keys(Keys.ARROW_LEFT)
                   # s.send_keys(Keys.ENTER)
                   # line+=1

                    
                    #s.send_keys(post_content[line])
                   # s.send_keys(Keys.ARROW_LEFT)
                   # time.sleep(2)
                    #s.send_keys(Keys.ARROW_LEFT)
                   # time.sleep(2)
                   # for i in range(0,cr):
                   #     s.send_keys(Keys.ARROW_RIGHT)
                   #     time.sleep(0.05)
                   # time.sleep(1)
                   # s.send_keys(Keys.ENTER)
                   # line +=1     
                    
                #l.send_keys("selenium")
                #driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys("🌎")
                time.sleep(50)
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]').click()
                time.sleep(5)
                #driver.switchTo().alert().dismiss()
                #time.sleep(4)
                #driver.execute_script("arguments[0].click();", post_click)
                print("share done {}".format(str(num_of_share)))
                num_of_share+=1
        else:
            with open('groups_link_fb.txt') as f:
                for line in f:
                    list_of_groups.append(line)
            num_of_share = 1
            for link in list_of_groups:
                driver.get(link)    
                time.sleep(4)
                driver.find_element(By.XPATH, '/html').click()
                time.sleep(3)
                #htmlElem2 = driver.find_element(By.CSS_SELECTOR,'html')
                try:
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/span').click()
                except Exception as e :
                    print("Join group")
                    time.sleep(3)
                    join = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", join)

                    continue
                #driver.execute_script("arguments[0].click();", box_of_post)
                time.sleep(4)
                l = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div")
                for line in post_content:
                    l.send_keys(line)
                    l.send_keys(Keys.ENTER)
                #l.send_keys("selenium")
                time.sleep(2)
                post_click = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div')
                time.sleep(2)
                driver.execute_script("arguments[0].click();", post_click)
                time.sleep(20)
                print("share done {}".format(str(num_of_share)))
                num_of_share+=1

        #keyboard.write("wwww")
        #elem.send_keys("01272011482")
        #driver.find_element(By.XPATH, '//*[@id="mount_0_0_on"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys("01272011482")
    except Exception as e :
        print("there is error check errors.txt")
        print("we will try with another account")
        accounts_file = open("accounts_fb.txt",'r')
        account = str(accounts_file.readline()).split(":")
        print(e)
        driver.close()
        automate_facebook(num_of_shares,keywords,num_of_keyword, account,youtube_link, file)
        text = "url : {} : error is : {} \n".format(link, e)
        print(e)
        with open("errors.txt", "a") as f:
            f.write(text)
        return 0

def linkedin(num_of_shares,keywords,num_of_keyword, account,youtube_link,file):
    links_of_group = []
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(),firefox_options=firefox_options,desired_capabilities=caps)
        driver.get("https://www.linkedin.com")
        time.sleep(5)
        email = "xopixev208@cnxcoin.com"
        password = "moatazmahmoud"

        email = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/div[1]/input')
        email.send_keys(str(account[0]))
        password = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/div[2]/input")
        password.send_keys(str(account[1]))

        if file == "no":
            #driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button').click()
            link = "https://www.linkedin.com/search/results/groups/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&sid=i.1".format(str(keywords[random.randint(1,num_of_keyword-1)]))
            print(link)
            time.sleep(5)
            driver.get(link)
            time.sleep(12)
            i = 1
            while i < num_of_shares :
                #//*[@id="YnY0p9i+T0uFiZ9AMBGE9w=="]/div/ul/li[2]/div/div/div[2]/div[1]/div[1]/div/span/span/a
                #/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[2]/div/div/div[2]/div[1]/div[1]/div/span/span/a
                link_of_group = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{}]/div/div/div[2]/div[1]/div[1]/div/span/span/a'.format(i))
                href = link_of_group.get_attribute('href')
                print(href)
                links_of_group.append(href)
                print(links_of_group)
                i+=1

            num_of_share = 1
            for link in links_of_group:
                driver.get(link)
                time.sleep(10)
                try:
                    #/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[1]/section/div/button
                    join = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[1]/section/div/button')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", join)
                    print("join group")
                    result = join.get_attribute("id")
                    print(result)
                    #join.click()
                    time.sleep(10)
                except Exception as e:
                    driver.get(link)
                    time.sleep(5)
                    post = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[4]/div/div[1]/button')
                    driver.execute_script("arguments[0].click();", post)
                    time.sleep(5)
                    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]').send_keys(youtube_link)
                    time.sleep(2)
                    post_buuton = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
                    driver.execute_script("arguments[0].click();", post_buuton)
                    time.sleep(10)
                    print("share done {}".format(str(num_of_share)))
                    num_of_share+=1
        else:
            print("read from the file")
            with open('groups_link_linkedin.txt') as f:
                for line in f:
                    links_of_group.append(line)

            time.sleep(5)
            num_of_share = 1
            for link in links_of_group:
                driver.get(link)
                time.sleep(10)
                try:
                    #/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[1]/section/div/button
                    join = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[1]/section/div/button')
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", join)
                    print("join group")
                    result = join.get_attribute("id")
                    print(result)
                    #join.click()
                    time.sleep(10)
                except Exception as e:
                    driver.get(link)
                    time.sleep(5)
                    post = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div/main/div/div[4]/div/div[1]/button')
                    driver.execute_script("arguments[0].click();", post)
                    time.sleep(5)
                    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]').send_keys(youtube_link)
                    time.sleep(2)
                    post_buuton = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
                    driver.execute_script("arguments[0].click();", post_buuton)
                    time.sleep(10)
                    print("share done {}".format(str(num_of_share)))
                    num_of_share+=1

    except Exception as e :
        print("there is error check errors.txt")
        print("we will try with another account")
        accounts_file = open("accounts_fb.txt",'r')
        account = str(accounts_file.readline()).split(":")
        print(e)
        driver.close()
        linkedin(num_of_shares,keywords,num_of_keyword, account,youtube_link, file)
        text = "url : {} : error is : {} \n".format(link, e)
        print(e)
        with open("errors.txt", "a") as f:
            f.write(text)

def reddit(num_of_shares,keywords,num_of_keyword, account,youtube_link, file):

    driver = webdriver.Chrome(ChromeDriverManager().install(),firefox_options=firefox_options,desired_capabilities=caps)
    reddit=driver.get("https://www.reddit.com/account/login/")
    time.sleep(1)
    emi =  driver.find_element(By.XPATH,'//*[@id="loginUsername"]').send_keys(account[0])
    pas =  driver.find_element(By.XPATH,'//*[@id="loginPassword"]').send_keys(account[1])
    login=driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()
    time.sleep(2)

    if file == "no":

        search_groups=driver.get("https://www.reddit.com/search/?q={}&type=sr".format(str(keywords[random.randint(1,num_of_keyword-1)])))
        time.sleep(4)
        groups_links=[]

        I =1
        while I< num_of_shares :
            print(I)
            g_link=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[{s}]/div/a'.format(s=I)).get_attribute("href")
            print(g_link)
            groups_links.append(g_link)
            I=I+1
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        for li in groups_links:
            num_of_share = 1
            try:
                print(li)
                driver.get(li)
                time.sleep(4)
                post=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[1]/input').click()
                #driver.navigate().refresh()
                time.sleep(15)
                titl=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[1]/div/textarea').send_keys('youtube link')
                time.sleep(2)
                write=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div').send_keys(str(youtube_link))
                butto=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div/div[1]/button').click()
                print("share done {}".format(str(num_of_share)))
                num_of_share +=1
                time.sleep(5)
            except:
                continue
    else:
        print("read from the file")
        with open('groups_link_reddit.txt') as f:
            for line in f:
                groups_links.append(line)

            time.sleep(5)
        for li in groups_links:
            try:
                print(li)
                driver.get(li)
                time.sleep(4)
                post=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[1]/input').click()
                #driver.navigate().refresh()
                time.sleep(15)
                titl=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[1]/div/textarea').send_keys('youtube link')
                time.sleep(2)
                write=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div').send_keys(str(youtube_link))
                butto=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div/div[1]/button').click()
                print("share done")
                time.sleep(7)
            except:
                continue

try:
    while True:
        x = 1
        print("             HI Rudolfs          ")
        youtube_link = str(input("Please Enter the Youtube VIdeos Link : "))
        print("***** CHoose Number of Platform to Shares : ")
        num_of_platform = int(input(" 1-Facebbok \n 2-linkedin \n 3-reddit \n 4-All \n "))
        num_of_shares = int(input("Please Enter NUmber of shares: "))
        file = str(input("read groups link from file? yes or no : ")) 
        keywords= str(input("Entere Keywords sepreated by ',': "))
        keywords += "," + keywords
        keywords = keywords.split(",")
        num_of_keyword = len(keywords)
        print("working .....")

        if int(num_of_platform) == 1:
            accounts_file = open("accounts_fb.txt",'r')
            account = str(accounts_file.readline()).split(":")
            post_file=open("postcontent.txt",'r')
            post_content=post_file.readlines()
            


            face = threading.Thread(target=automate_facebook,args=(num_of_shares,keywords,num_of_keyword,account,youtube_link, file))
            face.start()
        elif int(num_of_platform) == 2:
            accounts_file = open("accounts_linkedin.txt",'r')
            account = str(accounts_file.readline()).split(":")
            linked = threading.Thread(target=linkedin,args=(num_of_shares,keywords,num_of_keyword, account,youtube_link, file))
            linked.start()

        elif int(num_of_platform) == 3:
            accounts_file = open("accounts.reddit.txt",'r')
            account = str(accounts_file.readline()).split(":")

            redditt = threading.Thread(target=reddit,args=(num_of_shares,keywords,num_of_keyword, account,youtube_link, file))
            redditt.start()
        else:
            accounts_file_fb = open("accounts_fb.txt",'r')
            account_fb = str(accounts_file_fb.readline()).split(":")

            accounts_file_linkedin = open("accounts_linkedin.txt",'r')
            account_linedin = str(accounts_file_linkedin.readline()).split(":")

            accounts_file_reddit = open("accounts.reddit.txt",'r')
            account_reddit = str(accounts_file_reddit.readline()).split(":")

            face = threading.Thread(target=automate_facebook,args=(num_of_shares,keywords,num_of_keyword,account,youtube_link, file))
            face.start()

            linked = threading.Thread(target=linkedin,args=(num_of_shares,keywords,num_of_keyword, account,youtube_link, file))
            linked.start()

            redditt = threading.Thread(target=reddit,args=(num_of_shares,keywords,num_of_keyword, account,youtube_link, file))
            redditt.start()
except Exception as e :
    x=0
    while x < 4 :
        print(e)
        print("we have error we will try again")
        #error = #automate_facebook()
        x+=1
