# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    MovieScriptScraper.py                              ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2019/03/23 18:06:59 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2019/03/23 22:33:29 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
import re
from time import sleep

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

for movieRaw in titles:
    movie = movieRaw[:-8]
    chrome_driver.find_element_by_xpath(searchbox).send_keys(movie)
    chrome_driver.find_element_by_xpath(goButton).click()
    sleep(2)

    try:
        chrome_driver.find_element_by_link_text(movie).click()
        sleep(2)

        chrome_driver.find_element_by_link_text(prefix+movie+suffix).click()
        sleep(2)

        try:
            script = chrome_driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre").text

            re.sub('[<\/*b*br*>]', '', script)
            fileName = "Scripts/"+movie+".txt"
            with open(fileName, "w+") as f:
                f.write(script)
        except:
            chrome_driver.execute_script("window.history.go(-1)")
            titles.pop(titles.index(movieRaw))
            print("{} yielded a .pdf".format(movie))

    except:
        print("{} not found in page".format(movie))
        titles.pop(titles.index(movieRaw))

with open("titles.txt", "w") as f:
    f.write('\n'.join(titles))
