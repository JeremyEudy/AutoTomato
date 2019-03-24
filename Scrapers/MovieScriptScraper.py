# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    MovieScriptScraper.py                              ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2019/03/23 18:06:59 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2019/03/23 20:54:23 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
import re

targetURL = "https://www.imsdb.com/"
searchbox = "/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/div/input[1]"
goButton = "/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/div/input[2]"
prefix = 'Read "'
suffix = '" Script'

chrome_driver = webdriver.Chrome()
chrome_driver.get(targetURL)
titles = []

with open("titles.txt", "r") as f:
    titles = f.readlines()

for movie in titles:
    movie = movie[:-8]
    chrome_driver.find_element_by_xpath(searchbox).send_keys(movie)
    chrome_driver.find_element_by_xpath(goButton).click()

    chrome_driver.find_element_by_name(movie).click()
    chrome_driver.find_element_by_name(prefix+movie+suffix).click()
    script = chrome_driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre/pre")
    re.sub('[<\/*b*br*>]', '', script)
    fileName = movie+".txt"
    with open(fileName, "w+") as f:
        f.write(script)

