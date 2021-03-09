from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re
import csv

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(
    'staff_emails_scraper\chromedriver.exe', options=chrome_options)

driver.maximize_window()
driver.get('https://www.tau.ac.il/tau/index')

# insert professor's names to the list
teachers_list = []

with open('university_prof_emails_database.csv', 'a', newline='', encoding='utf-8-sig') as database:
    database_writer = csv.writer(database)
    database_writer.writerow(['name', 'title_description', 'email'])
    for teacher in teachers_list:
        teacher_first_last = teacher.split()
        first_name_box = driver.find_element_by_id('edit-first-name')
        first_name_box.clear()
        first_name_box.send_keys(teacher_first_last[0])

        last_name_box = driver.find_element_by_id('edit-last-name')
        last_name_box.clear()
        last_name_box.send_keys(teacher_first_last[1])

        search_btn = driver.find_element_by_id('edit-submit-search-pepole')
        search_btn.click()

        title_description = driver.find_element_by_xpath(
            '//*[@id="tau-person-results-table"]/tbody/tr/td[2]').text

        email = driver.find_element_by_xpath((
            '//*[@id="tau-person-results-table"]/tbody/tr/td[5]/div/a'))
        email_text = re.findall('[^:]+@+\S+', email.get_attribute("href"))
        database_writer.writerow([teacher, title_description, email_text[0]])
        time.sleep(2)
