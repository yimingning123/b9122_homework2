
import requests
from bs4 import BeautifulSoup
import re

# Seed URL
seed_url = "https://press.un.org/en"

# Function to check if a page is a press release
def is_press_release(page_url):
    response = requests.get(page_url)
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.content, "html.parser")
    press_release_links = soup.find_all("a", href=re.compile(r'^/en/press-release'))
    return len(press_release_links) > 0

# Function to extract press releases containing the word "crisis"
def extract_press_releases_with_crisis(seed_url, max_releases=10):
    press_releases = []
    page_queue = [seed_url]
    visited_pages = set()

    while page_queue:
        url = page_queue.pop(0)
        visited_pages.add(url)

        if is_press_release(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text()
            if "crisis" in text.lower():
                press_releases.append(url)

                # Check if we have collected enough press releases
                if len(press_releases) >= max_releases:
                    break

        if len(press_releases) >= max_releases:
            break

        # Find and add links on the current page to the queue
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all("a", href=True)
            for link in links:
                href = link['href']
                if href.startswith("/") and href not in visited_pages:
                    page_queue.append("https://press.un.org" + href)

    return press_releases

# Extract at least 10 press releases containing the word "crisis"
press_releases = extract_press_releases_with_crisis(seed_url, max_releases=10)

# Print the results
for i, release_url in enumerate(press_releases, 1):
    print(f"Press Release {i}: {release_url}")
