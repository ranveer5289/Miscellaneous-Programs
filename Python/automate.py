#Automate chrome using selenium.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display
import os
import time

chromedriver = "/usr/bin/chromedriver"
os.environ['webdriver.chrome.driver'] = chromedriver

display = Display(visible=0, size=(800,600))
display.start()

br = webdriver.Chrome(chromedriver)
br.get("http://www.google.com/search?q=python")

#q = br.find_element_by_name('q')
#q.send_keys('python')
#q.send_keys(Keys.RETURN)
#time.sleep(3)
print br.title

results = br.find_elements_by_class_name('g')
#print results

for result in results:
    print result.text
    print "-"*140

br.quit()
display.stop()
