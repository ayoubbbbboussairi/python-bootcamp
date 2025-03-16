import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest

job_tiltle = []
company_name = []
locat = []

result = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3808153047&f_JC=(0%2Clisystem%2Cgreen-jobs)&f_WT=1%2C3%2C2&geoId=102787409&keywords=%27sustainabilty%27%27life%20cycle%20assessment%27&location=Maroc&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R")
src = result.content
#create soup object to parse elements
soup = BeautifulSoup(src,'lxml')

#extract content
job_titles = soup.find_all('a',{'class':'disabled ember-view job-card-container__link job-card-list__title'})
company_names = soup.find_all('span',{'calss':'job-card-container__primary-description'})
location = soup.find_all('ly', {'class':'job-card-container__metadata-item'})

for i in range(len(job_titles)):
    job_tiltle.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    locat.append(location[i].text)

#creat and fill csv file
myfile = ["job_tiltle","company_name","locat"]
export = zip_longest(*myfile)
with open('C:\Users\user\Desktop\python_bootcamp\web scarping\scarp\jobs.csv', 'w') as file :
    wr = csv.writer(file)
    wr.writerow(export)

