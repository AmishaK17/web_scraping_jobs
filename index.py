# Python program to perform web scraping using Beautiful Soup library.
# 1. Scraping a jobs website
# 2. Pulling info of the jobs that were posted a few days ago 
# 3. Filtering the jobs as per the skills possessed
# 4. Setting a delay of 10 minutes in subsequent scraping
# 5. Storing the relevant jobs in separate text files.

from bs4 import BeautifulSoup
import requests
import time

print("Mention the skills that you're not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(" ", "")
            skills = job.find('span', class_ = 'srp-skills').text.replace(" ", "")
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More info: {more_info}")
                print(f'File saved: {index}')
                    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)


# The .txt files in the posts folder consist of the results acquired 
# by mentioning django as the unfamiliar skill while running the program at a particular time
