import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://srh.bankofchina.com/search/whpj/search_cn.jsp')

select_element = driver.find_element(By.XPATH, '//*[@id="pjname"]')
select = Select(select_element)
select.select_by_visible_text('欧元')

search_button = driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
search_button.click()

wait = WebDriverWait(driver, 5)
result_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'odd')))

for element in result_elements:
    content = element.text
    contents = content.split(' ')
    result = ' '.join([contents[0], contents[3], contents[6], contents[7]])
    print(result)

time.sleep(60)
driver.quit()

