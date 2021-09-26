import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


def extract_data(page,job_posted):
    url = f'https://in.indeed.com/jobs?q=python+developer&l=India&fromage={job_posted}&taxo1=8GQeqOBVSO2eVhu55t0BMg&start={page}'
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content,'html5lib')

    div_tags = soup.find_all('div', class_ = "heading4 color-text-primary singleLineTitle tapItem-gutter")
    for tags in div_tags:
        title=tags.text.strip().replace('new',"")
        titles.append(title)

    div_tags = soup.find_all('span', class_="companyName")
    for tags in div_tags:
        company = tags.text.strip()
        companies.append(company)

    div_tags = soup.find_all('div', class_="companyLocation")
    for tags in div_tags:
        location = tags.text.strip()
        locations.append(location)

    div_tags = soup.find_all('div', class_="job-snippet")
    for tags in div_tags:
        job_summary = tags.text.strip()
        job_summarys.append(job_summary)

    for i in range(15):
        urls.append(url)


titles,companies,locations, job_summarys,urls= [],[],[],[],[]

data_aavailabe = ['1','7','14']
print(f"select to see jobs posted within specified days:{data_aavailabe}")
value = input("enter value\n")
page = input('enter page number to store the data,it should be multiple of 10:\n')
file_name = input('enter file name  where u can store jobs data\n')
if value in data_aavailabe:
    extract_data(page=page, job_posted=value)
else:
    print('not a valid page try again')



job_dict = {
            'title':[i for i in titles],
            'company':[i for i in companies],
            'location':[i for i in locations],
            'summary':[i for i in job_summarys],
            'Apply':[i for i in urls]
            }

df = pd.DataFrame(job_dict)
df.to_excel(f'{file_name}.xlsx')

