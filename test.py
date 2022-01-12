from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


#1. Khai báo biến brower
browser =webdriver.Chrome(executable_path= "chromedriver.exe")

#2. Mở thử 1 trang web
browser.get("http://facebook.com")

#2a. Điền thông tin vào ô user and pass
txt_User = browser.find_element_by_id("email")
txt_User.send_keys("0981730116")

txt_Pass = browser.find_element_by_id("pass")
txt_Pass.send_keys("0981730116vietdeptrai")

#2b Submit form
txt_Pass.send_keys(Keys.ENTER)


#3. Dừng chương trình 5s
sleep(50)

#4. Đóng trình duyệt
browser.close()


