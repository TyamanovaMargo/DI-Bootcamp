# Exercise 5
import time
import statistics
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36")


driver = webdriver.Chrome(options=options)
url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
driver.get(url)


# Wait for weather data to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "daily-list-item"))
)

# Check if the element is not found
if not driver.find_elements(By.CLASS_NAME, "daily-list-item"):
    print("The weather page did not load correctly. Check the URL or bot blocking.")
    driver.quit()
    exit()



soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

#Extraction of meteorological data
temperatures = []
conditions = []
humidities = []

for forecast in soup.find_all('a', class_='daily-list-item'):
    temp_tag = forecast.find('span', class_='temp-hi')
    if temp_tag and temp_tag.text.strip():
        temp_text = temp_tag.text.strip().replace("°", "")
        if temp_text.isdigit():
            temp_hi = int(temp_text)
            temperatures.append(temp_hi)


    cond_tag = forecast.find('div', class_='phrase')
    if cond_tag and cond_tag.find("p", class_="no-wrap"):
        conditions.append(cond_tag.find("p", class_="no-wrap").text.strip())

    humidity_tag = forecast.find('div', class_='precip')
    if humidity_tag and humidity_tag.text.strip():
        match = re.search(r"(\d+)%", humidity_tag.text)
        if match:
            humidities.append(int(match.group(1)))


print(f" {len(temperatures)} temperatures found.")
print(f" {len(conditions)} weather conditions found.")
print(f" {len(humidities)} humidity values ​​found.")

# Analysis
Mean_temp = round(statistics.mean(temperatures), 1) if temperatures else "No Available"
most_common_condition = Counter(conditions).most_common(1)[0][0] if conditions else "Unknown"
Mean_humidity = round(statistics.mean(humidities), 1) if humidities else "No Available"



print(f" Mean Temperature : {Mean_temp}°F")
print(f" Most common weather condition : {most_common_condition}")
print(f" Mean Humidity : {Mean_humidity}%")