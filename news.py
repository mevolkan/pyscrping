import requests
from bs4 import BeautifulSoup

# Function to scrape headlines
def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract headlines
    headlines = soup.find_all("h3", class_="story-title")
    
    # Extract the text from headlines and remove leading/trailing whitespaces
    headlines_list = [headline.text.strip() for headline in headlines]
    
    return headlines_list

# Scrape headlines from standardmedia.co.ke
standardmedia_url = "https://www.standardmedia.co.ke/"
standardmedia_headlines = scrape_headlines(standardmedia_url)

print("Standard Media - Headlines:")
for headline in standardmedia_headlines:
    print("- ", headline)
print()

# Scrape headlines from businessdailyafrica.com
businessdaily_url = "https://www.businessdailyafrica.com/"
businessdaily_headlines = scrape_headlines(businessdaily_url)

print("Business Daily Africa - Headlines:")
for headline in businessdaily_headlines:
    print("- ", headline)
print()

# Scrape headlines from nation.africa/kenya
nation_url = "https://nation.africa/kenya"
nation_headlines = scrape_headlines(nation_url)

print("Nation - Headlines:")
for headline in nation_headlines:
    print("- ", headline)

