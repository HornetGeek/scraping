from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.google.com/")

elem=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
JS_ADD_TEXT_TO_INPUT = """ 
  var elm = arguments[0], txt = arguments[1]; 
  elm.value += txt; 
  elm.dispatchEvent(new Event('change')); 
  """ 
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