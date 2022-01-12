from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#1. Khai báo browser
browser = webdriver.Chrome(executable_path= 'chromedriver.exe')

#2. Mở URL của post
browser.get("https://www.facebook.com/groups/miaigroup/permalink/730028114435130/")

sleep(5)

# #3 Lấy link hiện comment
showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div")
showcomment_link.click()
# #4. Lấy comment
showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]")
showmore_link.click()
sleep(2)
showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]")
showmore_link.click()
sleep(2)
#

sleep(2)
#3. Đóng browser
browser.close()