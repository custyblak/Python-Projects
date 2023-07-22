from bs4 import BeautifulSoup
import requests

print('Input skills you are familiar with')
familiar_skills = input('> ').lower().split(',')
print(f'Searching for Job posts with {",".join(familiar_skills)}')

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
# Request a specific information from a website
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    Published_date = job.find('span', class_='sim-posted').span.text
    years_required = job.li.text[11:]
    if 'few' in Published_date and ('0' in years_required[0] or '1' in years_required[0]):
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')

        if any(skill in skills for skill in familiar_skills):
            link_to_job = job.header.h2.a['href']
            print(f'Company\'s Name: {company_name}')
            print(f'Required Skills:{skills}')
            print(f'Link:{link_to_job}')
            print(f'Years of experience: {years_required}')

            print('')
