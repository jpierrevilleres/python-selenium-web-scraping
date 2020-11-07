# Load selenium components
from selenium import webdriver

DRIVER_PATH = '/home/jp/prog_drivers/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Web Scraping Problem 1 – The Certificate
# Establish chrome driver and go to report site URL
url = "https://testwebsite.com"
driver = webdriver.Chrome()
driver.get(url)

# Web Scraping Problem 2 – Iframes
# Switch to iframe where form is
frame_ref = driver.find_elements_by_tag_name("iframe")[0]
iframe = driver.switch_to.frame(frame_ref)

# Find the Customer ID field and populate it
element = driver.find_element_by_name("custId")
element.send_keys(custId)  # send a test id

# Find and select the date drop-downs
select = Select(driver.find_element_by_name("fromMonth"))
select.select_by_visible_text(from_month)
select = Select(driver.find_element_by_name("fromYear"))
select.select_by_visible_text(from_year)
select = Select(driver.find_element_by_name("toMonth"))
select.select_by_visible_text(to_month)
select = Select(driver.find_element_by_name("toYear"))
select.select_by_visible_text(to_year)

# Web Scraping Problem 3 – JavaScript
# Find the ‘Find’ button, then click it
driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]/table[3]/tbody/tr[2]/td[2]/input").click()

#Web Scraping the Data 
# Loop through transactions and count
links = driver.find_elements_by_tag_name('a')
link_urls = [link.get_attribute('href') for link in links]
thisCount = 0
isFirst = 1
for url in link_urls:
if (url.find("GetXas.do?processId") >= 0):  # URL to link to transactions
       	if isFirst == 1:  # already expanded +
              	isFirst = 0
else:
       	driver.get(url)  # collapsed +, so expand
# Find closest element to URL element with correct class to get tran type                            tran_type=driver.find_element_by_xpath("//*[contains(@href,'/retail/transaction/results/GetXas.do?processId=-1')]/following::td[@class='txt_75b_lmnw_T1R10B1']").text
              # Get transaction status
              status = driver.find_element_by_class_name('txt_70b_lmnw_t1r10b1').text
              # Add to count if transaction found
              if (tran_type in ['Move In','Move Out','Switch']) and 
(status == "Complete"):
                    thisCount += 1


#Web Scraping Workaround Solutions
element = WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.ID, "theFirstLabel")))