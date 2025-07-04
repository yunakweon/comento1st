import requests
from bs4 import BeautifulSoup

# URL of the translation page
url = 'https://papago.naver.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the input and output text fields
input_field = soup.find('textarea', {'id': 'txtSource'})
output_field = soup.find('div', {'id': 'txtTarget'})

# Enter some text into the input field
input_field.string = 'Hello, how are you?'

# Print the contents of the output field
print(output_field.string)
