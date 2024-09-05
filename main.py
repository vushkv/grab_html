from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'/Users/viktorushakov/PycharmProjects/screen_device/venv/bin/chromedriver')

driver.get('https://google.com')
time.sleep(3)
# print(driver.page_source)
with open("page.txt", "w") as file:
    file.write(driver.page_source)
driver.quit()
print('done')