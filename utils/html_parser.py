import json
from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    json_content = script_tag.string


    return json.loads(json_content)
