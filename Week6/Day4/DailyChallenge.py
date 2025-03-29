from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up
from bs4 import BeautifulSoup
import re


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)


url = "https://www.bbc.com/weather/293397"
driver.get(url)

# Retrieve HTML code after loading
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract dates from forecasts
dates = [element["aria-label"] for element in soup.find_all("div", class_="wr-day__title wr-js-day-content-title") if element.has_attr("aria-label")]
max_temperatures = [temp.text.split("°")[0] + "°C" for temp in soup.find_all("span", class_="wr-day-temperature__high-value")]
min_temperatures = [temp.text.split("°")[0] + "°C" for temp in soup.find_all("span", class_="wr-day-temperature__low-value")]
conditions = [cond.text.strip() for cond in soup.find_all("div", class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque")]








print("Dates:", dates)
print("Max temperatures:", max_temperatures)
print("Min temperatures:", min_temperatures)
print("Conditions:", conditions)
