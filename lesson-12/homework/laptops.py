import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

service = Service(ChromeDriverManager().install())  
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.demoblaze.com")
time.sleep(3) 


laptops_tab = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_tab.click()
time.sleep(3)


def scrape_laptops():
    page_laptops = []
    soup = BeautifulSoup(driver.page_source, "html.parser")

    for item in soup.find_all("div", class_="card-block"):
        name_tag = item.find("a", class_="hrefch")
        if name_tag:
            name = name_tag.text.strip()
            price = item.find("h5").text.strip()
            description = item.find("p", class_="card-text").text.strip()

            
            if "monitor" not in name.lower() and "asus full hd" not in name.lower():
                if name not in seen_names:
                    seen_names.add(name)
                    page_laptops.append({
                        "name": name,
                        "price": price,
                        "description": description
                    })
    
    return page_laptops


all_laptops = []
seen_names = set()  

while True:
    all_laptops.extend(scrape_laptops())

    
    try:
        next_button = driver.find_element(By.ID, "next2")
        ActionChains(driver).move_to_element(next_button).click().perform()
        time.sleep(3)  
    except:
        print("No more pages.")
        break  


with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(all_laptops, file, indent=4)

print("Laptop data saved to laptops.json")

driver.quit()
