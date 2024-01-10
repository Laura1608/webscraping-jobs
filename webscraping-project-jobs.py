import requests
from bs4 import BeautifulSoup

url = 'https://www.freelance.nl/opdrachten'

# Retrieve content from webpage
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

project_list = soup.find_all('ul', class_='project-list')
project_list

links = []

for item in soup.select('projectlist-item'):
    link = soup.find('a', href='projectlist-link')
    links.append(link)

