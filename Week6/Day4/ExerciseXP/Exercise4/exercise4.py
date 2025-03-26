#🌟 Exercise 4 : Scrape and Categorize News Articles from a JavaScript-Enabled News Site

import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Launching Selenium
driver = webdriver.Chrome(options=options)

# Go to the BBC Technology page
url = "https://www.bbc.com/innovation/technology"
driver.get(url)

# Extract HTML code
soup = BeautifulSoup(driver.page_source, "html.parser")

# Closing Selenium
driver.quit()

# Extracting titles
titles = [title.text.strip() for title in soup.find_all("h2", {"data-testid": "card-headline"})]

# Extracting raw dates
dates_raw = [date.text.strip() for date in soup.find_all("span", class_="sc-6fba5bd4-1 ioNoDA")]

# Transforming dates into a readable format
dates = []
for date_text in dates_raw:
    if "days ago" in date_text:
        days = int(date_text.split()[0])
        formatted_date = (datetime.today() - timedelta(days=days)).strftime('%B %Y')
    else:
        formatted_date = "Unknown"
    dates.append(formatted_date)

# Check the lengths
print(f"Titles Number : {len(titles)}")
print(f"Dates Number  : {len(dates)}")

# Adjust the size of lists
min_length = min(len(titles), len(dates))
titles = titles[:min_length]
dates = dates[:min_length]

# DataFrame creation
df = pd.DataFrame({"Title": titles, "Month": dates})

# Categorizing articles by publication month
categorized_df = df.groupby("Month")["Title"].apply(list).reset_index()


print(categorized_df)