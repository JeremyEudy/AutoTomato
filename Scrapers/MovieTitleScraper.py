# **************************************************************************** #
#                                                                              #
#                                                             |\               #
#    MovieTitleScraper.py                               ------| \----          #
#                                                       |    \`  \  |  p       #
#    By: jeudy2552 <jeudy2552@floridapoly.edu>          |  \`-\   \ |  o       #
#                                                       |---\  \   `|  l       #
#    Created: 2019/03/23 13:22:36 by jeudy2552          | ` .\  \   |  y       #
#    Updated: 2019/03/23 14:54:06 by jeudy2552          -------------          #
#                                                                              #
# **************************************************************************** #
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
import re

targetURL = "https://www.listchallenges.com/the-most-important-movies-since-1975"
initialGridItem = "/html/body/form/div[7]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div/div[3]"

buttonPath = ""

chrome_instance = webdriver.Chrome()
chrome_driver.get(targetURL)

for i in range(0, 10):
    
