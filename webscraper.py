from selenium import webdriver
import os
import requests

output_dir = "./downloads"
url = "https://archive.org/details/educationaruba?and[]=languageSorter%3A%22Papiamento%22&and[]=mediatype%3A%22texts%22"
browser = webdriver.Firefox()
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')

# browser = webdriver.Firefox(options=options)

browser.get(url)
tiles = browser.find_elements_by_class_name("tile-img")
for tile in tiles:
    tile.click()
    pdf_link = browser.find_element_by_xpath("/html/body/div[1]/main/div[5]/div/div/div[2]/section[2]/div[8]/a").get_attribute("href")
    print(pdf_link)
    # response = requests.get(pdf_link)
    # if response.status_code == 200:
    #     file_path = os.path.join(output_dir, os.path.basename(pdf_link))
    #     with open(file_path, 'wb') as f:
    #         f.write(response.content)
    browser.get(url)
