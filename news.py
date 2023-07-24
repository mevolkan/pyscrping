import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape headlines
def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract titles
    headlines = soup.find_all("h2")

    # Extract the text from headlines and remove leading/trailing whitespaces
    headlines_list = [headline.text.strip() for headline in headlines]

    return headlines_list

# Scrape headlines from nation.africa/kenya
nation_url = "https://nation.africa/kenya"
nation_headlines = scrape_headlines(nation_url)

# Save headlines to a CSV file
csv_file_path = "nation_headlines.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    print("Nation - Headlines:")
    for headline in nation_headlines:
        print("- ", headline)
        writer.writerow([headline])

print("Headlines saved to", csv_file_path)
