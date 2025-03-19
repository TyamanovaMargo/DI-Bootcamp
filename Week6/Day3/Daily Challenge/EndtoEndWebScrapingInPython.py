
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://github.com/topics'
headers = {'User-Agent': 'Mozilla/5.0'} #Mimics a real browser to prevent GitHub from blocking the request.
response = requests.get(url, headers=headers) 

print(f'Status Code: {response.status_code}')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract topics using correct selectors
    topic_titles = [title.text.strip() for title in soup.find_all('p', class_='f3')]
    topic_descriptions = [desc.text.strip() for desc in soup.find_all('p', class_='f5')]

    # Ensure lists have the same length
    min_length = min(len(topic_titles), len(topic_descriptions))
    topic_titles = topic_titles[:min_length]
    topic_descriptions = topic_descriptions[:min_length]

    print(f'Number of topics extracted: {len(topic_titles)}')
    print(f'First 5 topic titles: {topic_titles[:5]}')
    print(f'First 5 descriptions: {topic_descriptions[:5]}')

    # Create DataFrame
    df = pd.DataFrame({'title': topic_titles, 'description': topic_descriptions})
    print(df)
else:
    print('Failed to retrieve the webpage. Check your connection or GitHub restrictions.')

