from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# TODO: create terminal app with no open tabs requirement
# TODO: Create a GUI for it

PATH = "chromedriver86.exe"
mainLink = "https://www.instagram.com/"
browser = webdriver.Chrome(PATH)
browser.implicitly_wait(10)
numberClassName = "g47SY"
file_stream = open("handles.csv", "rt", encoding="utf-8-sig")
csv_reader = csv.reader(file_stream, delimiter=",")
handles = list(csv_reader)
file_stream.close()

output = open('output.csv', 'w+', encoding="utf-8-sig")
output.write("id,name,handle,link,#posts,#followers,#following\n")
accountCount = 1
for handle in handles:
    link = mainLink + handle[0]
    browser.get(link)
    elements = browser.find_elements(By.CLASS_NAME, numberClassName)
    name = browser.find_element_by_css_selector(".rhpdm").text
    output.write(
        f"{accountCount},{name},{handle[0]},{link},\"{elements[0].text}\","
        f"\"{elements[1].text}\",\"{elements[2].text}\"\n")
    accountCount += 1
    print(f"{handle[0]} scraped successfully")
output.close()
browser.close()
