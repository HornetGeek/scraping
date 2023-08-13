from selenium import webdriver
from selenium.webdriver.common.by import By
#import chromedriver_autoinstaller

#chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

def paste_content(driver, el, content):
    driver.execute_script(
      f'''
const text = `{content}`;
const dataTransfer = new DataTransfer();
dataTransfer.setData('text', text);
const event = new ClipboardEvent('paste', {{
  clipboardData: dataTransfer,
  bubbles: true
}});
arguments[0].dispatchEvent(event)
''',
      el)

# Go to a page
driver.get('https://www.google.com/')
# Find the input box
input_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
msg = 'gfhgfh'
paste_content(driver, input_el, msg)