from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests

output_dir = "./downloads"
url = "https://archive.org/details/educationaruba?and[]=languageSorter%3A%22Papiamento%22&and[]=mediatype%3A%22texts%22"
browser = webdriver.Firefox()
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')

# browser = webdriver.Firefox(options=options)
links = []
browser.get(url)
tiles = browser.find_elements_by_xpath('//div[contains(@class, "item-ttl")]/a')
for tile in tiles:
    links.append(tile.get_attribute('href'))
for link in links:
    browser.get(link)

    # pdf_link = browser.find_element_by_xpath("/html/body/div[1]/main/div[5]/div/div/div[2]/section[2]/div[8]/a").get_attribute("href")
    pdf_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,"//*[contains(text(), 'PDF')]"))
    ).get_attribute("href")
    print(pdf_link)
    response = requests.get(pdf_link)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(pdf_link))
        with open(file_path, 'wb') as f:
            f.write(response.content)
 