#🌟 Exercise 1 : Parsing HTML with BeautifulSou

# Read the HTML content of the page.
from bs4 import BeautifulSoup

html_path = "/Users/margotiamanova/Desktop/DI-Bootcamp/Week6/Day3/ExerciseXP/index.html"

with open(html_path, "r") as file:
    content = file.read()
    print(content)


soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())



#Find the title of the webpage (the content inside the <title> tag).
title = soup.title.text 
print("Page Title:", title)
print(soup.title.get_text())

#Extract all paragraphs (<p> tags) from the page.
# paragraphs = soup.find_all("p")
# print(f"Paragraph {paragraphs}")

#2
paragraphs = [p.text for p in soup.find_all("p")]
print("\nParagraphs:")
for p in paragraphs:
    print("-", p)

# # Retrieve all links (URLs in <a href=""> tags) on the page.
links = [a["href"] for a in soup.find_all("a", href=True)]
print("\nLinks:")
for link in links:
    print("-", link)

# 🌟 Exercise 2 : Scraping robots.txt from Wikipedia
# Write a Python program to download and display the content of robot.txt for wikipedia
import requests

# URL of Wikipedia's robots.txt file
url = "https://en.wikipedia.org/robots.txt"

# Send a GET request to fetch the robots.txt file
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("robots.txt content:\n")
    print(response.text)  # Display the content of robots.txt
else:
    print("Failed to retrieve robots.txt:", response.status_code)



# 🌟Exercise 3 : Extracting Headers from Wikipedia’s Main Page

import requests
import re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for header in headers:
    print(header.text)


#🌟 Exercise 4 : Checking for Page Title

# Function to check if a page has a title
def check_page_title(url):
        # Send a GET request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Check if the page has a <title> tag
            if soup.title and soup.title.text:
                print(f" Page contains a title: {soup.title.text}")
            else:
                print(" No title found on the page.")

# Example usage
url = "https://en.wikipedia.org/wiki/Main_Page" 
check_page_title(url)


#🌟 Exercise 5 : Analyzing US-CERT Security Alerts
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.cisa.gov/news-events/cybersecurity-advisories?f%5B0%5D=advisory_type%3A93"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

date_elements = soup.find_all("time", class_="datetime")
dates = [element.text.strip() for element in date_elements]

current_year = datetime.datetime.now().year
current_year_alerts = [date for date in dates if str(current_year) in date]

num_alerts = len(current_year_alerts)
print(f"Number of US-CERT security alerts in {current_year}: {num_alerts}")







#🌟 Exercise 6 : Scraping Movie Detailsrt requests
from bs4 import BeautifulSoup
import requests

# IMDb movie list URL
url = "https://www.imdb.com/list/ls091294718/"


# Send the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the list of movies
    movies = soup.find_all("div", class_="lister-item mode-detail")

    for i in range(min(10, len(movies))):  # Get up to 10 movies
        movie = movies[i]

        # Extract the title
        title_element = movie.find("h3", class_="lister-item-header")
        title = title_element.a.text.strip() if title_element and title_element.a else "Title not found"

        # Extract the year
        year_element = movie.find("span", class_="lister-item-year")
        year = year_element.text.strip("()") if year_element else "Year not found"

        # Extract the summary (if available)
        summary_element = movie.find("p", class_="text-muted")
        summary = summary_element.text.strip() if summary_element else "Summary not found"

        # Print the result
        print(f"🎬 Movie: {title}")
        print(f"📅 Year: {year}")
        print(f"📖 Summary: {summary}\n")

else:
    print(f"Error loading IMDb: {response.status_code}")

