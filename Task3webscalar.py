 import requests
from bs4 import BeautifulSoup

# Step 1: Website URL (example: BBC News)
url = 'https://www.bbc.com/news'

# Step 2: Send GET request
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch the webpage")
    exit()

# Step 3: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract headlines (you can adjust the tag/class depending on the site)
headlines = []

for tag in soup.find_all(['h1', 'h2', 'h3']):
    headline = tag.get_text(strip=True)
    if headline and len(headline) > 15:
        headlines.append(headline)

# Step 5: Save to a text file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for i, headline in enumerate(headlines, 1):
        file.write(f"{i}. {headline}\n")

print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")