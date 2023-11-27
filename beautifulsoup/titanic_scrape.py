import requests
from bs4 import BeautifulSoup

website_url = 'https://subslikescript.com/movie/Titanic-120338#google_vignette'
response = requests.get(website_url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

title = soup.find('h1').text
plot = soup.find('p', class_="plot").text
transcript = soup.find('div', class_='full-script').text
transcript_transformed = transcript.strip().replace('\n', ' ')

file_titanic = "beautifulsoup/titanic.txt"

with open(file_titanic, 'w') as f:
    f.write('Title: {}'.format(title))
    f.write('Plot: {}'.format(plot))
    f.write('Transcript: {}'.format(transcript))
