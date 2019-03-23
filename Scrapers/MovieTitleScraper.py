# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    MovieTitleScraper.py                               ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2019/03/23 13:22:36 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2019/03/23 16:54:37 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
import re

targetURL = "https://www.listchallenges.com/the-most-important-movies-since-1975"

buttonPath = '/html/body/form/div[7]/div[1]/div[3]/div[1]/div[1]/div[2]/ul/li[12]/a'

chrome_driver = webdriver.Chrome()
chrome_driver.get(targetURL)
names = []

for i in range(1, 11):
    for j in range(1, 41):
        gridItem = "/html/body/form/div[7]/div[1]/div[3]/div[1]/div[4]/div[1]/div["+str(j)+"]/div/div[3]"
        try:
            name = chrome_driver.find_element_by_xpath(gridItem).text
            print(name)
            names.append(name)
        except Exception as e:
            print(e)
            names.append("no element found")

    try:
        chrome_driver.find_element_by_xpath(buttonPath).click()
    except:
        pass

with open("titles.txt", "w+") as f:
    f.write('\n'.join(names))
