import requests
from bs4 import BeautifulSoup
import csv

primary_category = "Medical Journal"

# Define the URL to be crawled
url = "https://www.google.com/search?q=" + primary_category

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a")

filtered_links = [link.get("href") for link in links if primary_category in link.text]


with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["URL"])
    writer.writerows([[link] for link in filtered_links])