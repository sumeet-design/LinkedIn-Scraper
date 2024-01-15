from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

#initializing driver 
driver = webdriver.Chrome()

#opening a website
url = "https://www.linkedin.com"
driver.get(url)
print("Website is opening..........")

time.sleep(3)

#clicking a button using xpath
log_but = "/html/body/nav/ul/li[4]/a/span"
#log_but = '//a[@href="https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs"]'
log_button = driver.find_element(By.XPATH,log_but)
log_button.click()
time.sleep(4)
#getting the page source after interactions

page_source = driver.page_source
# print(page_source)
driver.quit()
jt = []
cn = []
lc = []
pb = []


# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'lxml')

job_titles = soup.find_all(class_ = 'base-search-card__info')
for titles in job_titles:
    job_title = titles.find(class_ = 'base-search-card__title').text.strip()
    company_name = titles.find(class_ = 'base-search-card__subtitle').text.strip()
    location = titles.find(class_ = 'job-search-card__location').text.strip()
    try:
        published_date = titles.find(class_='job-search-card__listdate').text.strip()
    except:
        published_date = titles.find(class_ = 'job-search-card__listdate--new').text.strip()
    print("this is published date",published_date)
    # print("this is the job title i get from linked in ",job_title)
    
    jt.append(job_title)
    cn.append(company_name)
    lc.append(location)
    pb.append(published_date)

print(jt)

##SAVING INTO CSV FILE
df = pd.DataFrame({'Job Title': jt, 'Company Name': cn, 'Location': lc, 'Published Date': pb})
# Specifing the file name
file_name = 'output_data.csv'

# Saving the DataFrame to a CSV file
df.to_csv(file_name, index=False, encoding='utf-8')
    # print("this is title",titles.text)

print("Data saved successfully........")

###And today I finally learn how to scrap a data ............................