# b9122_homework2

Autor: Yiming Ning

Description: this is for b9122 homework 2, contaning two part of code:

## 1. Webcrawler code is class

**Description:** The "Web Crawler for URL Discovery" is a Python-based web crawling script that starts from a seed URL and systematically explores web pages to discover additional URLs. The primary goal is to gather a list of URLs while adhering to a maximum limit of URLs to visit. This project is a basic web crawler example and can be used as a starting point for more complex web scraping and crawling applications.

**Features:**

*Seed URL*: The project begins with a specified seed URL, which serves as the starting point for the web crawl. In this example, the seed URL is set to "https://www8.gsb.columbia.edu."

_URL Queue and Stack_: The script maintains two lists, urls and seen. urls serves as a queue of URLs to crawl, while seen keeps track of visited URLs. Additionally, there's an opened list to keep track of URLs that have been successfully opened.

_Maximum URL Limit_: Users can set a maximum limit on the number of URLs to visit (maxNumUrl). This ensures that the crawler doesn't continue indefinitely.

_URL Access and Parsing_: The script attempts to open and read URLs using the urllib library. It handles exceptions and prints error messages when a URL cannot be accessed.

_Child URL Discovery_: When a URL is successfully accessed, the script parses the webpage content using BeautifulSoup. It looks for anchor (<a>) tags with href attributes, which represent links to other web pages. The child URLs are extracted and normalized using urllib.parse.urljoin.

_URL Filtering_: The script filters the child URLs based on whether they are within the same domain as the seed URL (seed_url in childUrl) and whether they have been seen before (childUrl in seen). URLs that meet these criteria are added to the urls queue and the seen list.

Output: The script provides informative output about its progress, including the number of URLs in the queue, URLs being accessed, and whether URLs meet the filtering criteria.



## 2. United Nations Press Releases Crawler

**Description:** A Python web crawler designed to extract United Nations press releases containing the word "crisis" from the UN Press website.

**Features:**

_Seed URL_: The script starts with a seed URL (https://press.un.org/en) from the UN Press website.

_is_press_release Function_: It defines a function is_press_release to determine whether a web page is a press release. This function checks for the presence of an anchor tag with the href attribute starting with /en/press-release. If such a tag is found, the page is considered a press release.

_Extracting Press Releases_: The main function extract_press_releases_with_crisis crawls through the website, starting from the seed URL. It collects press releases that contain the word "crisis" by searching the text on each page.

_Results_: Once it has collected at least 10 press releases with the word "crisis," the script prints the URLs of these press releases.

