import requests
from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
# print(scraper.get("https://www.paterehab.com/brain-injury-terms-glossary/").text)
response = scraper.get("https://www.paterehab.com/brain-injury-terms-glossary/")
html_data = BeautifulSoup(response.text, 'html.parser')
print(html_data)
program_names = html_data.select('p > strong')
print(program_names)

#반복문을 사용해서 각 태그의 텍스트값만 출력
for tag in program_names:
	print(tag.get_text())