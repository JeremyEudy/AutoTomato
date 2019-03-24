"""
Title: TropesScraper.py
Author: Will Irwin
"""
import csv
import string
import time

from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select

target_url = "https://tvtropes.org/pmwiki/pmwiki.php/"
driver_path = '/usr/local/bin/geckodriver'
xpath = "//*[@id=\"folder0\"]/ul/li[1]/text()"
with open("titles.txt", "r") as f:
    movie_titles = f.readlines()
nopunc_movie_titles = [movie.translate(str.maketrans('', '', string.punctuation)) for movie in movie_titles]
nopunc_movie_titles = [movie.replace(" ", "") for movie in nopunc_movie_titles]
nopunc_movie_titles = [movie.strip() for movie in nopunc_movie_titles]

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(executable_path=driver_path, options=options)
trope_dict = {}

def parse_first():
    """Main version of pages"""
    try:
        browser.find_element_by_class_name("toggle-all-folders-button").click()
        folders = browser.find_elements_by_class_name("folder")
        tropes = []
        for folder in folders:
            links = folder.find_elements_by_xpath("ul/li/a[1]")
            tropes.extend([y.text.lower() for y in links])
        return tropes
    except:
        return []


def parse_second():
    """Older pages"""
    try:
        links = browser.find_elements_by_xpath("/html/body/div[5]/div[2]/article/div[2]/ul/li/a[1]")
        tropes = [y.text.lower() for y in links]
        return tropes
    except:
        return []

def get_script(title):
    """Retrieve script text from movie titles"""
    with open("Scripts/"+title.strip()+".txt", "rb") as f:
        contents = f.read()
    # import ipdb;ipdb.set_trace()
    contents = str(contents).replace(",", "")
    return contents

def clean_tropes(tropes):
    """Clean up bad boy lists"""
    tropes = list(filter(None, tropes))
    tropes = list(set(tropes))
    tropes = sorted(tropes)
    return tropes

def decide_parse_path(title):
    """Shorten run time by breaking out of unnecessary logic"""
    tropes = []
    for media in ["Film/", "WesternAnimation/", "Disney/"]:
        composite_url = target_url+media+title
        print(f"Trying: {title} under category {media}")
        browser.get(composite_url)
        time.sleep(1)

        result = parse_first()
        if result and tropes:
            return []
        else:
            tropes.extend(result)
            continue

        result = parse_second()
        if result and tropes:
            return []
        else:
            tropes.extend(result)

    return tropes

for title in nopunc_movie_titles:
    tropes = decide_parse_path(title)
    if not tropes:
        break
    tropes = clean_tropes(tropes)
    trope_dict[title] = tropes

flat_trope_list = [trope for tropes in trope_dict.values() for trope in tropes]
unique_tropes = sorted(set(flat_trope_list))
headers = ["Title", "Text", *unique_tropes]

with open("tropes_by_movie.csv", "w+") as f:
    # import ipdb;ipdb.set_trace()
    output_file = csv.writer(f)
    output_file.writerow(headers)
    for idx, title in enumerate(nopunc_movie_titles):
        try:
            script_text = get_script(movie_titles[idx])
            values = [1 if trope in trope_dict[title] else 0 for trope in unique_tropes]
            print(f"Writing row for {title}")
            output_file.writerow([movie_titles[idx], script_text, *values])
        except:
            print(f"Couldn't write {title}")
