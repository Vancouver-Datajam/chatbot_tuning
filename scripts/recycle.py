from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time
import random
from bs4 import BeautifulSoup
import re
import ast


def get_html_from_url(url):
    
    options = Options()
    
    # Set the window size to simulate a mobile browser
    # options.add_argument("--window-size=375,812")  # Adjust the width and height as needed
    
    # Set the User-Agent to simulate a mobile device
    # mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    

    mobile_user_agents=["Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    ]
    mobile_user_agent = random.choice(mobile_user_agents)
    options.add_argument(f"user-agent={mobile_user_agent}")
    # Chrome is controlled by automated test software
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    
    # Selenium Stealth settings
    stealth(driver,
          languages=["en-US", "en"],
          vendor="Google Inc.",
          platform="Win32",
          webgl_vendor="Intel Inc.",
          renderer="Intel Iris OpenGL Engine",
          fix_hairline=True,
      )   
    driver.get(url)
    
    time.sleep(0.000)  # Wait for 5 seconds (adjust as needed)
    
    # Wait for page to load
    while driver.execute_script("return document.readyState") != "complete":
        pass
     
    # Get the entire HTML of the page after waiting for all elements
    html = driver.page_source

    driver.quit()
    return html

url = "https://recyclebc.ca/what-can-i-recycle-2/#1489678746756-a838ed57-c78d"
page = get_html_from_url(url)
soup = BeautifulSoup(page, "html.parser")
print(soup)

container = soup.find("div", class_ = "wpb_wrapper")
results = soup.find("h5", class_="materials-dosdonts")
print(results.text)
'''
results = soup.find_all("li")
for i in results:
      print(i.text)


container = results.find_all("div", class_="blk-content padding-right-eq70")

f= open("mattress.txt","w+")
for i in container:
      f.write(i.text)
f.write(url)
f.close()'''