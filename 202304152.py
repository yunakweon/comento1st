import requests
from bs4 import BeautifulSoup

url = 'https://www.threetimes.kr/?NaPm=ct%3Dlghyc30c%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3De69e325bdd8796aff0d88ff6d2478020929bd310'

# Send HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the href attribute of each link
for link in links:
    print(link.get('href'))
